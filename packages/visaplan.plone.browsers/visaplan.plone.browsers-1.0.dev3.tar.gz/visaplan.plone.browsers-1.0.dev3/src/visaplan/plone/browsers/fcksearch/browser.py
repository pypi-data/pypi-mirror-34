# -*- coding: utf-8 -*- Umlaute: äöü
# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Andere Browser:
from Products.unitracc.browser.unitraccsearch.utils import normalizeQueryString

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import pp
logger, debug_active, DEBUG = getLogSupport(fn=__file__)


class IFCKsearch(Interface):

    def search(self):
        """ """

    def latestImage(self):
        """ """

    def latestLinks(self):
        """ """


class Browser(BrowserView):

    implements(IFCKsearch)

    def search(self):
        """ """

        context = self.context

        pc = context.getAdapter('pc')()
        author = self.context.getAdapter('auth')()
        form = context.REQUEST.form
        # pp(form=form)
        industrialsector = context.getBrowser('industrialsector')
        mine = False
        query = dict(form)
        query['sort_on'] = 'sortable_title'
        query['sort_limit'] = 300
        query['excludeFromSearch'] = False

        if query['where'] == 'mine':  # Nur für eigene Inhalte
            mine = True
            #query['allowedRolesAndUsers'] = ['user:%s' % author.getId()]
            del query['excludeFromSearch']
            # erstelle Query für Gruppeninhalts suche
            groups = author.getGroups()
            allowed = [group for group in groups]
            allowed.append(author.getId())
            query['getAccess'] = allowed

        if query.has_key('review_state'):
            if not query['review_state']:
                query['review_state'] = ['published',
                                         'inherit',
                                         'visible', ]
                if mine: # Falls eigener Inhalt auch Privat erlauben
                    del query['review_state']

        # Achtung: SearchableText und Title
        queryString = form.get('SearchableText', '')
        if queryString:
            DEBUG('search: queryString (1) = %(queryString)r', locals())
            queryList = normalizeQueryString(queryString)
            DEBUG('search: queryList (2.nQS) = %(queryList)r', locals())

            if not queryList:
                del query['SearchableText']  # XXX oben implizit aus form übernommen :-(
            elif query.get('titleonly'):
                del query['SearchableText']  # XXX oben implizit aus form übernommen :-(
                query['Title'] = queryList
            else:
                query['SearchableText'] = queryList
        elif 'SearchableText' in query:
            del query['SearchableText']  # XXX oben implizit aus form übernommen :-(

        # TODO: Die Verarbeitungslogik für den Fachbereich zentral
        #       implementieren, z. B. im Browser industrialsector!
        #Handle initial given getCode from dropdown
        if form.get('getCode', ''):
            list_ = industrialsector.search(form.get('getCode', ''))
            query['getCode'] = list_
        else:
            query['getCode'] = []

            if form.get('code1'):
                code1 = form.get('code1')[0]
            else:
                code1 = ''

            if form.get('code2'):
                code2 = form.get('code2')[0]
            else:
                code2 = ''

            if form.get('code3'):
                code3 = form.get('code3')
            else:
                code3 = []

            if code3:
                for code in code3:
                    query['getCode'].append(code1 + code2 + code)
            else:
                list_ = industrialsector.search(code1 + code2 + '*')
                query['getCode'] = list_

        if not query['getCode']:
            del query['getCode']
        else:
            query['getCode'] = {'query': query['getCode'],
                                'operator': 'or',
                                }

        if not query.get('getCustomSearch', ''):
            if form.get('media', '') == 'image':
                q = [pair[0]
                     for pair in context.getBrowser('unitracctype').getTypesWithImage()
                     ]
            else:
                q = [pair[0]
                     for pair in context.getBrowser('unitracctype').get()
                     ]
            query['getCustomSearch'] = {'query': q,
                                        'operator': 'or',
                                        }

        # pp(query=query)
        return pc(query)

    # Temporär ausser Betrieb da sinnfreie Implemtation
    # Bezogen auf den Content
    def latestImage(self):
        """ """
        context = self.context
        unitracctype = context.getBrowser('unitracctype')
        temp = context.getBrowser('temp')
        form = context.REQUEST.form
        pc = context.getAdapter('pc')()

        query = {}
        query['sort_on'] = 'sortable_title'
        query['review_state'] = 'private'
        query['getCustomSearch'] = {'query': [pair[0]
                                              for pair in unitracctype.getTypesWithImage()
                                              ],
                                    'operator': 'or',
                                    }

        portal = context.getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        query['path'] = {'query': temp.getTempFolder().getPath(),
                         'depth': 1}

        sm.setOld()

        return pc(query)

    # Temporär ausser Betrieb da sinnfreie Implemtation
    # Bezogen auf den Content
    def latestLinks(self):
        """ """
        context = self.context
        unitracctype = context.getBrowser('unitracctype')
        temp = context.getBrowser('temp')
        form = context.REQUEST.form
        pc = context.getAdapter('pc')()

        query = {}
        query['sort_on'] = 'sortable_title'
        query['review_state'] = 'private'
        query['getCustomSearch'] = {'query': [pair[0]
                                              for pair in unitracctype.get()
                                              ],
                                    'operator': 'or'}

        portal = context.getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        query['path'] = {'query': temp.getTempFolder().getPath(),
                         'depth': 1}

        sm.setOld()

        return pc(query)
