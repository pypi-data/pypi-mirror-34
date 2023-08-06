# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß
# Plone/Zope/dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
from DateTime import DateTime

# Unitracc-Tools:
from ...tools.search import language_spec

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)


class IGlossaryBrowser(Interface):

    def search(self):
        """ """


class Browser(BrowserView):

    implements(IGlossaryBrowser)

    def search(self):
        """ """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        try:
            form = context.REQUEST.form
            pc = context.getAdapter('pc')()
            txng = context.getBrowser('txng')
            query = {}

            queryString = form.get('SearchableText', '')
            DEBUG('search: queryString (1) = %(queryString)r', locals())
            if queryString and type(queryString) == type(''):
                queryString = txng.get(queryString)
                DEBUG('search: queryString (2.txng.get) = %(queryString)r', locals())
                if queryString:
                    query['SearchableText'] = queryString

            query['portal_type'] = 'UnitraccGlossary'
            query['getExcludeFromNav'] = False
            query['sort_on'] = 'sortable_title'
            query['effective'] = {'query': DateTime(),
                                  'range': 'max'}

            query['review_state'] = ['inherit', 'published', 'visible']

            langs = language_spec(form=form,
                                  # aktuelles Verhalten (schlau so?):
                                  default_to_all=False,
                                  context=context)
            if langs:
                query['Language'] = langs
            DEBUG('search: query (3) = %(query)s', locals())
            brains = pc(query)
            DEBUG('search: query (4) = %d Treffer', len(brains))

            return brains
        finally:
            sm.setOld()
