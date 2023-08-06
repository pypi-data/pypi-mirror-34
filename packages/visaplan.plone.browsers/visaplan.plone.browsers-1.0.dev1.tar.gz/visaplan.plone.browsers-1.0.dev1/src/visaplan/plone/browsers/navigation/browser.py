# -*- coding: utf-8 -*-
"""
Browser unitracc@@navigation: Navigation und Menü

siehe auch (gf; zusammenführen?)
../../adapters/getmenulevel/adapter.py
"""
# Plone/Zope/dayta:
from dayta.browser.public import BrowserView, implements, Interface
from Products.CMFCore.Expression import Expression, getExprContext
from Products.CMFCore.interfaces._tools import IActionCategory, IAction

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.profile import StopWatch

# Logging und Debugging:
from visaplan.tools.debug import pp
logger, debug_active, DEBUG = getLogSupport('navigation')
sw_kwargs = {'enable': bool(debug_active),
             }


class INavigation(Interface):
    """ Interface fuer Browser fuer alle Navigationen der Unitracc-Site """

    def getStructuredNavigation(self):
        """Create structured async side navigation"""

    def get_bottom_level(self, brain):
        """ """

    def get_actions(self, categories, hidden=True):
        """ """


class Browser(BrowserView):
    """ Browser fuer alle Navigationen der Unitracc Seite """

    implements(INavigation)

    def __init__(self, context, request):
        """ """
        BrowserView.__init__(self, context, request)
        self.pc = context.getAdapter('pc')()

    def get_bottom_level(self, current, maxcount=None):
        """
        Gib Menüpunkte (1. oder 2. Ebene) für das Fußleistenmenü zurück
        """
        context = self.context
        getAdapter = context.getAdapter
        pc = getAdapter('pc')()

        query = {
            'getExcludeFromNav': False,
            'portal_type': 'Folder',
            'sort_on': 'getObjPositionInParent',
            'path': {'query': current.getPath(),
                     'depth': 1,
                     },
            }
        if maxcount is not None:
            query['sort_limit'] = int(maxcount)
        # print '*** navigation.get_bottom_level(%(query)r)' % query['path']

        res = pc(query)
        # pp(res[0], dict(res[0]))
        return res
        translate = getAdapter('translate')
        for brain in res:
            if brain.Language:
                brain['translated_title'] = brain.Title
            else:
                brain['translated_title'] = translate(brain.Title)
        return res

    def getStructuredNavigation(self, uid=None):
        """
        Erstellt eine Navigation, die strukturierte Elemente anzeigt.
        Das aktuelle Element wird hervorgehoben.

        Input uid = string
        Output = Liste mit Dictionarys
        Struktur: [
                   {'title':'Inhalt', 'type':'Folder'
                    'level':1, 'uid':'dasdajskldjas783892394',
                    'selected:False', ''
                    'children':[{'title':'x', 'type':'UnitraccDocument',
                                 'level':2, 'uid':231das8dakdasdas',
                                 'selected':True, 'children':None}, ...]
                   },
                  {'title':'L1', 'type':'UnitraccDocument',
                   'level':1, 'uid':'23847238hudhas',
                   'selected':False, 'children':None}, ...
                  ]
        """
        with StopWatch('@@navigation.getStructuredNavigation(%(uid)r)',
                       mapping=locals(),
                       **sw_kwargs) as stopwatch:
            if uid is None:
                return []
            # Hole alle notwendigen Adapter
            context = self.context

            tree = context.getBrowser('tree')
            unitracccourse = context.getBrowser('unitracccourse')

            # Nutzer angemeldet?
            #sanon = context.getAdapter('isannav =on')()
            #if isanon:
            #    raise AuthenticatedError

            # Hole alle Elemente des Objekts und verarbeite sie zum Output
            output = []
            try:
                uid = uid.split("-")[1]
            except:
                pass
            selected = False  # XXX nicht verwendet!
            stopwatch.lap('Vorbereitungen')

            nav = tree.getFlatNavigationWithoutBrains()
            stopwatch.lap('@@tree.getFlatNavigationWithoutBrains')
            if debug_active:
                pp({'nav': nav,
                    })
            try:
                first = nav[0]
            except IndexError:
                return []
            output = unitracccourse.get_navigation(uid, nav)
            if debug_active:
                pp({'output': output,
                    })

            return output

    def _createNavDict_(self, value):
        """ erstelle Dictionary fuer StrukturNavigation """
        aktelem = value['current']
        element = {}
        element['title'] = value['Title']
        element['level'] = value['level']
        element['current'] = aktelem
        element['uid'] = aktelem.UID
        element['portal_type'] = aktelem.portal_type
        element['class'] = " "
        element['childs'] = value['childs']
        element['children'] = []
        return element

    def get_actions(self, categories, hidden=True):

        context = self.context
        pa = context.getAdapter('pa')()
        checkPerm = context.getAdapter('checkperm')
        translate = context.getAdapter('translate')

        self._list = []
        for category in categories:
            #Could be category or action
            category_dict = self._set_action_item(pa[category], self._list)
            for item in pa[category].objectValues():
                current_dict = self._set_action_item(item, category_dict['children'])
                if IActionCategory.providedBy(item):
                    self._recurse_actions(item, current_dict['children'])

        return self._list

    def _set_action_item(self, item, current):
        """ """
        context = self.context
        check_perm = context.getAdapter('checkperm')
        translate = context.getAdapter('translate')

        if IAction.providedBy(item):
            for permission in item.permissions:
                if not check_perm(permission):
                    return

        dict_ = {}

        if IAction.providedBy(item):
            show = True
            if item.available_expr and not Expression(item.available_expr)(getExprContext(context, context)):
                show = False
            for permission in item.permissions:
                if not check_perm(permission):
                    show = False
                    return
            if not show:
                return

        if IAction.providedBy(item):
            dict_['title'] = translate(msgid=getattr(item, 'msgid', item.title),
                                       domain=item.i18n_domain,
                                       default=item.title)
        else:
            domain = item.getProperty('domain', 'plone')
            msgid = item.getProperty('msgid', item.title)
            dict_['title'] = translate(msgid=msgid,
                                       domain=domain,
                                       default=item.title)

        if IActionCategory.providedBy(item):
            dict_['children'] = []
            dict_['interface'] = 'IActionCategory'

        if IAction.providedBy(item):
            dict_['interface'] = 'IAction'
            dict_['target'] = item.getProperty('link_target', '_self')
            dict_['class'] = item.getProperty('class_', '')
            dict_['url'] = Expression(item.url_expr)(getExprContext(context, context))

        current.append(dict_)

        return dict_

    def _recurse_actions(self, current_item, list_children):
        """ """
        for item in current_item.objectValues():
            current_dict = self._set_action_item(item, list_children)
            if IActionCategory.providedBy(item):
                self._recurse_actions(item, current_dict['children'])
