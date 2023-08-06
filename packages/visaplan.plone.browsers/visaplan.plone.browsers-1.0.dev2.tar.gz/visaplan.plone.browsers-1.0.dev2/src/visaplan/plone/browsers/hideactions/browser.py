# -*- coding: utf-8 -*- äöü
"""\
Browser unitracc@@hideactions: Aktions-Buttons verbergen

TODO: Zweck dokumentieren!
"""
from dayta.browser.public import BrowserView, implements, Interface


class IHideActions(Interface):
    """ """

    pass


class Browser(BrowserView):

    implements(IHideActions)

    def __call__(self):
        """ """
        context = self.context
        if context.portal_type in ['UnitraccAuthor',
                                   'UnitraccContact',
                                   ]:
            return True
        if context.getAdapter('templateid')() in ['listing_news',
                                                  ]:
            return True
