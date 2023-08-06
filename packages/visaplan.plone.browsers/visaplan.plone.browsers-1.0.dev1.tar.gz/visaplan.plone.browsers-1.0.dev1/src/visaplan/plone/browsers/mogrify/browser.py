# -*- coding: utf-8 -*- äöü
"""
Browser @@mogrify: transmogrifier-gestützte Im- und Exporte
"""
# Standardmodule:
from os.path import isfile, isdir
from posixpath import split as posix_split
from tempfile import NamedTemporaryFile
from tarfile import TarError
from time import strftime
from traceback import print_exc

# Plone/Zope/Dayta:
from AccessControl import Unauthorized
from zope.interface import classProvides, implements
from Globals import DevelopmentMode
from dayta.browser.public import BrowserView, implements, Interface
import transaction

# Unitracc-Tools:
from ...tools.forms import back_to_referer, tryagain_url, merge_qvars
from visaplan.tools.lands0 import (makeListOfStrings,
    list_of_strings, string_of_list,
    )
from ...tools.misc import getOption
from visaplan.tools.minifuncs import makeBool
from visaplan.tools.coding import (
    make_safe_decoder, purge_inapt_whitespace,
    )
from visaplan.tools.dicts import subdict

# Andere Browser und Adapter:

# Dieser Browser:
from .utils import (prefix_paths, make_prefixer,
        checked_sourcelist, make_childonly_filter,
        bool2text, wrapped_tarball,
        log_module,
        )
# blueprints-Modul: EchoTransform eingebunden per configure.zcml

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import pp
logger, debug_active, DEBUG = getLogSupport(fn=__file__)

try:
    # Installierte Module:
    from collective.transmogrifier.transmogrifier import (Transmogrifier,
            configuration_registry,
            )
except ImportError:
    logger.error('collective.transmogrifier nicht installiert!')
    Transmogrifier = (None, 'not installed')

try:
    # Nur in unserem Fork vorhanden:
    from quintagroup.transmogrifier.utils import get_info
    # (CHECKME: mutmaßlich nicht verwendet)
except ImportError:
    logger.error('quintagroup.transmogrifier nicht installiert!')
    get_info = (None, 'not installed')

from pprint import pformat
from pdb import set_trace

from xml.parsers.expat import ExpatError


# -------------------------------------------- [ Daten ... [
_FLAVOURS = [
             {'value': 'q-dir',
              'label': 'XML directory',
              },
             {'value': 'q-tarball',
              'label': 'XML tarball',
              },
             {'value': 'json-dir',
              'label': 'JSON directory',
              },
             ][:-1] # json-dir deaktiviert
_FLAVOUR_KEYS = set([dic['value'] for dic in _FLAVOURS])
_EXPORT_CHOICES = [
            {'value': 'zopeexport',
             'label': 'Export (tar archive or tree of zexp files)',
             },
            {'value': 'structuregroups',
             'label': 'Create Author and Reader groups',
             },
            {'value': 'catalog',
             'label': '(Re-) Catalog given ressources',
             },
            {'value': 'export_folderprops',
             'label': 'Export folder properties, including UIDs'
                      ' (export_folderprops.cfg)'
             },
            ]
_IMPORT_CHOICES = [
            {'value': 'zopeimport',
             'label': 'Import (.zexp files)'
                      ' (zopeimport.cfg)'
             },
            {'value': 'import',
             'label': 'Import (commonly proposed version)'
                      ' (import.cfg)'
             },
            {'value': 'demarshall',
             'label': 'Import exported properties, including UIDs'
                      ' (demarshall.cfg)'
             },
            ]
_DEBUG_CHOICES = [
            {'value': 0,
             'label': 'Off',
             },
            {'value': 1,
             'label': 'Enable "debug" option for blueprints which use it',
             },
            {'value': 2,
             'label': 'Like before, and trigger pdb.set_trace immediately',
             },
        ]
_TRACE_OPTIONS = [  # Schlüssel gewählt nach getOption-Argumenten
        {'key': 'debug',
         'label': 'debug mode'
                  ' (used by some blueprints to trigger pdb.set_trace)',
         'factory': makeBool,
         },
        {'key': 'trace-first',
         'label': 'Trace first item'
                  ' (used by some blueprints)',
         'factory': makeBool,
         },
        {'key': 'debug-ids',
         'label': 'IDs to trigger debugging'
                  ' (used by some blueprints)',
         'factory': makeListOfStrings,
         'reverse': string_of_list,  # Vorgabewert: str
         },
        ]
def not_key(s):
    return s != 'key'
_TRACE_DLIST = [
        (dic['key'],
         subdict(dic, keyfunc=not_key),
         )
        for dic in _TRACE_OPTIONS
        ]
_TRACE_ODICT = dict(_TRACE_DLIST)
pp((_TRACE_OPTIONS,
        _TRACE_ODICT,
        ))
del not_key
# -------------------------------------------- ] ... Daten ]

safe_decode = make_safe_decoder(refinefunc=purge_inapt_whitespace)


class IMogrify(Interface):
    """
    Interface des @@mogrify-Browsers
    """

    def listConfigurationIds(self):
        """
        Gib die IDs der registrierten Exportprofile zurück
        """

    def formdata(self):
        """
        Vorbelegungen für das Suchformular
        """

    def import_tarball(self):
        """
        Importiere die als "Tarball" (tar-Archiv, .tar.gz) hochgeladenen Objekte
        """
        # Die Methode kann nicht "import" genannt werden - wegen des Schlüsselworts ...
        # (leider von der Vim-Syntaxhervorhebung nicht beanstandet)

    def export(self):
        """
        Exportiere die angegebenen Objekte
        und alle per UID referenzierten Ressourcen
        """

    def export_uids(self):
        """
        Exportiere die UIDs gemäß der in uids.cfg gepflegten Liste
        """

    def perform(self):
        """
        führe eine anzugebende Konfiguration aus
        """


class Browser(BrowserView):

    implements(IMogrify)

    def listConfigurationIds(self):
        """
        Gib die IDs der registrierten Exportprofile zurück
        """
        return configuration_registry.listConfigurationIds()

    def formdata(self, forform=True):
        """
        Vorbelegungen für das Import- oder Exportformular
        """
        tmp = self._formdata(noisy=not forform, forform=forform)
        if forform:
            flavour = tmp['flavour']
            liz = []
            for dic in _FLAVOURS:
                dic['selected'] = flavour == dic['value']
                liz.append(dic)
            tmp['flavour-choices'] = liz
            # hier kein selected-Schlüssel:
            tmp['export-cfg-choices'] = _EXPORT_CHOICES
            tmp['import-cfg-choices'] = _IMPORT_CHOICES
            # für Formular:
            tmp['DevelopmentMode'] = DevelopmentMode
            if DevelopmentMode:
                tmp['debug-choices'] = _DEBUG_CHOICES
        else:
            # nicht für Formular, sondern für Ausführung;
            context = self.context
            rootfolder = context.getBrowser('unitraccfeature').rootfolder()
            rooted = make_prefixer(rootfolder)
            prefix = tmp['path-prefix']
            if prefix:
                prefix = rooted(prefix)
            if not tmp['path']:
                if prefix and prefix != rooted('/'):
                    tmp['path'] = [prefix]
            elif prefix:
                tmp['path'] = prefix_paths(tmp['path'], make_prefixer(prefix))
            else:
                tmp['path'] = prefix_paths(tmp['path'], rooted)

            # Angegebene Pfade nicht oberhalb des Kontextes
            # (ergibt ggf. ValueError):
            notabove = context.getPath()
            childonly = make_childonly_filter(notabove)
            for p in tmp['path']:
                childonly(p)

            # für Verarbeitung durch transmogrifier:
            for boo in ('exclude-contained',):
                tmp[boo] = bool2text(tmp[boo])
            # alle nicht für transmogrifier bestimmten Angaben entfernen:
            for obs in ('path_multiline', 'path-prefix'):
                # nur set hat die discard-Methode ...
                del tmp[obs]
        # sowohl für Formular als auch für transmogrifier:
        tmp['path'] = string_of_list(tmp['path'])
        return tmp

    def _get_virtual_path(self, request=None):
        """
        Virtuellen Pfad ermitteln, ohne Methodenkomponente
        """
        if request is None:
            request = self.context.REQUEST
        vhp = request['VIRTUAL_URL_PARTS']
        head, tail = posix_split(vhp[1])
        if tail in ('edit', 'view', 'transmex', 'transmin'):
            return head
        return vhp

    # @print_call_and_result
    # @trace_this
    def _formdata(self, noisy, forform):
        """
        Vorbelegungen für das Import- und Exportformular
        """
        context = self.context
        request = context.REQUEST
        virtual_path = self._get_virtual_path(request)
        form = request.form
        if 0:
            pp(form)
            pp([a for a in dir(context)
                    if 'path' in a.lower()
                    ])
        res = {}
        # val = form.get('exclude-contained')
        res['flavour'] = form.get('flavour', 'q-tarball')
        # res['exclude-contained'] = makeBool(val, 'no')
        res['exclude-contained'] = getOption(form, 'exclude-contained',
                                             'no', makeBool)
        res['export-cfg'] = form.get('export-cfg', 'zopeexport')
        # für Import:
        res['import-cfg'] = form.get('import-cfg', 'zopeimport')
        res['source'] = form.get('source')

        res['flavour'] = getOption(form, 'flavour',
                                   # wenn Importkonfiguration,
                                   # oder "unechte" Exportkonfiguration,
                                   # ist 'flavour' optional:
                                   default=(res['import-cfg'] or
                                            'export' not in (res['export-cfg'] or '')
                                            ) and ' '
                                              or  None,
                                   choices=_FLAVOUR_KEYS)
        res['path'] = list_of_strings(form.get('path') or virtual_path)
        # steuert, ob ein mehrzeiliges Eingabefeld ausgegeben wird:
        res['path_multiline'] = (res['path'][1:]
                                 and True
                                 or makeBool(form.get('path_multiline', 'no')))

        res['verbose'] = getOption(form, 'verbose', 'no', makeBool)
        res['use-transactions'] = getOption(form, 'use-transactions', 'no', makeBool)
        res['path-prefix'] = context.getPath()
        res['output-prefix'] = form.get('output-prefix', '').strip('/')
        # optionale Werte:
        for key in ('existing',
                    'config-id',
                    'skip-leading',
                    'add-members',
                    'whitelist',
                    ):
            if key in form:
                res[key] = form[key]
        # Spezielle Behandlung der Debug-Optionen:
        # - jedenfalls auswerten und in Ergebnis schreiben
        # - nur im Entwicklungsmodus in speziellen Schlüssel
        #   debug-options kopieren
        dbg_options = {}
        if DevelopmentMode:
            res['debug-options'] = dbg_options
        for dic in _TRACE_OPTIONS:
            val = getOption(form, **dic)
            if val is None:
                continue
            # Transformation zu Strings für transmogrifier: nicht hier ...
            if forform:
                f = dic.get('reverse')
                if f is not None:
                    val = f(val)
            key = dic['key']
            dbg_options[key] = res[key] = val
        if noisy and not DevelopmentMode:
            message = context.getAdapter('message')
            for key, val in dbg_options.items():
                logger.warn('Debugging option %(key)s '
                          'ignored (%(val)r)', locals())
                message('Debugging option ${key} '
                          'ignored ("${val}")',
                        'warning',
                        mapping=locals())
        return res

    # @trace_this
    def import_tarball(self):
        """
        Importiere die als "Tarball" (tar-Archiv, .tar.gz) hochgeladenen Objekte
        """
        context = self.context
        message = context.getAdapter('message')
        form = self.formdata(False)
        use_cfg = form['import-cfg']
        ok = False
        reader_options = {'prefix': '',
                          }
        try:
            flavour = form.get('flavour')
            source = form.get('source')
            if flavour == 'q-tarball':
                fui = form.get('upload')  # ZPublisher.HTTPRequest.FileUpload-Instanz
                if form.get('debug'):
                    pp(form)
                    set_trace()  # debug angefordert
                if fui:  # XXX reicht vermutlich nicht!
                    # pp(dict(fui.headers.dict))
                    content_type = fui.headers.dict['content-type']
                    with NamedTemporaryFile(delete=False) as tmpfile:
                        tmpfile.write(fui.read())
                        source = tmpfile.name
                        logger.info('import_tarball: storing uploaded %(content_type)r'
                                    ' file to %(source)r',
                                    locals())
                    ok = True
                    #  'content-disposition': 'form-data; name="upload"; filename="name.tar.gz"'
                elif source:
                    if isfile(source):
                        ok = True
                    else:
                        message('File ${source} not found!',
                                'error',
                                mapping=locals())
                else:
                    message('Please upload an archive file,'
                            ' or specify an existing file on the server!',
                            'error')
                reader_options.update({
                    'context': 'tarball',
                    'path': source,
                    })
            else:
                if source:
                    if isdir(source):
                        ok = True
                    else:
                        message('Directory ${source} not found!',
                                'error',
                                mapping=locals())
                else:
                    message('Please specify an existing directory on the server!',
                            'error')
                reader_options.update({
                    'context': 'directory',
                    'path': source,
                    })
        except KeyError as e:
            message(str(e), 'error')
        finally:
            # pp(dict(form))
            if flavour == 'json-dir':
                message('Import type ${flavour} not yet supported!',
                        'error',
                        mapping=locals())
                ok = False

            if not ok:
                return back_to_referer(context, url='transmin', detect_browser=True)

            working = False
            use_transactions = form['use-transactions']
            try:
                transmogrifier = Transmogrifier(context)
                use_cfg = form.get('import-cfg')
                if 'existing' in form:
                    reader_options['existing'] = form['existing']
                kwargs = {'reader': reader_options,
                          }
                if form.get('debug'):
                    pp({'use_cfg': use_cfg, 'kwargs': kwargs, })
                    set_trace()  # debug angefordert
                if use_transactions:
                    transaction.begin()
                    logger.info('transaction started')
                    working = True
                if kwargs:
                    logger.info('import_tarball: use_cfg=%r, kwargs=\n%s',
                                use_cfg,
                                pformat(kwargs))
                else:
                    logger.info('import_tarball: use_cfg=%r', use_cfg)
                tm = transmogrifier(use_cfg,
                                    **kwargs)
            except (OSError, TarError) as e:
                logger.exception(e)
                log_module(logger, e)
                message(str(e), 'error')
                if working:
                    transaction.abort()
                    logger.info('transaction aborted')
            except Exception as e:
                # print dir(e)
                logger.error('Unerwarteter Fehler: %(e)s', locals())
                logger.exception(e)
                log_module(logger, e)
                if working:
                    transaction.abort()
                    logger.info('transaction aborted')
                message(str(e), 'error')
            else:
                logger.info('import_tarball: successful')
                message('Import successful!')
                if working:
                    transaction.commit()
                    logger.info('transaction committed')
            return back_to_referer(context, url='transmin', detect_browser=True)


    # @trace_this
    def export(self):
        """
        Exportiere *oder katalogisiere* die angegebenen Objekte
        und alle per UID referenzierten Ressourcen
        """
        context = self.context
        getBrowser = context.getBrowser
        message = context.getAdapter('message')
        result = None
        working = False
        try:
            form = self.formdata(False)
            use_cfg = form['export-cfg']
            export_type = 'export' in use_cfg
            use_transactions = form['use-transactions']
            if export_type:
                flavour = form['flavour']
                if flavour not in _FLAVOUR_KEYS:
                    raise ValueError('Unknown export flavour %(flavour)r!'
                                     % form)
                if flavour.endswith('tarball'):
                    download = True
                    writer_opts = {'context': 'tarball',
                                   'prefix': '',
                                   }
                elif flavour == 'json-dir':
                    raise ValueError('Noch nicht implementiert')
                elif flavour.endswith('dir'):
                    download = False
                    writer_opts = {'context': 'directory',
                                   'prefix': form['output-prefix']
                                             or strftime('%Y%m%d-%H%M%S'),
                                   }
                else:
                    raise ValueError('%(flavour)r: nicht tarball, nicht dir?!'
                                     % locals())
                allow_root = False
            else:
                allow_root = True
                download = False
                writer_opts = {}
            propertiesexporter_opts = {
                    'helper_kwargs': {
                        'safe_decode': safe_decode,
                        }
                    }
            uidextractor_opts = dict(propertiesexporter_opts)
            if 1:
                # Die angegebenen Pfade sind absolut;
                # nun die Portalwurzel verwenden, wg. der referenzierten Ressourcen:
                portal = context.getAdapter('portal')()
                portal_path = portal.getPath()
                transmogrifier = Transmogrifier(portal)
                logger.info('transmogrifier created')
                if 0:
                    print '*'*79
                    print 'path, vorher:', form['path']
                    print '*'*79
                sitewalker_opts = {
                        'start-path': checked_sourcelist(form['path'], portal_path,
                                                         allow_empty=False,
                                                         allow_root=allow_root,
                                                         as_string=True),
                        'exclude-contained': form['exclude-contained'],
                        }
                manifestexporter_opts = {'path': sitewalker_opts['start-path'],
                                         }
                # Es wird sinnvollerweise nur *entweder* eine sitewalker-
                # *oder* eine manifestexporter-Sektion die Daten liefern; in
                # den kwargs stehen vorerst beide.  Die summary-Sektion gibt
                # nur die Optionen der tatsächlich verwendeten Sektionen aus.
                kwargs = dict(sitewalker=sitewalker_opts,
                              manifestexporter=manifestexporter_opts,
                              uidextractor=uidextractor_opts,
                              propertiesexporter=propertiesexporter_opts,
                              subportal={'verbose': '2'},
                              reindex={'verbose': 'true'},
                              summary={'print-sections': 'true'},
                              writer=writer_opts)
                dbg_options = form.get('debug-options', {})
                if dbg_options:
                    if DevelopmentMode:
                        # Entwicklungsmodus: Debug-Optionen anwenden
                        for key, val in dbg_options.items():
                            f = _TRACE_ODICT[key].get('reverse', str)
                            dbg_options[key] = f(val)
                        # eine Flash-Message als Hinweis auf etwaiges set_trace
                        # wäre sinnfrei, da erst beim Laden der Ergebnisseite angezeigt ...
                        # Alle Blueprints ignorieren die ihnen unbekannten Optionen.
                        for dic in kwargs.values():
                            dic.update(dbg_options)
                    else:
                        message('Development mode disabled.')
                if use_transactions:
                    transaction.begin()
                    logger.info('transaction started')
                    working = True
                if form.get('debug'):
                    pp(kwargs)
                    print '*'*79
                    set_trace()  # debug angefordert
                tm = transmogrifier(use_cfg, **kwargs)
                logger.info('transmogrifier executed')
                if form.get('debug'):
                    pp((('transmogrifier:', transmogrifier),
                        ('transmogrifier(...) -->', tm),  # kaum prakt. Nährwert
                        ))
                result = self.handle_export(transmogrifier, download, context)
        except ExpatError as e:
            logger.error('ExpatError while transmogrificating!')
            logger.exception(e)
            ei = {}
            for a in ('code', 'lineno', 'offset'):
                ei[a] = getattr(e, a, None)
                logger.info('ExpatError: e.%-10s %r', a+':', ei[a])
                # print 'e.%-10s %r' % (a+':', ei[a])
            # print_exc()
            if working:
                transaction.abort()
                logger.info('transaction aborted')
            raise
        except (Exception) as e:
            message(e.__class__.__name__+': '+str(e), 'error')
            logger.exception(e)
            logger.error(str(e))
            if working:
                transaction.abort()
                logger.info('transaction aborted')
        else:
            if working:
                transaction.commit()
                logger.info('transaction committed')
        finally:
            if result is None:
                return back_to_referer(context,
                                       url='transmex', detect_browser=True)
            return result

    def handle_export(self, tm, download=None, context=None):
        """
        Generische Behandlung des Exportergebnisses

        tm -- der Transmogrifier
        download -- Wahrheitswert: wird eine Datei zum Download dargeboten?
        context -- der Kontext
        """
        if context is None:
            context = self.context
        message = context.getAdapter('message')
        result = None
        for chunk in tm.get_info(category='export_context'):
            # pp(('chunk:', chunk))
            info = chunk['info']
            if info['context_type'] == 'tarball':
                # es kann nur einen geben ...
                if result is None:
                    # Seiteneffekt: RESPONSE-Header
                    result = wrapped_tarball(info['context'], context)
                    logger.info('Returning tarball!')
                else:
                    logger.error('Surplus tarball!')
                if download is None:
                    download = True
            elif info['context_type'] == 'directory':
                message("Exported to directory '${output_dir}'",
                        mapping=info)
                if download is None:
                    download = False
            else:
                print 'info.keys() =', info.keys()
                # import pdb; pdb.set_trace()
                logger.error('Unsupported export_context of type '
                             '%(context_type)r: %(context)r',
                             info)
                print dir(info['context'])
        if result is not None:
            return result
        elif download is None:
            logger.error("No info['context_type'], no download value!")
            message('A problem occurred; please contact support.',
                    'warning')
        elif download:
            logger.error('No tarball written!')
            message('No tarball written!',
                    'error')
        else:
            message('Export successful')

    def export_uids(self):
        """
        Exportiere die UIDs gemäß der in uids.cfg gepflegten Liste
        """
        context = self.context
        message = context.getAdapter('message')
        result = None
        try:
            portal = context.getAdapter('portal')()
            portal_path = portal.getPath()
            transmogrifier = Transmogrifier(portal)
            tm = transmogrifier('uids')
            result = self.handle_export(transmogrifier,
                                        context=context)
        except ExpatError as e:
            print 'exception:', e
            ei = {}
            for a in ('code', 'lineno', 'offset'):
                ei[a] = getattr(e, a, None)
                print 'e.%-10s %r' % (a+':', ei[a])
            print_exc()
            raise
        except (Exception) as e:
            message(e.__class__.__name__+': '+str(e), 'error')
            logger.exception(e)
            logger.error(str(e))
        finally:
            if result is None:
                return back_to_referer(context,
                                       url='transmex', detect_browser=True)
            return result

    def perform(self):
        """
        führe eine anzugebende Konfiguration aus
        """
        context = self.context
        getBrowser = context.getBrowser
        message = context.getAdapter('message')
        result = None
        try:
            form = self.formdata(False)
            config_id = form['config-id']
            sitewalker_opts = subdict(form,
                                      ['exclude-contained',
                                       ])
            sitewalker_opts['start-path'] = form['path']
            groupargs = subdict(form, ['add-members', 'whitelist', 'exclude-contained'])
            portal = context.getAdapter('portal')()
            portal_path = portal.getPath()
            transmogrifier = Transmogrifier(portal)
            kwargs = {'sitewalker': sitewalker_opts,
                      'structuregroups': groupargs,
            }
            tm = transmogrifier(config_id, **kwargs)
        except (Exception) as e:
            message(e.__class__.__name__+': '+str(e), 'error')
            logger.exception(e)
            logger.error(str(e))
        finally:
            if result is None:
                return back_to_referer(context,
                                       url='transmogrify', detect_browser=True)


# vim: ts=8 sts=4 sw=4 si et
