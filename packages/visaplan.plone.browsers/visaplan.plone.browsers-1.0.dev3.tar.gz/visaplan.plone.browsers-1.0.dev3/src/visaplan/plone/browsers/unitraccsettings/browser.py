# -*- coding: utf-8 -*-
"""
@@unitraccsettings - Reimplementierung von tomcom.settings

Verwendet denselben pickle-Storage wie tomcom.settings (im Sinne von
*identisch*, d.h. dasselbe Verzeichnis und dieselben Dateien);
Änderungen:
- UI
  - Unterstützung bekannter Settings
- Dokumentation
"""

# Plone/Zope/Dayta:
from tomcom.browser.public import BrowserView, implements, Interface

from App.config import getConfiguration
from ZODB import utils

# Standardmodule:
from os import sep, makedirs
from os.path import exists, isdir
import cPickle as pickle

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _
from ...tools.forms import back_to_referer

# Dieser Browser:
from .utils import make_formfields, make_path_maker
from .data import BASE, DEFAULT, CONFIGPAGE
from .crumbs import register_crumbs

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport()
from visaplan.tools.debug import log_or_trace, pp


# --------------------------------------------------- [ Daten ... [
BASE_PATH = getConfiguration().product_config.get('settings', {})['settings_dir']
MAKEDIRS_MODE = 0770
# --------------------------------------------------- ] ... Daten ]

# ----------------------------------------- [ Hilfsfunktionen ... [
# Methode _base_path ersetzen, _get_full_path beschleunigen:
get_full_paths = make_path_maker(BASE_PATH)
# ----------------------------------------- ] ... Hilfsfunktionen ]



class IUnitraccSettings(Interface):

    def _base_path(self):
        """ """

    def set(self):
        """
        Setze den Wert für den Schlüssel "key"
        (Schlüsselwert und Inhalt aus den Formulardaten)
        """

    def reset(self):
        """
        Setze den Wert für den Schlüssel "key"
        (Schlüsselwert aus den Formulardaten, Inhalt aus den Defaults)
        """

    def get(self, key, default=None):
        """
        Gib den gespeicherten Wert für den Schlüssel <key> zurück
        (oder <default>, wenn noch nichts gespeichert)
        """

    def get_known_pages(self):
        """
        Gib die Namen der bekannten Schlüssel sowie (falls vorhanden)
        die spezialisierten Konfigurationsseiten zurück
        """

    def formdata(self, data=None):
        """
        Erzeuge aus <data> eine Liste von Dictionarys, aus denen Formularfelder gebaut werden können
        """


class Browser(BrowserView):

    implements(IUnitraccSettings)

    def _base_path(self):
        # obsolet; siehe get_full_paths
        return getConfiguration().product_config.get('settings', {})['settings_dir']

    def _get_full_path(self, suffix):
        """
        Gib den Dateinamen zurück und erzeuge ggf. das Verzeichnis
        """
        context = self.context
        oid = context._p_oid
        dirname, filename = get_full_paths(oid, suffix)
        if not isdir(dirname):
            makedirs(dirname, MAKEDIRS_MODE)
        return filename

    def get_known_pages(self):
        """
        Gib die Namen der bekannten Schlüssel sowie (falls vorhanden)
        die spezialisierten Konfigurationsseiten zurück
        """
        return [{'key': dic['key'],
                 'configpage': dic.get('configpage'),
                 }
                for dic in BASE
                ]

    def set(self):
        """
        Setze den Wert für den Schlüssel "key"
        (Schlüsselwert und Inhalt aus den Formulardaten)
        """
        context = self.context

        context.getBrowser('tpcheck').auth_settings_set()

        request = context.REQUEST
        form = request.form
        key = form.get('key', '')
        portal = context.getAdapter('portal')
        message = context.getAdapter('message')

        if not form.get('key'):
            message('No key given.')
            return back_to_referer(request)

        self._set(key, dict(form))

        message('Changes saved.')
        return back_to_referer(request, key=key)

    def reset(self):
        """
        Setze den Wert für den Schlüssel "key"
        (Schlüsselwert aus den Formulardaten, Inhalt aus den Defaults)
        """
        context = self.context

        context.getBrowser('tpcheck').auth_settings_set()

        request = context.REQUEST
        form = request.form
        key = form.get('key', '')
        portal = context.getAdapter('portal')
        message = context.getAdapter('message')

        if not form.get('key'):
            message('No key given.')
            return back_to_referer(request)

        if self.get(key) and not form.get('force-reset'):
            message("Won't override the existing values for key ${key}",
                    'error',
                    mapping=locals())
            return back_to_referer(request, key=key)

        values = DEFAULT.get(key)
        if values is None:
            message('Sorry, no defaults for key ${key}',
                    'error',
                    mapping=locals())
            return back_to_referer(request, key=key)
        self._set(key, values)

        message('Changes saved.')
        return back_to_referer(request, key=key)

    def _set(self, key, data):
        """
        Setze den Wert für den Schlüssel <key> auf <data>
        """
        path = self._get_full_path(key)
        with open(path, 'wb') as fo:
            logger.info('Schreibe %(key)r nach %(path)s', locals())
            fo.write(pickle.dumps(data))

    def get(self, key, default=None):
        """
        Gib den gespeicherten Wert für den Schlüssel <key> zurück
        (oder <default>, wenn noch nichts gespeichert)
        """

        path = self._get_full_path(key)
        if not exists(path):
            return default
        return pickle.loads(open(path, 'rb').read())

    @log_or_trace(debug_active)
    def _getInherited(self, key,
                      factory,
                      factory_portal=None,
                      default=None,
                      from_portal=True):
        """
        Gib einen potentiell geerbten Wert zurück

        key -- der Schlüssel, z. B. "localsearch"
        factory -- eine Funktion, die den zurückzugebenden Wert erzeugt,
                   mit den Argumenten:
                   data -- die gefundenen Daten
                   brain -- das Katalogobjekt des Objekts, zu dem die
                            gefundenen Daten gehören
                   distance -- die Anzahl der Schritte bis zu dem
                               Objekt, bei dem wir fündig geworden sind
                   uid -- die UID des Objekts (nicht verfügbar für Portal)
        factory_portal -- wie factory, aber zum Aufruf für das Portal,
                          und daher mit einem Argument o (für das
                          Portalobjekt) anstelle von brain (und aller
                          anderen)

        from_portal -- werden die Werte dieses Schlüssels zentral "im
                       Portal" gespeichert?
        """
        assert from_portal is True, (
                '_getInherited(...): andere als "im Portal" gespeicherte '
                'Settings noch nicht unterstützt'
                )
        context = self.context
        pt = context.portal_type
        # Das Portal hat keine UID, und deshalb gibt es dafür auch keine
        # Daten:
        if pt == 'Plone Site':
            if factory_portal is None:
                return default
            return factory_portal(context)

        getAdapter = context.getAdapter
        # Gibt eine Liste von Brains zurück:
        aqparents = getAdapter('aqparents')()

        portal = getAdapter('portal')()
        settings = portal.getBrowser('settings')
        data = settings.get(key, {})

        for distance, brain in enumerate(aqparents):
            uid = brain.UID
            if data.has_key(uid):
                return factory(brain=brain,
                               uid=uid,
                               data=data[uid],
                               distance=distance)
        return default

    def formdata(self, key=None):
        """
        Erzeuge aus <data> eine Liste von Dictionarys,
        aus denen Formularfelder gebaut werden können
        """
        context = self.context
        form = context.REQUEST.form
        form_key = form.get('key')
        if key is None:
            assert form_key
            key = form_key
        elif key:
            if form_key:
                assert key == form_key
        elif form_key:
            key = form_key
        else:
            return []
        # _ = message = context.getAdapter('message')

        res = {'messages': [],
               'savetext': None
               }
        meta = {'defaults_loaded': False
                }
        messages = res['messages']

        readonly = None
        configpage = CONFIGPAGE.get(key)
        if configpage is not None:
            if configpage['isglobal']:
                html = context.restrictedTraverse('settings_snippet_global_config_hint'
                                                  )(**configpage)
            else:
                html = context.restrictedTraverse('settings_snippet_context_config_hint'
                                                  )(**configpage)
            messages.append({'class': 'info',
                             'html': html,
                             })
            readonly = True
        data = self.get(key) # todo: Defaultwert je nach (bekanntem) key
        meta['has_data'] = data is not None
        defaults = DEFAULT.get(key)
        meta['has_defaults'] = defaults is not None
        if data is not None:
            res['savetext'] = 'Change'
        else:
            messages.append({'class': 'warning',
                             'text': _('No data yet for key "%(key)s"'
                                       ) % locals(),
                             })
            data = defaults
            if data is not None:
                meta['defaults_loaded'] = True
                messages.append({'class': 'info',
                                 'text': _('Loaded the default values into the form; '
                                           'you will likely want to change them.'),
                                 })
                res['savetext'] = 'Save'
            else:
                messages.append({'class': 'error',
                                 'text': _('Sorry, there is no support yet for adding '
                                           'data without default values!'),
                                 })

        if data is not None and 'key' in data:
            del data['key']
        liz = make_formfields(data)
        for row in liz:
            if row.get('type') == 'pformat':
                if not readonly:
                    messages.append({'class': 'error',
                                     'text': _('Unsupported datatypes'),
                                     })
                    readonly = True
                break
        if not readonly:
            liz.insert(0, {'name': 'key',
                           'value': key,
                           'type': 'hidden',
                           })
        meta['readonly'] = readonly or False
        res['formfields'] = liz and [
                             {'type': 'fieldset',
                              'label': key,
                              'children': liz,
                              }]
        res['meta'] = meta
        return res
