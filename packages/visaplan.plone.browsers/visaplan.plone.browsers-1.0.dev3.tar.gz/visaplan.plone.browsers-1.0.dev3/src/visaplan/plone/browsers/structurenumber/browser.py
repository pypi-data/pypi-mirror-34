from dayta.browser.public import BrowserView, implements, Interface
from plone.memoize import ram


def cache_key(method, self, uid=None):

    if not uid:
        uid = self.context.UID()
    return uid


class IStructureNumber(Interface):

    def get(self):
        """ """

    def isVisible(self):
        """ """

    def set(self, brain):
        """ """


class Browser(BrowserView):

    implements(IStructureNumber)

    key = 'structureNumber'

    @ram.cache(cache_key)
    def get(self, uid=None):
        """ """
        context = self.context
        book = context.getBrowser('book')
        if not uid:
            brain = context.getHereAsBrain()
        else:
            getbrain = context.getAdapter('getbrain')
            brain = getbrain(uid)

        parents = book.getInBookParents(brain)
        parents.reverse()
        if brain:
            parents.append(brain)
        list_ = []

        for parent in parents:
            number = parent.getStructureNumber
            if number:
                list_.append(str(number))

        return '.'.join(list_)

    def isVisible(self):
        """ """
        context = self.context
        book = context.getBrowser('book')
        if book.getBookFolderAsBrain():
            return True

    def set(self, brain):
        """ """
        context = self.context
        pc = context.getAdapter('pc')()
        parent = brain.getParent()
        tree = context.getBrowser('tree')

        query = {}
        query['getCustomSearch'] = 'generateStructureNumber=True'
        query['sort_on'] = 'getObjPositionInParent'
        query['portal_type'] = tree.getTreeTypes()
        query['path'] = {'query': parent.getPath(),
                         'depth': 1}

        ids = [b.getId for b in pc(query)]

        number = 0
        if brain.getGenerateStructureNumber:
            if ids.count(brain.getId):
                number = ids.index(brain.getId) + 1

        if brain.getStructureNumber != number:
            object_ = brain._unrestrictedGetObject()
            object_.setStructureNumber(number)
            object_.setModificationDate(object_.modified() + 0.000001)
            pc.reindexObject(object_, ['modified'], update_metadata=1)
