# -*- coding: utf-8 -*- äöü
"""
@@mogrify.blueprints
"""

# Standardmodule:
from pprint import pprint
import HTMLParser
from posixpath import (normpath as posix_normpath,
        split as posix_split, join as posix_join,
        splitext,
        )

# Plone/Zope:
from zope.interface import classProvides, implements
from Products.Marshall import registry
from Products.Archetypes.interfaces import IBaseObject
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.context import (
        DirectoryExportContext, DirectoryImportContext,
        TarballExportContext, TarballImportContext,
        )
from OFS.ObjectManager import BadRequestException
from ZODB.POSException import ConflictError

# Installierte Module:
from collective.transmogrifier.interfaces import ISection, ISectionBlueprint
from collective.transmogrifier.utils import defaultKeys, Matcher, traverse
from collective.transmogrifier.utils import defaultMatcher
from collective.transmogrifier.utils import make_itemInfo
from quintagroup.transmogrifier.propertymanager import Helper as PropertyHelper
from quintagroup.transmogrifier.utils import make_skipfunc
from bs4 import BeautifulSoup

# Unitracc-Tools:
from visaplan.tools.lands0 import lines_to_list, makeListOfStrings
from visaplan.tools.classes import Counter  # -> collections.Counter oder defaultdict
from ...tools.misc import getOption
from visaplan.tools.minifuncs import makeBool, NoneOrInt

from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)

# Andere Browser:
from ..unitraccgroups.utils import generic_group_id, STRUCTURE_GROUP_SUFFIXES

# Dieser Browser:
from .utils import (all_uids, make_readableNameFactory, make_dirProxy,
        make_pathFilter,
        )
from .visaplan._base import BaseSection

__all__ = []
from pdb import set_trace


class EchoTransform(BaseSection):
    """
    Inhalte einfach ausgeben und weiterreichen
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        # BaseSection.__init__(self, transmogrifier, name, options, previous)

    def __iter__(self):
        prefix = self.name.join(('[', ']:'))
        count = self.count
        for item in self.previous:
            count('passed-through')
            pprint((prefix, item))
            yield item


class UidExtractor(BaseSection):
    """
    Per UID referenzierte Objekte ermitteln und in die Pipeline injizieren.

    Dies muß *vor* der "eigentlichen" Extraktion der redaktionellen Inhalte
    geschehen, weil die Inhalte der ermittelten Objekte ja ebenfalls benötigt
    werden!

    Daß die *untersuchten* Inhalte somit zweimal extrahiert werden,
    wird dabei hingenommen.

    Konfiguration:

    inspect_fields - die zu untersuchenden Felder; Beispiel:
             [uidextractor]
             blueprint = visaplan.transmogrifier.uidextractor
             inspect_fields =
                  text
                  description
    """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        # set_trace()
        # BaseSection.__init__(self, transmogrifier, name, options, previous)
        self._store_initial_args(transmogrifier, name, options, previous)

        print name.join((' [', '].init'))
        # Wenn's funktioniert, *dringend* gut kommentieren!
        # Die item-Dicts haben einen Schlüssel '_path'
        if 'path-key' in options:
            pathkeys = options['path-key'].splitlines()
        else:
            pathkeys = defaultKeys(options['blueprint'], name, 'path')
        self.pathkey = Matcher(*pathkeys)

        if 'inspect_fields' in options:
            inspect_fields = lines_to_list(options['inspect_fields'])
        else:
            inspect_fields = ['text']

        #  0: keine Rekursion (nur übergebene Objekte untersuchen)
        # -1: unbegrenzte Rekursion
        self.maxdepth = getOption(options, 'max-recursions', '10', NoneOrInt)
        if self.maxdepth is None:
            self.maxdepth = -1
        # self.verbose aus BaseSection._set_debugging_options:
        self._skip_this = make_skipfunc(whitelist=inspect_fields,
                                        verbose=self.verbose,
                                        default_blacklist=[
                                            'id',
                                            'generateStructureNumber',
                                            'subPortals',
                                            'code',
                                            ])
        # helper_kwargs sind gegenwärtig die einzige Möglichkeit, dem Helper
        # Argumente zu übergeben, z. B. eine safe_decode-Funktion.
        # helper_kwargs = options.get('helper_kwargs', {})

        # aus q.t.marshall.MarshallerSection:
        self.excludekey = defaultMatcher(options, 'exclude-key',
                                         name, 'excluded_fields')
        self.exclude = filter(None, [i.strip() for i in
                              options.get('exclude', '').splitlines()])

        self.atxml = registry.getComponent("atxml")
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):
        prefix = self.name.join(('[', '].iter:'))
        print ' ' + prefix[:-1]
        skip = self._skip_this
        counter = Counter()
        count = self.count
        UIDs_in = set()   # UIDs der verarbeiteten Objekte
        UIDs_out = set()  # von dieser Sektion gefundene UIDs
        recursion = 0     # nullte Rekursion: übergebene Objekte
        itemInfo = make_itemInfo(self.name)
        trace1st = self.trace1st
        # set_trace()

        pc = self.context.getAdapter('pc')()

        for item in self.previous:
            count('got')

            pathkey = self.pathkey(*item.keys())[0]
            path = item[pathkey]

            # obj = traverse(self.context, str(path).lstrip('/'), None)
            obj = self.context.unrestrictedTraverse(path, None)
            if obj is None:  # path doesn't exist
                count('forwarded')
                itemInfo(item)  #, trace=trace1st)
                yield item
                continue

            if not IBaseObject.providedBy(obj):
                count('unsupported')
                count('forwarded')
                yield item
                continue

            # get list of excluded fields given in options and in item
            excludekey = self.excludekey(*item.keys())[0]
            atns_exclude = tuple(self.exclude)
            if excludekey:
                atns_exclude = tuple(set(item[excludekey]) | set(atns_exclude))

            for dic in self._generate_new_dicts(
                    obj,       # das Objekt
                    atns_exclude, # gar nicht erst zu extrahieren
                    recursion,    # 0 für ersten Durchlauf
                    UIDs_in,      # set: UIDs der übergebenen Objekte
                    UIDs_out,     # set: gefundene UIDs
                    counter):  # der spezielle Zähler
                yield dic
                count('created')

            count('forwarded')
            yield item
            itemInfo(item)  #, trace=trace1st)
            continue

        # jetzt Rekursion: gefundene UIDs zu Objekten auflösen und diese auslesen
        countdown = self.maxdepth  # -1: keine Begrenzung!
        # die hier erzeugten dicts haben keine eigene Festlegung:
        atns_exclude = tuple(set(self.exclude))
        pc = self.context.getAdapter('pc')()
        while countdown:
            countdown -= 1
            if not UIDs_out:
                break
            recursion += 1
            logger.info('%(prefix)s %(recursion)d. Rekursion', locals())
            uids = list(UIDs_out)
            UIDs_out.clear()
            for uid in uids:
                brains = pc(UID=uid)
                if not brains:
                    counter[('uid', 'misses')] += 1
                    continue
                if brains[1:]:
                    counter[('uid', 'ambiguous', uid)] += 1
                for brain in brains:
                    for dic in self._generate_new_dicts(
                            brain.getObject(),
                            atns_exclude, # gar nicht erst zu extrahieren
                            recursion,    # 0 für ersten Durchlauf
                            UIDs_in,      # set: UIDs der übergebenen Objekte
                            UIDs_out,     # set: gefundene UIDs
                            counter):  # der spezielle Zähler
                        yield dic
                        count('created')

        ende = UIDs_out and 'Abbruch' or 'Ende'
        if self.maxdepth > 0:
            recursions = '%d/%d' % (recursion, self.maxdepth)
        else:
            recursions = str(recursion)

        logger.info('%(prefix)s %(ende)s nach %(recursions)s Rekursionen',
                    locals())
        if UIDs_out:
            unresolved = len(UIDs_out)
            logger.warning('%(prefix)s %(unresolved)d UIDs nicht untersucht',
                           locals())

        pprint(dict(counter))

    def _generate_new_dicts(self,
            obj,
            atns_exclude,
            recursion,    # 0 für ersten Durchlauf
            UIDs_in,      # set: UIDs der übergebenen Objekte
            UIDs_out,     # set: gefundene UIDs
            counter):
        """
        Generiere neue item-Dicts aus den UIDs, die im übergebenen Objekt
        gefunden werden.

        Schon gefundene UIDs sowie Zähler werden in übergebenen Objekten
        vorgehalten.

        UIDs_in - diesem Set werden nur UIDs von Objekte hinzugefügt, die von
                  dieser Methode analysiert wurden.

        UIDs_out - diesem Set werden die gefundenen UIDs hinzugefügt (sofern
                   sie nicht schon im ersten Set enthalten sind).
                   Es wird für jede Iteration zurückgesetzt; wenn keine neuen
                   UIDs mehr gefunden wurden, kann die Verarbeitung beendet
                   werden

        """
        if obj is None:
            if recursion:
                counter[('uid', 'unresolved')] += 1
            return
        myuid = None
        try:
            try:
                myuid = obj.getUID()
                if myuid in UIDs_in:
                    return
                UIDs_in.add(myuid)
            except Exception as e:
                logger.exception(e)

            content_type, length, data = \
                    self.atxml.marshall(obj, atns_exclude=atns_exclude)
            if 0:
                print '\n'.join(['MarshallerSection:', ' * content_type: %r' % (content_type,), ' * length:       %r' % (length,), ' * data:         %r' % (data,)])
        except ConflictError:
            raise
        except Exception:
            data = None
        else:
            xmlsoup = BeautifulSoup(data)
            pc = self.context.getAdapter('pc')()
            unescape_html = HTMLParser.HTMLParser().unescape
            skip = self._skip_this
            for elem in xmlsoup.find_all('field'):
                # print elem
                elem_name = elem['name']
                if skip(elem_name):
                    counter[('skipped', 'byname', elem_name)] += 1
                    continue
                if not elem.string:
                    counter[('skipped', 'empty', elem['mimetype'])
                            ] += 1
                    continue
                if 0:\
                pprint([('name:',     elem_name),
                        ('mimetype:', elem['mimetype']),
                        ])
                for uid in all_uids(elem, unescape_html):
                    counter[('uid', 'extracted')] += 1
                    counter[('uid', 'extracted', 'recursion', recursion)] += 1
                    counter[('uid', 'extracted', 'from-field', elem_name)] += 1
                    if uid in UIDs_in:
                        counter[('uid', 'duplicates', 'parents')] += 1
                        continue
                    if uid in UIDs_out:
                        counter[('uid', 'duplicates', 'siblings')] += 1
                        continue

                    first = not UIDs_in and 0  # nur für Debugging
                    UIDs_out.add(uid)
                    brains = pc(UID=uid)
                    if not brains:
                        counter[('uid', 'misses')] += 1
                        continue
                    if brains[1:]:
                        counter[('uid', 'ambiguous', uid)] += 1
                    found = False
                    for brain in brains:
                        if first:
                            pprint(dir(brain))
                            # set_trace()
                        try:
                            o = brain.getObject()
                            if o is None:
                                counter[('uid', 'zombie-brains')
                                        ] += 1
                                continue
                            counter[('uid', 'resolved')
                                    ] += 1
                            dic = {'_path': o.getPath(),
                                   '_type': o.getPortalTypeName(),
                                   }
                            yield dic
                            # itemInfo(dic, trace=trace1st)
                            # pprint(('yielded:', dic))
                            break

                        except AttributeError as e:
                            print dir(brain)
                            logger.exception(e)
                            # set_trace()
                    if not found:
                        counter[('uid', 'unresolved')] += 1


class OrphansOnly(BaseSection):
    """
    Verwirf alle Objekte, die Eltern haben
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)

        # Wenn's funktioniert, *dringend* gut kommentieren!
        # Die item-Dicts haben einen Schlüssel '_path'
        if 'path-key' in options:
            pathkeys = options['path-key'].splitlines()
        else:
            pathkeys = defaultKeys(options['blueprint'], name, 'path')
        self.pathkey = Matcher(*pathkeys)
        self.sep = options.get('sep', '/')
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):
        """
        Puffere zunächst alle vorhandenen Objekte und sortiere sie nach Pfad;
        verwirf dann alle, die ein Eltern- oder auch ein entfernteres
        Vorfahrenobjekt in der Pipeline haben.

        Duplikate werden implizit ebenfalls verworfen.
        """
        count = self.count
        pathkey = self.pathkey
        sep = self.sep
        sortable = []
        for item in self.previous:
            count('got')

            key = pathkey(*item.keys())[0]
            if key is None:
                # hat keine Pfadinformation; ist also ein anderes Dings,
                # das hier nicht behandelt wird:
                count('ignored')
                count('forwarded')
                yield item
            else:
                path = item[key]
                tup = tuple(path.split(sep))
                sortable.append((tup, item))

        sortable.sort()
        prevtup = ()
        prevlen = 99
        for tup, item in sortable:
            if tup[:prevlen] == prevtup:
                count('dropped')
                continue
            prevlen = len(tup)
            prevtup = tup
            count('forwarded')
            yield item


class ZopeExport(BaseSection):
    """
    Verwende die Zope-Standardfunktionalität zum Export von Objekten.
    Zur Vorbereitung ist eine OrphansOnly-Sektion zu empfehlen!
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)

        # aus quintagroup.transmogrifier.writer.WriterSection:
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')

        has_prefix = 'prefix' in options
        if 'prefix' in options:
            self.prefix = options['prefix'].strip()
        else:
            self.prefix = ''

        context_type = getOption(options, 'context',
                                 choices=['tarball',
                                          'directory',
                                          ])
        info = {'context_type': context_type,
                }

        context = self.context
        setup_tool = getToolByName(context, 'portal_setup')
        if context_type == 'directory':
            profile_path = posix_normpath('/'.join(
                filter(None, (options.get('path', ''),
                              self.prefix,
                              ))))
            info['output_dir'] = profile_path
            self.export_context = DirectoryExportContext(setup_tool, profile_path)
        elif context_type == 'tarball':
            self.export_context = TarballExportContext(setup_tool)
        else:
            raise ValueError('Unsupported export context: %r'
                             % (context_type,))
        info['context'] = self.export_context
        transmogrifier.add_info('export_context',
                 name,
                 info)

        # toxml-Argument des Standard-Exportformulars:
        self.xmlformat = getOption(options, 'xml-format', 'no', makeBool)
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):
        """
        exportiere alle exportierbaren Objekte

        Exportierbar ist alles, was eine Pfadinformation hat.
        """
        pathkey = self.pathkey
        context = self.context
        export_context = self.export_context
        xmlformat = self.xmlformat
        logprefix = '[%s]:' % self.name
        if xmlformat:
            ext = '.xml'
            contenttype = 'text/xml'
        else:
            ext = '.zexp'
            contenttype = 'application/octet-stream'

        count = self.count
        prevdir = None
        for item in self.previous:
            count('got')
            item['_export_context'] = self.export_context

            key = pathkey(*item.keys())[0]

            if not key:  # path doesn't exist
                count('no-key')
                count('forwarded')
                yield item
                continue

            path = item[key]
            if not path:
                count('no-path')
                count('forwarded')
                yield item
                continue

            subdir, name = posix_split(posix_normpath(path))
            if subdir != prevdir:
                parent = subdir and traverse(context, subdir) or context
                prevdir = subdir

            doit = 0
            try:
                data = parent.manage_exportObject(name, True, xmlformat)
                doit = 1
            except Exception as e:
                print path
                logger.exception(e)
                logger.error('%(logprefix)s can\'t export %(path)s', locals())
                if 0:
                    set_trace()
                    data = parent.manage_exportObject(name, True, xmlformat)

            if doit:
                export_context.writeDataFile(name+ext, data,
                                             contenttype, subdir=subdir)
                count('written')
                count('forwarded')
            else:
                count('errors')
                count('not-forwarded')
            yield item


class ZopeImport(BaseSection):
    """
    Verwende die Zope-Standardfunktionalität zum Import von Objekten.
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)

        # aus quintagroup.transmogrifier.writer.WriterSection:
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')

        has_prefix = 'prefix' in options
        if 'prefix' in options:
            self.prefix = options['prefix'].strip()
        else:
            self.prefix = ''

        context_type = getOption(options, 'context',
                                 choices=['tarball',
                                          'directory',
                                          ])
        info = {'context_type': context_type,
                }

        context = self.context
        setup_tool = getToolByName(context, 'portal_setup')
        if context_type == 'directory':
            profile_path = options.get('path', '')
            info['output_dir'] = posix_normpath('/'.join(filter(None, (profile_path,
                                                        self.prefix,
                                                        ))))
            self.import_context = DirectoryImportContext(setup_tool, profile_path)
        elif context_type == 'tarball':
            self.import_context = TarballImportContext(setup_tool)
        else:
            raise ValueError('Unsupported export context: %r'
                             % (context_type,))
        info['context'] = self.import_context
        # Von Verzeichnissen können Dateien direkt gelesen werden:
        self.passthrough = context_type == 'directory'
        # irrelevant für Verzeichnisse (dann keine temporären Dateien nötig):
        self.single_tmpfile = getOption(options, 'use-single-tmpfile', 'yes', makeBool)
        self.verify = getOption(options, 'verify-imports', 'no', makeBool)
        self.take_ownership = getOption(options, 'take-ownership', 'yes', makeBool)
        self.existing_choice = getOption(options, 'existing',
                                  choices=['count', 'skip', 'ignore',
                                           'replace', 'refresh'])
        self.save_every = getOption(options, 'save-every', '0', NoneOrInt)
        # Achtung! Die folgenden debug-Optionen können set_trace auslösen:
        self.debug_countdown = getOption(options, 'debug-countdown', '0', makeBool)
        self.debug_filenames = getOption(options, 'debug-filenames', '', makeListOfStrings)
        transmogrifier.add_info('import_context',
                 name,
                 info)

        # toxml-Argument des Standard-Exportformulars:
        self.xmlformat = getOption(options, 'xml-format', 'no', makeBool)
        # weitere Optionen aus BaseSection._set_debugging_options

    def walk(self, topdown=True):
        """
        Angelehnt an os.walk(): Generiere Verzeichnis- und Dateilisten
        """
        join = posix_join
        import_context = self.import_context
        isdir = import_context.isDirectory
        listdir = import_context.listDirectory

        def _walk(top):
            names = listdir(top)
            dirs, nondirs = [], []
            for name in names:
                if isdir(join(top, name)):
                    dirs.append(name)
                else:
                    nondirs.append(name)

            if topdown:
                yield top, dirs, nondirs

            for name in dirs:
                new_path = join(top, name)
                for tup in _walk(new_path):
                    yield tup

            if not topdown:
                yield top, dirs, nondirs

        for tup in _walk(''):
            yield tup

    def __iter__(self):
        """
        importiere alle importierbaren Objekte

        Importierbar sind Zope-Exporte (.xml oder .zexp);
        etwa fehlende Container werden erzeugt.
        """
        count = self.count
        for item in self.previous:
            count('got')
            count('forwarded')
            yield item

        pathkey = self.pathkey
        context = self.context
        import_context = self.import_context
        verify = self.verify
        take_ownership = self.take_ownership
        existing_choice = self.existing_choice
        logprefix = '[%s]:' % self.name
        prevdir = None

        # set_trace()
        make_tempname = make_readableNameFactory(self.import_context,
                                                 self.passthrough,
                                                 self.single_tmpfile)

        existingdir = make_dirProxy(context)
        tmpnames = set()
        oldbase = None
        COUNTDOWN = self.debug_countdown
        failed_imports = 0
        save_every = self.save_every or None
        if save_every:
            import transaction
        minicount = 0
        debug_filenames = self.debug_filenames
        try:
            for dirname, dirs, files in self.walk():
                # erzeugt ggf. implizit ein Folder-Objekt:
                thisdir = existingdir[dirname]
                oids_before = set(thisdir.objectIds())
                for name in files:
                    base, ext = splitext(name)
                    if name in debug_filenames:
                        set_trace()
                    if ext in ('.zexp', '.xml'):
                                  # ['count', 'ignore', 'skip', 'replace', 'refresh'])
                        if existing_choice in ('skip', 'count'):
                            exists = base in thisdir.objectIds()
                            if exists:
                                logger.info('%(base)r exists in %(thisdir)s', locals())
                                if existing_choice == 'skip':
                                    count('skipped-existing')
                                    count('untyped')
                                    yield {'_path': posix_join(dirname, base),
                                           '_type': None,  # TODO
                                           }
                                    continue
                                else:
                                    tryit = COUNTDOWN > 0
                                    if tryit:
                                        COUNTDOWN -= 1
                                        pprint({'existing_choice': existing_choice,
                                                'dirname': dirname,
                                                'base': base,
                                                })
                                        set_trace()
                                        tryit = False

                        tmpname = make_tempname(posix_join(dirname, name))
                        tmpnames.add(tmpname)
                        try:
                            thisdir._importObjectFromFile(tmpname, verify,
                                                          take_ownership)
                        except BadRequestException as e:
                            logger.error('Error importing %(tmpname)s', locals())
                            logger.exception(e)
                            if existing_choice == 'count':
                                count('failed-imports')
                                failed_imports += 1
                            else:
                                raise
                        else:
                            count('imported')
                            if save_every is not None:
                                minicount = (minicount + 1) % save_every
                                if minicount == 0:
                                    count('savepoint-commits')
                                    transaction.savepoint(optimistic=True)

                            oids_after = set(thisdir.objectIds())
                            oids_added = oids_after - oids_before
                            if base in oids_added:
                                logger.info('Ok: %(base)r added', locals())
                                o = thisdir._getOb(base)
                                count('as-expected')
                            else:
                                logger.error('Expected %(base)r, added %(oids_added)r', locals())
                                if len(oids_added) == 1:
                                    count('renamed')
                                    imported = tuple(oids_added)
                                    logger.info('Counting as "renamed"')
                                    base = imported[0]
                                    o = thisdir._getOb(base)
                                else:
                                    if oids_added:
                                        logger.info('Counting as "unidentified"')
                                        count('unidentified')
                                    else:
                                        count('errors')
                                        logger.info('Counting as "errors"')
                                    o = None

                            if o is not None:
                                count('created')
                                count('untyped')
                                yield {'_path': posix_join(dirname, base),
                                       '_type': None,  # TODO
                                       }
        finally:
            if failed_imports:
                self.context.getAdapter('message')(
                    '${failed_imports} import[s] failed',
                    'warning',
                    mapping=locals())
            if not self.passthrough:
                for tmpname in tmpnames:
                    unlink(tmpname)


class MakeGroups(BaseSection):
    """
    Autoren- und Lesergruppen erzeugen
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        # set_trace()
        # BaseSection.__init__(self, transmogrifier, name, options, previous)

        if 'path-key' in options:
            pathkeys = options['path-key'].splitlines()
        else:
            pathkeys = defaultKeys(options['blueprint'], name, 'path')
        self.pathkey = Matcher(*pathkeys)

        self.whitelist = getOption(options, 'path',
                                   ['akademie/vortraege/*',
                                    'knowhow/fachbuecher/*',
                                    ],
                                   factory=makeListOfStrings)
        self.pathmatcher = make_pathFilter(self.whitelist,
                                           skip_leading=('unitracc',
                                                         'gkz',
                                                         ))

        self.addmembers = getOption(options, 'add-members',
                                    factory=makeListOfStrings)
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):
        count = self.count
        matches = self.pathmatcher
        itemInfo = make_itemInfo(self.name)
        newmembers = self.addmembers
        context = self.context
        groups = context.getBrowser('groups')
        # set_trace()
        for item in self.previous:
            count('got')

            pathkey = self.pathkey(*item.keys())[0]
            path = item[pathkey]

            # obj = traverse(self.context, str(path).lstrip('/'), None)
            obj = self.context.unrestrictedTraverse(path, None)
            if obj is None:  # path doesn't exist
                count('forwarded')
                # itemInfo(item, trace=trace1st)
                yield item
                continue

            if not matches(path):
                count('mismatch')
                count('forwarded')
                yield item
                continue

            uid = getattr(obj, '_at_uid', None)
            if uid is None:
                count('error-no-uid')
                count('forwarded')
                yield item
                continue

            for suffix in STRUCTURE_GROUP_SUFFIXES:
                gid = generic_group_id(uid, suffix)
                group = groups.getById(gid)
                if not group:
                    group = groups.add(gid, obj.Title() + ' ' + suffix)
                    count('groups-created')
                else:
                    count('groups-found')
                # set_trace()
                obj.manage_setLocalRoles(gid, [suffix])
                for mid in newmembers:
                    group.addMember(mid)

            count('forwarded')
            yield item
