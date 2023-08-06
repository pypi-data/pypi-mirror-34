from dayta.browser.public import BrowserView, implements, Interface


class IManagementUser(Interface):

    pass


class Browser(BrowserView):

    implements(IManagementUser)
