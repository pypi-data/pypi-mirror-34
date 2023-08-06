from dayta.browser.public import BrowserView, implements, Interface
import json


class IJson(Interface):

    def encode(self, value):
        """ """

    def decode(self, value):
        """ """


class Browser(BrowserView):

    implements(IJson)

    def encode(self, value):
        return json.dumps(value)

    def decode(self, value):
        return json.loads(value)
