# -*- coding: UTF-8 -*- äöü
# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface
from plone.memoize import ram
from Acquisition import aq_inner

# Standardmodule:
import re

# Logging und Debugging:
from ...tools.debug import print_call_and_result, trace_this
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)
from visaplan.tools.debug import log_or_trace, pp
lot_kwargs = {'debug_level': debug_active,
              }


class IBook(Interface):

    def getBookImages(self):
        """ """

    def getPreviousBrain(self):
        """ """

    def getNextBrain(self):
        """ """

    def getFirst(self, brain):
        """ """

    def getLevelNumber(self):
        """ """

    def getCurrentUid(self, options):
        """ """

    def getInBookParents(self, brain=None):
        """ """

    def getBookTemplates(self):
        """ """

    def getBookFolderAsBrain(self):
        """ """

    def getCurrentParentAsBrain(self, options):
        """ """

    def getTree(self):
        """ """

    def getBookFolderTemplates(self):
        """ """

    def addPortlets(self):
        """ """

    def isBook(self, brain=None):
        """ """

    def getStyleClass(self, dict_):
        """ """

    def get_level(self):
        """ """

    def search():
        """
        Allgemeine Suche des book-Browsers
        """

    def search_technical_information():
        """
        Suche Fachbücher
        """

    def search_virtual_construction():
        """
        Suche Virtuelle Baustellen
        """

    def search_documentation():
        """
        Suche Baustellendokumentationen
        """


def cache_key(method, self, brain=None):

    if brain:
        uid = brain.UID
        modified = brain.modified
    else:
        uid = self.context.UID()
        modified = self.context.modified()
    return (uid, str(modified))


class Browser(BrowserView):

    implements(IBook)

    def getBookImages(self):
        """ """
        context = self.context
        pc = context.getAdapter('pc')()
        getbrain = context.getAdapter('getbrain')

        query = {}
        query['portal_type'] = ['Document']
        query['path'] = context.getPath()
        query['sort_on'] = 'getObjPositionInParent'
        query['getExcludeFromNav'] = False

        list_ = []

        for brain in pc(query):
            text = str(brain.getRawText)

            images = re.findall(r'src="(.+?)"', text)
            for src in images:
                src = src.lower()
                if src.find('resolveuid') != -1:
                    splitted = src.split('/')
                    uid = splitted[splitted.index('resolveuid') + 1]
                    list_.append((brain, uid))

        return list_

    @log_or_trace(**lot_kwargs)
    def _query(self, context, **kwargs):
        """
        Erzeuge die Suchargumente für --> search, search_technical_information etc.
        """
        query = {
            'portal_type': ['Folder',
                            'UnitraccAnimation',
                            ],
            'getExcludeFromNav': False,
            'sort_on': 'getObjPositionInParent',
            'review_state': ['visible', 'inherit',
                             'published', 'restricted'],
            }
        form = context.REQUEST.form

        queryString = form.get('SearchableText', '')
        if queryString:
            DEBUG('search: queryString (1) = %(queryString)r', locals())
            txng = context.getBrowser('txng')
            queryString = txng.processWords(queryString).strip()
            DEBUG('search: queryString (2.txng) = %(queryString)r', locals())

        if queryString:
            queryString = '*' + queryString + '*'
            query['SearchableText'] = queryString

        if form.has_key('getCustomSearch'):
            query['getCustomSearch'] = form['getCustomSearch']

        # Noch keine Behandlung etwaiger Doppelangaben:
        if kwargs:
            query.update(kwargs)
        return query

    def search(self):
        """
        @@book.search
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
	try:
            query = self._query(context)
            pc = context.getAdapter('pc')()
            brains = pc(query)

            return brains
	finally:
            sm.setOld()

    def search_technical_information(self):
        """
        Suche Fachbücher
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
	try:
            query = self._query(context,
                                getCustomSearch='layout=technical_information_view')
            # Methode wird aufgerufen, Stand: $Rev: 22045 $
            # pp(query=query)
            pc = context.getAdapter('pc')()
            brains = pc(query)

            return brains
	finally:
            sm.setOld()

    def search_virtual_construction(self):
        """
        Suche Virtuelle Baustellen
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
	try:
            query = self._query(context,
                                getCustomSearch='partOf=virtual_construction_view')
            # Methode wird aufgerufen, Stand: $Rev: 22045 $
            # pp(query=query)
            pc = context.getAdapter('pc')()
            brains = pc(query)

            return brains
	finally:
            sm.setOld()

    def search_documentation(self):
        """
        Suche Baustellendokumentationen
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
	try:
            query = self._query(context,
                                getCustomSearch='layout=documentation_view')
            # Methode wird aufgerufen, Stand: $Rev: 22045 $
            # pp(query=query)
            pc = context.getAdapter('pc')()
            brains = pc(query)

            return brains
	finally:
            sm.setOld()

    def getNextBrain(self, uid):
        """ """
        context = self.getContext()
        form = context.REQUEST.form
        getbrain = context.getAdapter('getbrain')
        tree = context.getBrowser('tree')

        current = getbrain(uid)

        if current:
            if current.exclude_from_nav:
                dict_ = tree.getNextBrain(current)
            else:
                dict_ = tree.getNextBrain(current, True)
            if not dict_:
                return
            dict_ = dict(dict_)

            last = self.getLast()

            if current and last and current.UID != last.UID:
                return dict_

    def getPreviousBrain(self, uid):
        """ """
        context = self.context
        form = context.REQUEST.form
        getbrain = context.getAdapter('getbrain')
        tree = context.getBrowser('tree')

        current = getbrain(uid)

        if current:
            if current.exclude_from_nav:
                dict_ = tree.getPreviousBrain(current.getParent(), True)
            else:
                dict_ = tree.getPreviousBrain(current, True)
            return dict_

    # @print_call_and_result
    def getBookFolder(self):
        """ """
        brain = self.getBookFolderAsBrain()
        if brain:
            return brain.getObject()

    # @trace_this
    def getBookFolderAsBrain(self, brain=None):
        """
        Ermittle den Wurzelordner des Fachbuchs
        """
        context = self.context
        getbrain = context.getAdapter('getbrain')
        if not brain:
            if context.portal_type == 'Plone Site':
                return
            brain = context.getHereAsBrain()
        if brain:
            if brain.getPartOf:
                parent = getbrain(brain.getPartOf)
                if parent:
                    if parent.getLayout in self.getBookTemplates():
                        return parent
            #Fallback while creation
            for parent in context.getAdapter('aqparents')(brain):
                if parent.getLayout in self.getBookTemplates():
                    return parent

    def getBookFolderInfo(self):
        """
        Gib Titel-, Autoreninformation und Veröffentlichungsjahr zurück
        """
        brain = self.getBookFolderAsBrain()
        if not brain:
            return 'INFO NOT FOUND'
        res = [brain.Title]
        val1 = brain.Rights
        if val1:
            res.extend([' / ', val1])
        val2 = brain.getDateForList
        if val2:
            res.extend([' (', str(val2.year()), ')'])
        return ''.join(res)

    @ram.cache(cache_key)
    def isBook(self, brain=None):
        """ """
        brain = self.getBookFolderAsBrain(brain)
        if brain and brain.getLayout in self.getBookTemplates():
            return True

    isBookPage = isBook
    # def isBookPage(self, brain=None):
    #     """
    #     Handelt es sich bei brain (bzw. dem Kontext) um eine Buchseite, im Sinne von:
    #     einem Dings unterhalb einer Buch-Wurzelseite?
    #     """
    #     brain = self.getBookFolderAsBrain(brain)
    #     if brain and brain.getLayout in self.getBookTemplates():
    #         return True

    def getBookNumberingFolderAsBrain(self):
        """ """
        context = self.context
        brains = context.getAdapter('aqparents')()
        bookTemplates = self.getBookTemplates()

        for brain in brains:
            if brain.getResetNumbering:
                return brain

    def getLevelNumber(self, brain):
        """ """
        parent = brain
        bookTemplates = self.getBookTemplates()

        counter = 1
        while hasattr(parent, 'getLayout'):
            if parent.getLayout in bookTemplates:
                return counter
            counter += 1
            parent = parent.getParent()
        return parent

    def getFirst(self):
        """ """
        context = self.context
        brain = self.getBookFolderAsBrain()

        tree = context.getBrowser('tree')
        brain = tree.getFirstAsBrain(brain)
        while brain and brain.portal_type == 'Folder':
            brain = tree.getNextBrain(brain)
            if brain:
                brain = brain['current']

        if not brain:
            brain = context.getHereAsBrain()
        return {'current': brain}

    def getLast(self):
        """ """
        context = self.context
        brain = self.getBookFolderAsBrain()

        tree = context.getBrowser('tree')
        brain = tree.getLastAsBrain(brain)
        while brain and brain.portal_type == 'Folder':
            brain = tree.getPreviousBrain(brain)
            if brain:
                brain = brain['current']

        if not brain:
            brain = context.getHereAsBrain()

        return brain

    def getBookTemplates(self):
        """ """
        return ['instructions_view',
                'documentation_view',
                'paper_view',
                'technical_information_view']

    def getBookFolderTemplates(self):
        """
        Templates für die *Übersichtsseiten*!
        """
        return ['documentation_folder_view',
                'technical_information_folder_view',  # Übersicht der Fachbücher
                'paper_folder_view',  # Übersicht der Skripte
                'instructions_folder_view']

    def getCurrentUid(self, options):
        """ """
        context = self.context
        form = context.REQUEST.form
        if form.has_key('uid'):
            return form['uid'].split('-')[1]

        if options.has_key('uid'):
            return options['uid']

        return self.getFirst()['current'].UID

    def getCurrentParentAsBrain(self, options):
        context = self.context
        getbrain = context.getAdapter('getbrain')

        uid = self.getCurrentUid(options)
        current = getbrain(uid)
        if current.portal_type != 'Folder':
            return current.getParent()
        else:
            return current

    def getInBookParents(self, brain=None):
        """ """
        context = self.context

        brains = context.getAdapter('aqparents')(brain)
        bookTemplates = self.getBookTemplates()
        brains.reverse()
        counter = 0

        for brain in brains:
            if brain.getLayout in bookTemplates:
                break
            counter += 1

        brains = brains[counter:]
        brains.reverse()

        return brains[1:]

    def getTree(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        self.tree = context.getBrowser('tree')
        self.tree.query['is_default_page'] = False

        brain = self.tree.getRelBrain()
        if not brain:
            brain = context.getHereAsBrain()

        brains = self.getInBookParents(brain)
        brains.reverse()

        if brain and brain.portal_type == 'Folder':
            brains.append(brain)

        return self.recurse(brains, [])

    def getResetTree(self, brain):
        """ """
        context = self.context
        self.tree = context.getBrowser('tree')

        return self.recurse([brain], [], excludeFromNav=False)

    def recurse(self, parents, results, level=1, index=0, excludeFromNav=True):
        """ """
        if index < len(parents):
            brains = self.tree.getCachedLevel(parents[index], excludeFromNav)

            for brain in brains:
                dict_ = {}
                dict_['current'] = brain
                dict_['level'] = level
                dict_['childs'] = []

                results.append(dict_)

                if index + 1 < len(parents):
                    if parents[index + 1].UID == brain['UID']:
                        self.recurse(parents, dict_['childs'], level + 1, index + 1, excludeFromNav=excludeFromNav)

        return results

    def addPortlets(self):
        context = self.context

        context.getBrowser('authorized').add_folder()

        for templateId in ['portlet_book_navigation']:
            mapping = context.restrictedTraverse('++contextportlets++plone.leftcolumn')
            addview = mapping.restrictedTraverse('+/portlets.Classic')
            addview.createAndAdd(data={'template': templateId})

    def getStyleClass(self, dict_):
        context = aq_inner(self.context)

        string_ = ''


        if context.absolute_url().startswith(dict_['getURL'] + '/') and context.absolute_url() != dict_['getURL']:
            string_ += 'navigation-open'

        if context.UID() == dict_['UID'] or context.aq_parent.UID() == dict_['UID']:
            if not string_:
                string_ += 'navigation-current'
            else:
                if context.getExcludeFromNav():
                    string_ = 'navigation-current'
        return  string_

    def get_level(self):

        context = self.context

        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = ['Document', 'Folder']
        query['sort_on'] = 'getObjPositionInParent'
        query['getExcludeFromNav'] = False
        query['path'] = {'query': context.getPath(),
                         'depth': 1}

        return pc(query)
