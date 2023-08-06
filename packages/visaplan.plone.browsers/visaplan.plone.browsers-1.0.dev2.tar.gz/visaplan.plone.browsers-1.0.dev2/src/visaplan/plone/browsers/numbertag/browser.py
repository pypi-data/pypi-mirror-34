# -*- coding: utf-8 -*- äöü
from dayta.browser.public import BrowserView, implements, Interface
import re

# Verwendet vom transform-Browser
# (transformBookLinks bzw. transform_booklinks);
# siehe auch --> @picturenumber

# from pprint import pprint

class INumberTag(Interface):

    def get(self, haystack_uid, needle_uid):
        """ """


class Browser(BrowserView):

    implements(INumberTag)

    def get(self, haystack_uid, needle_uid, class_):
        """
        Durchsuche den Text (getRawText) des Katalogobjekts mit der UID
        <haystack_uid> nach <a>-Elementen.  Wenn ein passendes Element gefunden
        wird, gib die Nummer desselben im Kontext des Katalogobjekts zurück.
        """
        counter = 0
        if 0:
            \
        pprint((('haystack:', haystack_uid),
                ('needle:  ', needle_uid),
                ('class_:  ', class_),
                ))
        if not haystack_uid or not needle_uid:
            return counter
        context = self.context
        getbrain = context.getAdapter('getbrain')
        current = getbrain(haystack_uid)
        if current:
            text = str(current.getRawText)

            tags = [item[0] for item in re.findall(r'(\<(a)[^<]*</a>)', text)]

            orderNumberInPage = 0

            for tag in tags:
                if tag.find(class_) != -1:
                    counter += 1
                    if tag.find(needle_uid) != -1:
                        return counter

        return counter
