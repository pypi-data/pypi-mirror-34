# -*- coding: utf-8 -*- äöü
## integriert in --> @@subportal!
from dayta.browser.public import BrowserView, implements, Interface


class ILogo(Interface):

    def getLogo(self):
        """ """


class Browser(BrowserView):

    implements(ILogo)

    def getLogo(self):
        """
        Gib den Namen der zu verwendenden Logo-Graphik zurück,
        in Abhängigkeit von
        - @@subportal.get_current_info()['logo']
        - Top-Level-Domäne
        """
        context = self.context
        # langCode = context.getAdapter('langcode')()
        subportal = context.getBrowser('subportal')

        dict_ = subportal.get_current_info()

        if dict_.get('logo'):
            return dict_['logo']

        portal = context.getAdapter('portal')()
        domain_ending = portal.absolute_url().split('.')[-1]
        if (domain_ending != 'com'
            and not portal.restrictedTraverse('logo-' + domain_ending + '.jpg', None)
            ):
            domain_ending = 'com'

        return 'logo-' + domain_ending + '.jpg'
