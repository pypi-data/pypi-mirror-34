# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)


class ILiterature(Interface):

    def search(self):
        """ """


class Browser(BrowserView):

    implements(ILiterature)

    def search(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        pc = context.getAdapter('pc')()
        txng = context.getBrowser('txng')

        queryString = form.get('SearchableText', '')
        DEBUG('search: queryString (1) = %(queryString)r', locals())
        queryString = txng.processWords(queryString)
        DEBUG('search: queryString (2.txng) = %(queryString)r', locals())

        query = {}
        query['portal_type'] = 'Document'
        query['getExcludeFromNav'] = False
        query['path'] = context.getPath()
        query['sort_on'] = 'getObjPositionInParent'

        if queryString:
            query['SearchableText'] = queryString

        if form.get('language', ''):
            query['Language'] = [form.get('language', ''), '_']

        return pc(query)
