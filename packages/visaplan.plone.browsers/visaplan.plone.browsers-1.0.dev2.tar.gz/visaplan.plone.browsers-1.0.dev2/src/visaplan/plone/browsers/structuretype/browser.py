# -*- coding: utf-8 -*- äöü

from dayta.browser.public import BrowserView, implements, Interface

# -------------------------- [ UIDs (Abweichungen nach Projekt!) ... [
# XXX UIDs wieder gleichziehen! (Update-Schritt)
# z. B. know-how/literaturverzeichnis:
UID_LITERATURE =           'a5f4907c00e2f12fe5626fb1d29336b9'
# z. B. know-how/virtuelle-baustellen:
UID_VIRTUALCONSTRUCTION =  'e7f3babe388b73b663c3fec239abf27e'
# z. B. akademie/vortraege:
UID_PRESENTATION =         '1255c69f5497ffb66ab21dfb9108ec4e'
# z. B. akademie/skripte:
UID_PAPER =                '6c7879ebbc919b61c72f77a4a1d9474f'
# z. B. know-how/dokumentation:
UID_DOCUMENTATION =        '9303f302674cb386293e2fa8ca46f7a3'
# z. B. know-how/handlungsanweisungen:
UID_INSTRUCTIONS =         '7dbcefcded46f02aa83458d8b13580be'
# z. B. know-how/fachbuecher:
UID_TECHNICALINFORMATION = '86c045bc109c562f129be4ae034bf3cb'
# -------------------------- ] ... UIDs (Abweichungen nach Projekt!) ]


class IStructureType(Interface):

    def getStructureFolderAsBrain(self, brain=None):
        """ """

    def getUIDVirtualConstructionFolder(self):
        """ """

    def getUIDPresentationFolder(self):
        """ """

    def getUIDPaperFolder(self):
        """ """

    def getUIDDocumentationFolder(self):
        """ """

    def getUIDInstructionsFolder(self):
        """ """

    def getUIDTechnicalInformationFolder(self):
        """ """

    def getTechnicalInformationFolders(self, review_state=''):
        """ """

    def getInstructionFolders(self, review_state=''):
        """ """

    def getDocumentationFolders(self, review_state=''):
        """ """

    def getPaperFolders(self, review_state=''):
        """ """

    def getPresentationFolders(self, review_state=''):
        """ """


class Browser(BrowserView):

    implements(IStructureType)

    def getStructureFolderAsBrain(self, brain=None):
        """
        Ermittle das nächste Elternelement, das die Wurzel eines
        Strukturelements ist, und gib es zurück.
        """
        context = self.context
        book = context.getBrowser('book')
        presentation = context.getBrowser('presentation')

        brains = context.getAdapter('aqparents')(brain)
        templates = book.getBookTemplates() + presentation.getPresentationTemplates()

        for brain in brains:
            if brain.getLayout in templates:
                return brain
            if brain.UID == UID_LITERATURE:
                return brain  # know-how/literaturverzeichnis
            if brain.UID == UID_VIRTUALCONSTRUCTION:
                return brain

    def getUIDVirtualConstructionFolder(self):
        # know-how/virtuelle-baustellen
        return UID_VIRTUALCONSTRUCTION

    def getUIDPresentationFolder(self):
        # akademie/vortraege
        return UID_PRESENTATION

    def getUIDPaperFolder(self):
        # akademie/skripte
        return UID_PAPER

    def getUIDDocumentationFolder(self):
        # know-how/dokumentation
        return UID_DOCUMENTATION

    def getUIDInstructionsFolder(self):
        # know-how/handlungsanweisungen
        return UID_INSTRUCTIONS

    def getUIDTechnicalInformationFolder(self):
        # know-how/fachbuecher
        return UID_TECHNICALINFORMATION

    def getTechnicalInformationFolders(self, review_state=''):
        """ """
        return self.getLevel(UID_TECHNICALINFORMATION, review_state)

    def getInstructionFolders(self, review_state=''):
        """ """
        return self.getLevel(UID_INSTRUCTIONS, review_state)

    def getDocumentationFolders(self, review_state=''):
        """ """
        return self.getLevel(UID_DOCUMENTATION, review_state)

    def getPaperFolders(self, review_state=''):
        """ """
        return self.getLevel(UID_PAPER, review_state)

    def getPresentationFolders(self, review_state=''):
        """ """
        return self.getLevel(UID_PRESENTATION, review_state)

    def getLevel(self, uid, review_state):
        """ """
        context = self.context
        pc = context.getAdapter('pc')()
        rc = context.getAdapter('rc')()

        query = {}
        query['sort_on'] = 'getTitleIndex'
        query['path'] = {'query': rc.lookupObject(uid).getPath(),
                         'depth': 1}
        if review_state:
            query['review_state'] = review_state

        return pc(query)
