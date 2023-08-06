# -*- coding: utf-8 -*- äöü  vim: tw=79
from dayta.browser.public import BrowserView, implements, Interface

# Vorgabewert fuer Startseite (als UID)
DEFAULT_PAGE_UID = 'f1bce398a8269e3b5f468373596e9a0c'

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport()
from visaplan.tools.debug import log_or_trace, pp
lot_kwargs = {'logger': logger,
              'debug_level': debug_active,
              }

# Dieser Browser:
from .crumbs import register_crumbs
from .data import NOSEARCH_IDS, NOSEARCH_PREFIXES


class IMainpage(Interface):

    def get_mainpage(self):
        """Liefert Sprach und Subportal abhaengig die korrekte Seite zurueck"""

    def get_banner_context(self):
        """ """

    def configured_page_uid(self, dic=None):
        """
        Gib die konfigurierte Startseiten-UID oder den Vorgabewert zurück
        """

    def show_search_login(self):
        """
        Soll das Suchformular ausgegeben werden?

        Historisch:
        "Soll die Suche und das Login gezeigt werden?"
        Das war aber Unsinn - beide haben nichts miteinander zu tun.
        Das Login-Formular wird ausgegeben, wenn der aktuelle Benutzer nicht
        angemeldet ist.
        """


class Browser(BrowserView):

    implements(IMainpage)

    config_storage_key = 'config_mainpage'

    def get_banner_context(self):

        context = self.context
        request = context.REQUEST

        if request.has_key('VIRTUAL_URL_PARTS') and request['VIRTUAL_URL_PARTS'][1]:
            """
            Virtual_URL_PARTS = (server-url, parameter OR '')
            nicht auf der Startseite; keinen Context zurueckgeben
            """
            return None

        if context.portal_type == 'Plone Site':
            return self.get_mainpage()
        return context

    @log_or_trace(**lot_kwargs)
    def get_mainpage(self):
        """
        Wenn eine folder_uid konfiguriert ist ("Main page folder uid"), gib das
        erste Dokument zurück, das unter diesem Ordner gefunden wird.

        Andernfalls gib die Seite mit der UID <page_uid> zurück ("Fallback
        default page uid", Standardwert: 'f1bce398a8269e3b5f468373596e9a0c').
        """

        context = self.context

        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()
        dict_ = self._get_config()

        folder_uid = dict_.get('folder_uid')
        if folder_uid:
            uid2path = context.getAdapter('uid2path')
            query = {}
            query['portal_type'] = 'Document'
            query['sort_on'] = 'getObjPositionInParent'
            query['path'] = {'query': uid2path(dict_.get('folder_uid')),
                             'depth': 1}
            pp(query=query)

            # Nur Suchen, wenn folder_uid konfiguriert:
            brains = pc(query)

            #Es darf hier zwingend nur ein Element zurueckkommen. Es gibt nur eine Startseite.
            #Wird gar nix gefunden. Deutsche Startseite als fallback.
            if brains:
                o = brains[0].getObject()
                try:
                    o_uid = o.UID()
                    return o
                except Exception, e:
                    print '!!!', e

        page_uid = self.configured_page_uid(dict_)
        return rc.lookupObject(page_uid)

    def configured_page_uid(self, dic=None):
        """
        Gib die konfigurierte Startseiten-UID oder den Vorgabewert zurück
        """
        if dic is None:
            dic = self._get_config()
        return dic.get('page_uid', DEFAULT_PAGE_UID) or DEFAULT_PAGE_UID

    @log_or_trace(**lot_kwargs)
    def _get_config(self):

        context = self.context
        settings = context.getBrowser('settings')
        return settings.get(self.config_storage_key, {})

    @log_or_trace(**lot_kwargs)
    def show_search_login(self):
        """
        Soll das Suchformular ausgegeben werden?

        Historisch:
        "Soll die Suche und das Login gezeigt werden?"
        Das war aber Unsinn - beide haben nichts miteinander zu tun.
        Das Login-Formular wird ausgegeben, wenn der aktuelle Benutzer nicht
        angemeldet ist.
        """
        context = self.context
        template = context.getAdapter('templateid')()
        logger.info('show_search_login: template=%(template)r', locals())

        if template is None:
            return True

        if template in NOSEARCH_IDS:
            logger.info('show_search_login: NOSEARCH id match %(template)r',
                        locals())
            return False

        match = template.startswith
        for prefix in NOSEARCH_PREFIXES:
            if match(prefix):
                logger.info('show_search_login: NOSEARCH prefix match'
                            ' (%(template)r.startswith %(prefix)r)',
                            locals())
                return False

        return True
