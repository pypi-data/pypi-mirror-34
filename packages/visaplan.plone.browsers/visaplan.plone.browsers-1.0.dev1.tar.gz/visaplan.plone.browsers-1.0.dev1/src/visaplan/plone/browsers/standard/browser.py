# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
from DateTime import DateTime

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)


class IStandardBrowser(Interface):

    def search(self):
        """ """


class Browser(BrowserView):

    implements(IStandardBrowser)

    def search(self):
        """ """
        context = self.context
        getAdapter = context.getAdapter
        portal = getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        form = context.REQUEST.form
        pc = getAdapter('pc')()
        txng = context.getBrowser('txng')

        queryString = form.get('SearchableText', '')
        DEBUG('search: queryString (1) = %(queryString)r', locals())
        queryString = txng.processWords(queryString).strip()
        DEBUG('search: queryString (2.txng) = %(queryString)r', locals())
        if queryString:
            queryString = '*' + queryString + '*'

        query = {
            'portal_type': 'UnitraccStandard',
            'getExcludeFromNav': False,
            'sort_on': 'sortable_title',
            'review_state': ['visible', 'inherit',
                             'published'],  # TH: warum nicht auch 'restricted'?
            'effective': {'query': DateTime(),
                          'range': 'max'},
            }

        if form.get('source', ''):
            query['getCustomSearch'] = ['source=' + form.get('source', '')]

        if queryString:
            query['SearchableText'] = queryString

        if form.get('language', ''):
            if form['language'] == 'all':
                # TH 16.3.2017: Warum nicht einfach weglassen?
                langs = [x[0] for x in getAdapter('pl')().listSupportedLanguages()]
            else:
                langs = [form['language']]
            query['Language'] = langs

        if form.get('Subject', ''):
            query['Subject'] = form.get('Subject', '')
        brains = pc(query)

        sm.setOld()

        return brains
