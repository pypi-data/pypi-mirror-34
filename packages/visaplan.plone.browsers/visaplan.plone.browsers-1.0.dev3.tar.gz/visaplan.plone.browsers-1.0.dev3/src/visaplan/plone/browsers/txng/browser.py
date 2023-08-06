from dayta.browser.public import BrowserView, implements, Interface


class ITxng(Interface):

    def processWords(string_):
        """ """

    def get(self, string_):
        """ """


class Browser(BrowserView):

    implements(ITxng)

    def processWords(self, string_):

        _stw = self.context.getBrowser('lightsearch')._string_to_words
        # TH: safe_decode durch @@lightsearch._string_to_words aufgerufen 
        return u' '.join(_stw(string_))

    def get(self, string_):

        value = self.processWords(string_)
        value = value.strip()
        if value:
            value = u'*' + value + u'*'
        return value
