# -*- coding: utf-8 -*-
"""
@@languageredirector:
Weiterleitung zum zur Sprache passenden (virtuellen) Host

TODO:
- hartcodierte Zuordnungen konfigurierbar machen
  - am besten je Subportal
- direkt Plone-Tools verwenden
- Adapter "protocol" ist unnötig
"""
from dayta.browser.public import BrowserView, implements, Interface


class ILanguageRedirector(Interface):

    """
    Browser wird durch Kontext aufgerufen
    """


class Browser(BrowserView):

    implements(ILanguageRedirector)

    def __call__(self):
        """ """
        context = self.context
        getAdapter = context.getAdapter
        portalUrl = getAdapter('portal')().absolute_url()
        langCode = getAdapter('langcode')()
        redirect = context.REQUEST.RESPONSE.redirect
        protocol = getAdapter('protocol')()

        if langCode == 'de':
            if portalUrl.find('unitracc.de') == -1:
                return redirect(protocol + 'unitracc.de')
            return

        if langCode == 'en':
            if portalUrl.find('unitracc.com') == -1:
                return redirect(protocol + 'unitracc.com')
            return

        if langCode == 'es':
            if portalUrl.find('unitracc.es') == -1:
                return redirect(protocol + 'unitracc.es')
            return
