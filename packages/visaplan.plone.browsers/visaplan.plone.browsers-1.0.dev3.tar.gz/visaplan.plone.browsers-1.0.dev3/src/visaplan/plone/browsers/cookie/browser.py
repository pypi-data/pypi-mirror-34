from dayta.browser.public import BrowserView, implements, Interface


class ICookie(Interface):

    def set(self, key, value):
        """set cookie"""

    def get(self, key):
        """get cookie"""


class Browser(BrowserView):

    implements(ICookie)

    def get(self, key):
        """ """
        return self.context.REQUEST.cookies.get(key, '')

    def set(self, key, value):
        """ """
        REQUEST = self.context.REQUEST
        cookies = REQUEST.cookies.get(key, '')
        if REQUEST.cookies.has_key(key):
            del REQUEST.cookies[key]
        REQUEST.RESPONSE.setCookie(key, value, path='/')

    def delete(self, key):
        if self.context.REQUEST.cookies.has_key(key):
            del self.context.REQUEST.cookies[key]
