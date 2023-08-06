# -*- coding: utf-8 -*-
"""
unitracc@@presentation: Browsermodul zur Unterstützung von Vorträgen

siehe (gf) ./LIESMICH.txt
"""
# Plone/Zope/dayta:
from AccessControl import Unauthorized
from dayta.browser.public import BrowserView, implements, Interface
from plone.memoize import ram

# Installierte Module:
import demjson

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport

# Dieser Browser:
from .crumbs import OK

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport('presentation')
if debug_active:
    from pprint import pprint


class IPresentationBrowser(Interface):

    def search(self):
        """ """

    def getFoilCount(self, brain):
        """
        Ermittle die Gesamtanzahl der Folien des Vortrags.
        """

    def getToc(self):
        """ """

    def getCurrentFoilNumber(self):
        """ """

    def getPresentationFolder(self):
        """ """

    def getAgenda(self, uid):
        """
        Erstelle die Agenda fuer den Vortrag.
        """

    def isPresentationPage(self):
        """ """

    def getPresentationTemplates(self):
        """ """

    def getPresentationFolderTemplates(self):
        """ """

    def getBookFolderAsBrain(self, brain=None):
        """ """

    def getPresentations(self):
        """ """

    def isPresentation(self):
        """ """

    def getHelp(self, lang):
        """
        Gib das Objekt für die (deutsche oder englische) Benutzungshilfe für
        Präsentationsseiten zurück.
        Achtung: es werden hartcodierte UIDs verwendet!
        """

    def getHelpAsDict(self, lang):
        """
        Rufe getHelp auf und gib ein Python-Dict mit den Schlüsseln getText und
        getRawTitle zurück
        """

    def get_template(self, current, template_id):
        """ """

    def go_to(self):
        """
        Springe auf Seite
        """


def cache_key(method, self, brain):
    pc = self.context.getAdapter('pc')()

    return (brain.UID, pc.getCounter())


class Browser(BrowserView):

    implements(IPresentationBrowser)

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
            queryString = txng.processWords(queryString).strip()
            DEBUG('search: queryString (2.txng) = %(queryString)r', locals())

            if queryString:
                queryString = '*' + queryString + '*'
                query['SearchableText'] = queryString

            query['portal_type'] = 'Folder'
            query['getExcludeFromNav'] = False
            query['sort_on'] = 'getObjPositionInParent'
            query['getCustomSearch'] = 'layout=presentation_view'

            query['review_state'] = ['visible', 'inherit',
                                     'published', 'restricted']
            brains = pc(query)
            return brains
        finally:
            sm.setOld()

    # @ram.cache(cache_key)
    def getAgenda(self, uid):
        """
        Gib die Agenda für den Vortrag zurueck
        """
        context = self.context
        tree = context.getBrowser('tree')
        uid = uid.split("-")[-1]
        course_agenda = context.getBrowser('unitracccourse')
        navigation = tree.getFlatNavigationWithBrains()
        navigation = course_agenda.get_navigation(uid, navigation)
        list_of_elements = []
        parents = []

        def handle_childs(element):
            """
            Eliminiere alle Inhalte, die nicht vom Typ UnitraccLesson (Lektion)
            oder Folder sind.
            """
            childs = []
            for child in element['childs']:
                child['title'] = child['Title']
                if not child['portal_type'] in ["UnitraccLesson", "Folder"]:
                    continue
                else:
                    if child['childs']:
                        if child['class'] == 'navigation-current':
                            child['childs'] = []
                        else:
                            child['childs'] = handle_childs(child)

                    child['uid_object'] = "uid-" + child['uid_object']
                    childs.append(child)

            return childs

        for element in navigation:
            element['title'] = element['Title']
            if element['childs']:
                if element['class'] == 'navigation-current':
                    element['childs'] = []
                else:
                    element['childs'] = handle_childs(element)

            element['uid_object'] = "uid-" + element['uid_object']
            list_of_elements.append(element)

        return list_of_elements

    @ram.cache(cache_key)
    def getFoilCount(self, brain):
        """
        Ermittle die Gesamtanzahl der Folien des Vortrags.

        Vorgehensweise: es werden alle Objekte unter dem übergebenen
        Wurzelelement gezählt, die nicht von der Navigation
        ausgeschlossen sind, und anschließend das Wurzelelement
        abgezogen.
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            pc = context.getAdapter('pc')()

            query = {}
            query['path'] = brain.getPath()
            query['getExcludeFromNav'] = False

            len_brains = len(pc(query)) - 1

            return len_brains
        finally:
            sm.setOld()

    def getToc(self):
        context = self.context
        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = 'Document'
        query['getExcludeFromNav'] = False
        query['sort_on'] = 'getObjPositionInParent'
        query['path'] = context.getPath()

        return pc(query)

    def getCurrentFoilNumber(self):
        context = self.context
        tree = context.getBrowser('tree')
        uid = tree.getRelUid()

        for dict_ in tree.getFlatNavigationWithoutBrains():
            if dict_['current'] == uid:
                return dict_['number']

        # alter Code:
        counter = 1
        for dict_ in tree.getFlatNavigationWithoutBrains():
            if dict_['current'] == uid:
                return counter
            counter += 1
        return counter

    def getPresentationFolder(self):
        """
        Gib das Wurzelelement des aktuellen Vortrags zurueck;
        siehe auch @@storagefolder.getPresentationFolder
        """
        parent = self.getContext()

        while hasattr(parent, 'getLayout') and parent.getLayout() != 'presentation_view':
            parent = parent.aq_parent
            if parent.portal_type == 'Plone Site':
                return
        return parent

    def isPresentationPage(self):
        context = self.getPresentationFolder()

        if hasattr(context, 'getLayout') and context.getLayout() == 'presentation_view':
            return True

    def getPresentationTemplates(self):
        """ """
        return ['presentation_view']

    def getPresentationFolderTemplates(self):
        """ """
        return ['presentation_folder_view']

    def getBookFolderAsBrain(self, brain=None):
        """ """
        context = self.context
        brains = context.getAdapter('aqparents')(brain)
        presentationTemplates = self.getPresentationTemplates()

        for brain in brains:
            if brain.getLayout in presentationTemplates:
                return brain

    def getPresentations(self):
        context = self.context

        pc = context.getAdapter('pc')()
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getPresentationFolder()

        query = {}
        query['sort_on'] = 'sortable_title'
        query['getCustomSearch'] = 'layout=presentation_view'

        query['path'] = {'query': folder.getPath(),
                         'depth': 1}

        return pc(query)

    def isPresentation(self, UID=''):
        """
        Checks if context is within a presentation
        """
        context = self.context
        brain = False

        if UID:
            getbrain = context.getAdapter('getbrain')
            brain = getbrain(UID)

        else:
            if context.portal_type != 'Plone Site':
                brain = context.getHereAsBrain()

        if brain:
            # print "BRAIN: %s" % brain.Title
            for parent in context.getAdapter('aqparents')(brain):
                # print "PARENT: %s" % parent.Title
                if hasattr(parent, 'getLayout') and \
                parent.getLayout == 'presentation_view':
                    return True

        return False

    def getHelp(self, lang):
        """
        Gib das Objekt für die (deutsche oder englische) Benutzungshilfe für
        Präsentationsseiten zurück.
        Achtung: es werden hartcodierte UIDs verwendet!

        .../resolvei18n/95a12f3c39ba704e2fc07ace91673857
        """
        context = self.context
        rc = context.getAdapter('rc')()

        # Hilfe für die Präsentationsansicht,
        # /hilfe/hilfe-praesentationsansicht/hilfe-fuer-die-praesentationsansicht:
        uid = "95a12f3c39ba704e2fc07ace91673857"
        if lang == "en":
            # engl. Version, Help for presentation view:
            uid = "96e5c48e8cf05afbd67a54abc6da49e6"
        if debug_active:
            auth = context.getBrowser('auth')
            user_id = auth.getId()
            DEBUG('getHelp(%(lang)r): Benutzer ist %(user_id)r', locals())

        obj = rc.lookupObject(uid)
        if debug_active:
            DEBUG('getHelp(%(lang)r): Objekt ist %(obj)r', locals())
            try:
                method = obj.getRawText
                DEBUG('getHelp(%(lang)r): method ist %(method)r', locals())
                value = method()
                DEBUG('getHelp(%(lang)r): value ist %(value)r', locals())
            except Unauthorized as e:
                logger.error('Fehler beim Zugriff!')
                logger.exception(e)
            except Exception as e:
                logger.error('Sonstiger Fehler!')
                logger.exception(e)
            else:
                DEBUG('getHelp(%(lang)r): sieht gut aus!', locals())

        return obj

    def getHelpAsDict(self, lang):
        """
        Rufe getHelp auf und gib ein Python-Dict mit den Schlüsseln getText und
        getRawTitle zurück
        """
        DEBUG('getHelpAsDict(%(lang)r) ...', locals())
        obj = self.getHelp(lang)
        res = {'getText': obj.getText(),
                'getRawTitle': obj.getRawTitle(),
                }
        if debug_active:
            pprint(('@@presentation.getHelpAsDict -->', res))
        return res

    def get_template(self, current, template_id):
        """ """
        return current.unrestrictedTraverse(str(template_id), None)

    def go_to(self):
        """
        Springe auf Seite
        """
        context = self.context
        form = context.REQUEST.form

        rc = context.getAdapter('rc')()

        puid = form.get('puid')
        view = form.get('view')
        page = form.get('page')
        ajax = form.get('ajax')

        brain = rc.lookupObject(puid)

        try:
            page = int(page)
        except ValueError:
            return None

        tree = context.getBrowser('tree')
        cooked = brain.getHereAsBrain()  # ist das nötig?!
        identical = cooked is brain
        DEBUG('goto(): brain=%r, cooked=%r, identisch: %s, gleich: %s',
              brain, cooked, identical, identical or brain == cooked)
        one_based_tuple = tree.getFlatNavigationNumbersMap(cooked)[1]
        try:
            suid = one_based_tuple[page]
        except IndexError:
            return None

        if not ajax:
            url = brain.absolute_url() + "/" + view + "?uid=uid-" + suid
            context.REQUEST.response.redirect(url)

        return demjson.dumps({'uid': suid})
