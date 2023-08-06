from dayta.browser.public import BrowserView, implements, Interface
from zopyx.txng3.core.interfaces import INormalizer, IStopwords
from zope.component import createObject
from zope.component import getUtility

from visaplan.tools.coding import safe_decode


class ILightSearch(Interface):

    def filter(self, list1, list2):
        """First string is the query string second what is there result is true or false"""


class Browser(BrowserView):

    implements(ILightSearch)

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.langCode = 'en'    # TH: fix englisch?!
        self.normalizer = getUtility(INormalizer)
        self.splitter = createObject('txng.splitters.default',
                                casefolding=True,
                                separator='',
                                maxlen=30,
                                )
        self.sw_utility = getUtility(IStopwords)

    def _string_to_words(self, string_):

        string_ = self.normalizer.process(safe_decode(string_), self.langCode)
        words = self.splitter.split(string_)
        return self.sw_utility.process(words, self.langCode)

    def filter(self, string1, string2):
        # TODO: Dokumentieren; testbare Funktion (Doctest) auskoppeln

        words1 = self._string_to_words(string1)
        words2 = self._string_to_words(string2)

        string_ = ' '.join(words2)

        for word in list(words1):
            if string_.find(word) != -1:
                words1.remove(word)

        if not words1:
            return True
        return False
