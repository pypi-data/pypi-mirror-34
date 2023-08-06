from dayta.browser.public import BrowserView, implements, Interface


class IUserLanguage(Interface):

    def get(self):
        """ """


class Browser(BrowserView):

    implements(IUserLanguage)

    def get(self):
        """ """
        context = self.context
        return context.getAdapter('usedlanguages')()
