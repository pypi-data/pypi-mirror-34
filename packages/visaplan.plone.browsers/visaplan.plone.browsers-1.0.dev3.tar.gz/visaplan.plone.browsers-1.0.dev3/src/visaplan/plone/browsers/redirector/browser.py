from dayta.browser.public import BrowserView, implements, Interface


class IRedirector(Interface):

    pass


class Browser(BrowserView):

    implements(IRedirector)

    def __call__(self):
        """ """
        context = self.context
        portal = context.getAdapter('portal')()
        request = context.REQUEST
        if portal.absolute_url().find('www.') != -1:
            url = request['URL']
            url = url.replace('www.', '')

            if request['QUERY_STRING']:
                url += '?'
                url += request['QUERY_STRING']
            return context.REQUEST.RESPONSE.redirect(url)
