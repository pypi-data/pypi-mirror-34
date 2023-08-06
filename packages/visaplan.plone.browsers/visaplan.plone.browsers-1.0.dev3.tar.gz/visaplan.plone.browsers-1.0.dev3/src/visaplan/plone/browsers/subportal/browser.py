# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et
"""
unitracc@@subportal: Subportal-Funktionalität und -verwaltung

siehe TODO.txt
"""
from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
import os
from hashlib import md5
from os import sep
from os.path import getmtime, getctime, getsize
from urlparse import urlparse
from DateTime import DateTime
from thread import get_ident as get_thread_ident

from plone.memoize import ram
from Products.CMFCore.utils import getToolByName

# Unitracc:
from ...permissions import Manage_Subportals, Get_Subportal_Info

# Unitracc-Tools:
from visaplan.tools.http import extract_hostname
from visaplan.tools.sequences import nonempty_lines

# Andere Browser:
from ..unitraccfeature.utils import (DESKTOP_UID, REGISTRATION_UID, HELP_UID,
        ABOUT_UID, CONTACT_UID, MEMBERSFOLDER_UID,
        NEWSFOLDER_UID, ARTICLESFOLDER_UID, EVENTSFOLDER_UID,
        TEMP_UID,  # Ansteuerung über UID evtl. abschaffen
        )

# Dieser Browser:
from .utils import (detect_project, img_link_dict,
        lang_from_hostname, make_prefixer, create_subportalId,
        )
from .crumbs import register_crumbs

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import log_or_trace, pp
logger, debug_active, DEBUG = getLogSupport(defaultFromDevMode=False)
lot_kwargs = {'debug_level': debug_active,
              'logger': logger,
              # verbose=True (Vorgabe) impliziert log_args und log_result:
              'verbose': False,
              'log_result': True,
              }
lot_keyfuncs_kwargs = dict(lot_kwargs)
if debug_active:
    lot_keyfuncs_kwargs['debug_level'] = (debug_active and
            # hier ggf. Logging für Cache-Key-Funktionen (de)aktivieren:
            0)

# ------------------------------------------------------ [ Daten ... [
GA_CODE = """
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', '%s', 'auto');
ga('send', 'pageview');
</script>
"""

NON_KEYS = ('default_uid',
            )
SAVE_CNT = 0

# Für Subportal-Ermittlung nur Hostnamen heranziehen, kein Protokoll und/oder Port.
# Da wir derzeit keinen Grund haben, es anders zu machen, und die bisherige Methode
# bei Fällen wie http://aqwa-academy.net:/Pfad/zur/Datei versagt
# (überflüssiger Doppelpunkt, mutmaßlich aus RewriteRule),
# ist das nunmehr die einzige implementierte Methode.
HOSTNAMES_ONLY = True
# ------------------------------------------------------ ] ... Daten ]


# ------------------------------------------- [ Cache-Funktionen ... [
@log_or_trace(**lot_keyfuncs_kwargs)
def simple_key(method, self):
    """
    Key-Funktion für Subportal-übergreifende Lesefunktionen
    """
    res = (method,
           SAVE_CNT,
           get_thread_ident(),
           )
    return res

@log_or_trace(**lot_keyfuncs_kwargs)
def url2uid_key(method, self):
    """
    Key-Funktion für Auflösung des Kontexts zur UID eines Subportals
    """
    res = (method,
           urlparse(self.context.absolute_url()).netloc,
           SAVE_CNT,
           get_thread_ident(),
           )
    return res

@log_or_trace(**lot_keyfuncs_kwargs)
def urlandlang_key(method, self, lang):
    """
    Berücksichtigt den Kontext und die Anzeigesprache
    """
    res = (method,
           urlparse(self.context.absolute_url()).netloc,
           lang,
           SAVE_CNT,
           get_thread_ident(),
           )
    return res

@log_or_trace(**lot_keyfuncs_kwargs)
def uid_key(method, self, uid):
    """
    Key-Funktion für Auflösung einer UID zu bestimmten Eigenschaften
    des angesprochenen Subportals
    """
    res = (method,
           uid,
           SAVE_CNT,
           get_thread_ident(),
           )
    return res
# ------------------------------------------- ] ... Cache-Funktionen ]


# -------------------------------------------------- [ Interface ... [
class ISubPortal(Interface):

    def set():
        """ """

    def get():
        """
        Gib die kompletten Informationen zurück;
        nützlicher für Seitentemplates etc.: --> get_current_info
        """

    def add():
        """ """

    def delete():
        """
        löscht das übergebene Subportal (ohne Vorwarnung!)
        """

    def css():
        """ """

    def js():
        """ """

    def is_uid_active(uid):
        """ """

    def get_voc_subportals():
        """ """

    def get_default_page():
        """ """

    def get_translations():
        """ """

    def get_image_right_info():
        """ """

    def get_analytics():
        """ """

    def get_team_email():
        """
        Gib die E-Mail-Adresse des Teams für das aktuelle Subportal zurück
        """

    def get_booking_email():
        """
        Gib die E-Mail-Adresse des Buchungs-Teams für das aktuelle Subportal zurück
        """

    def get_paypal_id():
        """
        Gib die E-Mail-Adresse des PayPal-Kontos für das aktuelle Subportal zurück
        """

    def get_from_address(key):
        """
        Gib die gewünschte Absenderadresse für das aktuelle Subportal zurück.

        Die konfigurierten Adressen werden nur verwendet, wenn die Instanz auf
        dem produktiven Server läuft; ansonsten wird der Projektname als
        virtueller Benutzername verwendet.
        """

    def registration_url():
        """
        Gib die URL für die Registrierungsseite zurück
        """

    def uids_dict():
        """
        Gib alle UIDs zurück, die sich ggf. je nach Projekt unterscheiden
        """

    def urls_dict():
        """
        Gib alle URLs zurück, die (ggf. je nach Projekt unterschiedliche) UIDs
        verwenden
        """

    def getLogo():
        """
        Gib den Namen der zu verwendenden Logo-Graphik zurück,
        in Abhängigkeit von
        - get_current_info()['logo']
        - Top-Level-Domäne
        """

    def get_logo_settings():
        """
        Gib ein Dict mit den Informationen zum linken und rechten Logo zurück
        """
# -------------------------------------------------- ] ... Interface ]


class Browser(BrowserView):

    implements(ISubPortal)

    storageKey = 'subportal'

    @log_or_trace(trace=0, **lot_kwargs)
    def set(self):
        """
        Speichere die Änderungen (aller Subportale auf einmal)
        """
        global SAVE_CNT
        context = self.context
        getAdapter = context.getAdapter
        request = context.REQUEST

        OK = False
        getAdapter('authorized')(Manage_Subportals)
        try:
            form = request.form
            # pp(form=dict(form))
            portal = getAdapter('portal')()
            settings = portal.getBrowser('unitraccsettings')
            settings._set(self.storageKey, form)
            OK = True

            message = getAdapter('message')
            message('Changes saved.')
        finally:
            if OK:
                SAVE_CNT += 1
            return request.RESPONSE.redirect(request['HTTP_REFERER'])

    @ram.cache(url2uid_key)
    def get(self):

        context = self.context
        context.getAdapter('authorized')(Get_Subportal_Info)
        dic = self._get()
        dk = 'default_uid'
        dv = dic.get(dk)
        if not dv:
            liz = dic.keys()
            dic['no_default_warning'] = True
            if dk in liz:
                liz.remove(dk)
            if len(liz) == 1:
                dic[dk] = liz[0]
        return dic

    @ram.cache(simple_key)
    @log_or_trace(trace=0, **lot_kwargs)
    def _get(self):
        """
        Gib die kompletten Subportaldefinitionen zurück
        """

        context = self.context
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('unitraccsettings')
        return settings.get(self.storageKey, {})

    @ram.cache(simple_key)
    @log_or_trace(trace=0, **lot_kwargs)
    def _get_url_to_uid(self):
        """
        Gib ein dict zurück, das die Hostnamen (HOSTNAMES_ONLY) oder Root-URLs
        (alte Methode) den UIDs der Subportale zuordnet
        """
        dict_ = {}
        data = self._get()
        if HOSTNAMES_ONLY:
            for k in self.keys():
                v = data[k]
                for url in nonempty_lines(v.get('domains', '')):
                    dict_[extract_hostname(url)] = k
        else:  # alte Methode:
            for k in self.keys():
                v = data[k]
                for url in v.get('domains', '').splitlines():
                    dict_[url.strip()] = k
        return dict_

    @ram.cache(simple_key)
    def _default_uid(self):
        """ """
        return self._get().get('default_uid', '')

    @log_or_trace(trace=0, **lot_kwargs)
    def get_current_id(self):
        """
        Gib die UID des aktuellen Subportals zurück
        """

        context = self.context
        dict_ = self._get_url_to_uid()

        if HOSTNAMES_ONLY:
            try:
                uid = dict_.get(extract_hostname(context.absolute_url()))
            except IndexError:
                # z. B. bei Aufruf durch externe Methoden:
                logger.error('Kann keinen Hostnamen extrahieren! %(context)r', locals())
                try:
                    u = context.absolute_url()
                except Exception:
                    pass
                else:
                    logger.info('(absolute_url: %(u)s)', locals())
                finally:
                    uid = None

        else:
            portal = context.getAdapter('portal')()
            uid = dict_.get(portal.absolute_url())
        if not uid:
            uid = self._default_uid()
        return uid

    def _get_current_id(self, hostname):
        """
        Gib die UID des aktuellen Subportals zurück

        (wie --> get_current_id, aber mit übergebenem Hostnamen)
        """
        dict_ = self._get_url_to_uid()
        uid = dict_.get(hostname)
        if uid is not None:
            return uid
        return self._default_uid()

    @log_or_trace(trace=0, **lot_kwargs)
    def get_current_info(self):
        """
        Gib die Konfiguration (ein dict) für das aktuelle Subportal zurück
        """
        uid = self.get_current_id()
        dict_ = self._get()
        return dict_.get(uid, {})

    def _get_current_info(self, uid):
        """
        Gib die Konfiguration (ein dict) für das aktuelle Subportal zurück

        (wie --> get_current_info, aber mit übergebener Subportal-UID)
        """
        dict_ = self._get()
        return dict_.get(uid, {})

    def add(self):
        """
        Füge ein Subportal hinzu
        """
        global SAVE_CNT
        context = self.context
        getAdapter = context.getAdapter
        request = context.REQUEST

        getAdapter('authorized')(Manage_Subportals)

        portal = getAdapter('portal')()
        message = getAdapter('message')
        settings = portal.getBrowser('unitraccsettings')
        dict_ = settings.get(self.storageKey, {})

        m = md5()
        m.update(str(DateTime()) + '-' + portal.getId())
        uid = m.hexdigest()

        title = request.get('title', '').strip()
        spid = create_subportalId(uid, title)
        if spid in dict_:
            message('Subportal ${spid} does already exist!',
                    'warning',
                    mapping=locals())
            spid = uid
        dict_[spid] = {'title': title}

        settings._set(self.storageKey, dict_)

        message('New subportal ${spid} created.',
                mapping=locals())
        SAVE_CNT += 1

        return request.RESPONSE.redirect(request['HTTP_REFERER'])

    def delete(self):
        """
        löscht das übergebene Subportal (ohne Vorwarnung!)
        """
        global SAVE_CNT
        context = self.context
        getAdapter = context.getAdapter
        request = context.REQUEST

        getAdapter('authorized')(Manage_Subportals)

        portal = getAdapter('portal')()
        message = getAdapter('message')
        settings = portal.getBrowser('unitraccsettings')
        dict_ = settings.get(self.storageKey, {})
        try:
            default_uid = dict_['default_uid']
        except KeyError:
            default_uid = None
        if not default_uid:
            message('Please select a default subportal!',
                    'error')

        else:
            message('default subportal is %s' % default_uid)
            form = request.form
            try:
                uid = form['uid']
                try:
                    title = dict_[uid]['title']
                    if uid == default_uid:
                        message("Won't delete default subportal %s (%s)!"
                                % (uid,
                                   title or 'untitled'
                                   ),
                                'error')
                    else:
                        del dict_[uid]
                        settings._set(self.storageKey, dict_)
                        message('Subportal %r (%s) deleted.'
                                % (uid,
                                   title or 'untitled',
                                   ))
                        SAVE_CNT += 1
                except KeyError:
                    message('No subportal %r found'
                            % (uid,
                               ),
                            'error')
            except KeyError:
                message('No subportal id given', 'error')
        return request.RESPONSE.redirect(request['HTTP_REFERER'])

    def keys(self):
        """
        Gib eine sortierte Liste der Schlüssel (UIDs) zurück
        """
        return sorted([k
                       for k in self._get().keys()
                       if k not in NON_KEYS
                       ])

    def keys_and_titles(self, **kwargs):
        """
        Gib eine Sequenz von dicts zurück; Schlüssel: uid, title, active

        Wenn current_spid übergeben wird (die Bezeichung des aktuell aktiven Subportals),
        wird dieses "aktiv gesetzt"; ansonsten das erste in der Liste.
        """
        items = self._get()
        keys = sorted([k
                       for k in items.keys()
                       if k not in NON_KEYS
                       ])
        res = []
        unnamed = 0
        current_spid = kwargs.pop('current_spid', None)
        if current_spid:
            for key in keys:
                title = items[key].get('title', '').strip() or key
                dic = {'uid': key,
                       'title': title,
                       'active': key == current_spid,
                       }
                res.append(dic)
        else:
            for key in keys:
                title = items[key].get('title', '').strip() or key
                dic = {'uid': key,
                       'title': title,
                       'active': not res,
                       }
                res.append(dic)
        return res

    def get_voc_subportals(self):
        """ """
        context = self.context
        dict_ = self._get()
        uids = self.keys()

        return [(uid, dict_[uid]['title'])
                for uid in uids]

    @log_or_trace(trace=0, **lot_kwargs)
    def logo(self):
        """
        siehe --> getLogo()
        """

        dict_ = self.get_current_info()

        if dict_.get('logo'):
            return dict_['logo']

    @log_or_trace(**lot_kwargs)
    def css(self):

        dict_ = self.get_current_info()

        return [string_.strip()
                for string_ in dict_.get('css', '').splitlines()
                if string_.strip()]

    @log_or_trace(**lot_kwargs)
    def js(self):

        dict_ = self.get_current_info()

        return [string_.strip()
                for string_ in dict_.get('js', '').splitlines()
                if string_.strip()]

    @log_or_trace(**lot_kwargs)
    def title(self):

        dict_ = self.get_current_info()

        return dict_.get('portal_title', '')

    @ram.cache(uid_key)
    def is_uid_active(self, uid):

        context = self.context
        if uid in context.getSubPortals():
            return True

    def _set_for_context(self, uids):
        """ """
        context = self.context
        context.setSubPortals(uids)
        context.reindexObject(idxs=['get_sub_portal'])

    def initialize_default(self):

        logger.info('initialize_default ...')
        cnt_found = 0
        cnt_changed = 0
        cnt_unchanged = 0
        cnt_errors = 0
        context = self.context

        context.getAdapter('authorized')(Manage_Subportals)

        pickle = context.getBrowser('pickle')
        tmp_sp = self.keys()
        default_sp = self._default_uid()
        subportals = []
        if default_sp:
            subportals.append(default_sp)
        pc = context.getAdapter('pc')()

        try:
            for brain in pc(Language='all', sort_on='created'):
                cnt_found += 1
                try:
                    data = pickle._get_uncached(brain.UID + '_ps', {})
                    if not data.get('subPortals'):
                        object_ = None
                        try:
                            object_ = brain._unrestrictedGetObject()
                        except Exception, e:
                            #ghost brain
                            pc.uncatalog_object(brain.getPath())
                        if object_:
                            subportal = object_.getBrowser('subportal')
                            subportal._set_for_context(subportals)
                            object_.reindexObject(idxs=['get_sub_portal'])
                            cnt_changed += 1
                    else:
                        cnt_unchanged += 1
                except Exception, e:
                    if not cnt_errors:
                        # print dir(logger)
                        logger.error(str(e))
                        logger.debug(e)
                    cnt_errors += 1
                    if cnt_errors > 3:
                        raise
        finally:
            logger.info('initialize_default: beendet')
            logger.info('%5d Objekte gefunden' % cnt_found)
            logger.info('%5d Objekte geaendert' % cnt_changed)
            logger.info('%5d Objekte belassen' % cnt_unchanged)
            if cnt_errors:
                logger.error('%5d Fehler' % cnt_errors)
        return 'OK'

    def get_default_page(self):
        # TH: Was hat das mit Subportalen zu tun? §:-|

        context = self.context
        pc = context.getAdapter('pc')()

        query = {'portal_type': 'Document',
                 'getExcludeFromNav': False,
                 'sort_on': 'getObjPositionInParent',
                 'path': {'query': context.getPath(),
                          'depth': 1},
                 }

        brains = pc(query)
        if brains:
            return brains[0].getObject()

    def get_translations(self):

        context = self.context

        dict_ = self.get_current_info()

        new_list = []
        languages = {}
        for string_ in dict_.get('languages', '').splitlines():
            if len(string_.split(';')) == 2:
                lang_code, language_name = string_.split(';')
                languages[lang_code] = language_name

        for item in context.getBrowser('additionallanguages').languages():
            if languages.has_key(item['code']):
                item['name'] = languages[item['code']]
                new_list.append(item)
        return new_list

    def get_image_right_id(self):

        dict_ = self.get_current_info()
        return dict_.get('image_right_id', '')

    def get_image_right_info(self):
        """
        Verarbeite Zeilen nach dem Muster:

        de;bildname.jpg;url

        Wenn für die aktuelle Anzeigesprache kein Eintrag vorhanden ist,
        wird die englische Version verwendet.
        """

        context = self.context
        display_lang = context.getAdapter('langcode')()
        return self._giri(display_lang)

    @ram.cache(urlandlang_key)
    def _giri(self, display_lang):
        """
        Arbeitspferd für get_image_right_info
        """
        data = self.get_current_info()
        dict_en = {}
        lr = data.get('logoright', '')
        if not lr:
            return dict_en
        for string_ in lr.splitlines():
            if not string_:
                continue
            dic = img_link_dict(string_)
            lang = dic['lang_code']
            if lang == display_lang:
                return dic
            elif lang == 'en':
                dict_en = dic
        return dict_en

    @log_or_trace(trace=0, **lot_kwargs)
    def get_logo_settings(self):
        """
        Gib ein Dict mit den Informationen zum linken und rechten Logo zurück

        Das linke Logo ist das Logo des Portals (z. B. UNITRACC),
        ggf. in Varianten je nach TLD (.de oder .com; "host_lang");
        das rechte Logo enthält ein oder mehrere Partnerlogos,
        ebenfalls ggf. abhängig von der "Hostnamens-Sprache".
        Im Falle mehrerer Partnerlogos ist es üblicherweise sinnvoll, als "URL"
        eine Map-ID zu konfigurieren; diese <map> ist dann in top.pt zu
        notieren.

        Schlüssel:
          logo - Dateiname (ohne Pfad) für das linke Logo
        (aus img_link_dict, für das rechte Logo:)
          lang_code - der Sprachcode aus der logoright-Zeile
          image_id - Dateiname (ohne Pfad)
          url - Verweis-URL
          alt - Ersatztext
        (sowie, wenn "url" mit "map:" beginnt:
          usemap - #<Map-ID>
        Neue Schlüssel, vollständige Pfade:
          logoleft_full  (statt veraltend "logo")
          logoright_full (statt veraltend "image_id")

        Ersetzt get_image_right_info() und getLogo()
        """
        context = self.context
        # dict_ = self._get_url_to_uid()
        hostname = extract_hostname(context.absolute_url())
        host_lang = lang_from_hostname(hostname)
        uid = self._get_current_id(hostname)
        data = self._get_current_info(uid)
        prefixed = make_prefixer(data.get('imagebase'))
        logoleft_mask = data.get('logoleft_mask', 'logo-%(host_lang)s.jpg')
        # pp(locals())
        ls_dict = None  # logo settings dict
        dicts = []
        # Logo rechts: Eintrag mit passender Host-Sprache?
        for z in data.get('logoright', '').splitlines():
            dic = img_link_dict(z)
            if host_lang is None:
                dicts.append(dic)
                continue
            lang = dic['lang_code']
            if lang == host_lang:
                ls_dict = dic
                break
            else:
                dicts.append(dic)
        # pp(dicts=dicts)

        if ls_dict is None:
            # mindestens eine Zeile *muß* es geben!
            ls_dict = dicts[0]

        logoright = ls_dict.get('image_id')
        if logoright:
            ls_dict['logoright_full'] = prefixed(logoright)
        else:
            ls_dict['logoright_full'] = None
        ls_dict.update({'host_lang': host_lang,
                        'usemap': None,
                        })
        url = ls_dict['url']
        if url:
            if url.startswith('map:'):
                ls_dict['url'] = None
                mapid = url[4:] or None
                if mapid is not None:
                    ls_dict['usemap'] = '#'+mapid
        else:
            ls_dict['url'] = None
        # pp(ls_dict=ls_dict)

        # Logo links (UNITRACC.com oder .de):
        try:
            logoleft = data['logo']
        except KeyError:
            pass
        else:
            # z. B. bei Unitracc-SP nicht definiert:
            if logoleft:
                ls_dict['logo'] = logoleft
                ls_dict['logoleft_full'] = prefixed(logoleft)
                return ls_dict
        if host_lang is None:
            host_lang = 'de'
        ls_dict['logo'] = logoleft = logoleft_mask % locals()
        ls_dict['logoleft_full'] = prefixed(logoleft)

        return ls_dict

    def get_analytics(self):

        context = self.context
        dict_ = self.get_current_info()

        if dict_.get('gacode'):
            return GA_CODE % dict_['gacode']
        else:
            return context.getBrowser('analytics')()

    def get_team_email(self):
        """
        Gib die E-Mail-Adresse des Teams für das aktuelle Subportal zurück
        """
        return self._get_email('team_email')

    def _get_email(self, key, default='info@unitracc.de'):
        """
        Gib eine Mail-Adresse zurück, gedacht als Empfänger-Adresse
        (also auch auf Entwickler-Instanzen so auszugeben)
        """
        spinfo = self.get_current_info()
        address = spinfo.get('team_email', default)
        return address

    def get_booking_email(self):
        """
        Gib die E-Mail-Adresse des Buchungs-Teams für das aktuelle Subportal zurück
        """
        return self._get_email('booking_email')

    def get_paypal_id(self):
        """
        Gib die E-Mail-Adresse des Buchungs-Teams für das aktuelle Subportal zurück
        """
        return self._get_email('paypal_id')

    def get_root_urls(self):
        """
        Generiere die URLs, die für das aktuelle Subportal eingetragen sind.

        Die Feldbezeichnung "domains" ist etwas ungenau ...
        """
        for line in self.get_current_info().get('domains', '').splitlines():
            val = line.strip()
            if val:
                yield val

    def get_from_address(self, key='team_email'):
        """
        Gib die gewünschte Absenderadresse für das aktuelle Subportal zurück.

        Die konfigurierten Adressen werden nur verwendet, wenn die Instanz auf
        dem produktiven Server läuft;
        ansonsten, und wenn die Adresse zum angegebenen Schlüssel leer ist,
        wird der Projektname als virtueller Benutzername verwendet.
        """
        context = self.context
        feature = context.getBrowser('unitraccfeature').all()
        # Auf dem Live-Server können die konfigurierten Absenderadressen
        # verwendet werden - wir nehmen an, daß die entsprechenden
        # Nameserver-Einträge vorhanden sind:
        if feature['on_live_server']:
            spinfo = self.get_current_info()
            val = spinfo.get(key)
            if val:
                val = val.strip()
            if val:
                return val
        # nicht auf dem Live-Server, oder nicht gesetzt:
        # SMTP-Server glücklichmachen
        project = detect_project(self.get_root_urls(), feature)
        return '@'.join((project+'-'+key,
                         feature['os_hostname'],
                         ))

    def registration_url(self):
        """
        Gib die URL für die Registrierungsseite zurück
        """
        portal_url = getToolByName(self.context, 'portal_url')()
        return ''.join((portal_url,
                        '/resolvei18n/',
                        REGISTRATION_UID,
                        ))

    def uids_dict(self):
        """
        Gib alle UIDs zurück, die sich ggf. je nach Projekt unterscheiden

        TODO: Diese UIDs sollen wieder gleichgezogen werden,
              z. B. mit Hilfe eines Migrationsschritts!
              Maßgeblich ist die Urinstanz unitracc.de.
        """
        return {'registration':   REGISTRATION_UID,
                'about':          ABOUT_UID,
                'contact':        CONTACT_UID,
                'desktop':        DESKTOP_UID,
                'help':           HELP_UID,
                'newsfolder':     NEWSFOLDER_UID,
                'articlesfolder': ARTICLESFOLDER_UID,
                'eventsfolder':   EVENTSFOLDER_UID,
                }

    def urls_dict(self):
        """
        Gib alle URLs zurück, die (ggf. je nach Projekt unterschiedliche) UIDs
        verwenden
        """
        portal_url = getToolByName(self.context, 'portal_url')()
        prefix = portal_url + '/resolvei18n/'
        res = {}
        for key, val in self.uids_dict().items():
            if val is None:
                res[key] = val
            else:
                res[key] = prefix + val
        return res

    def getPortalID(self):
        """
        Gib den Text zurück, der in den @@registration-Mails als portal_id
        eingesetzt wird; Name der Methode angelehnt an @@registration.getPortalID.

        Der Text kann durchaus länger als eine "echte ID" sein, z. B.
        "Wissensnetzwerk Steine-Erden"
        """
        return self.title()

    def getSubtitle(self):
        """
        Zur Verwendung als Untertitel in Mail-Fußzeilen
        """
        dict_ = self.get_current_info()
        return dict_.get('portal_subtitle', '')

    @log_or_trace(trace=0, **lot_kwargs)
    def getLogo(self):
        """
        Gib den Namen der zu verwendenden Logo-Graphik zurück,
        in Abhängigkeit von
        - @@subportal.get_current_info()['logo']
        - Top-Level-Domäne
        """
        # langCode = context.getAdapter('langcode')()

        dict_ = self.get_current_info()

        if dict_.get('logo'):
            return dict_['logo']

        context = self.context
        portal = context.getAdapter('portal')()
        domain_ending = portal.absolute_url().split('.')[-1]
        if (False and
            domain_ending != 'com'
            and not portal.restrictedTraverse('logo-' + domain_ending + '.jpg', None)
            ):
            domain_ending = 'com'
        if domain_ending in ('test',
                             'local',
                             ):
            domain_ending = 'de'

        return 'logo-' + domain_ending + '.jpg'

# vim: ts=8 sts=4 sw=4 si et hls
