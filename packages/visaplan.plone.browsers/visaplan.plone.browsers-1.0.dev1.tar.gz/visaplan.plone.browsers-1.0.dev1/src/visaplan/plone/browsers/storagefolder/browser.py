# -*- coding: utf-8 -*-

from dayta.browser.public import BrowserView, implements, Interface


class IStorageFolder(Interface):

    def getVirtualConstructionFolder(self):
        """ """

    def getPresentationFolder(self):
        """ """

    def getPaperFolder(self):
        """ """

    def getDocumentationFolder(self):
        """ """

    def getInstructionsFolder(self):
        """ """

    def getTechnicalInformationFolder(self):
        """ """


class Browser(BrowserView):

    implements(IStorageFolder)

    def getVirtualConstructionFolder(self):
        context = self.context
        uid = context.getBrowser('structuretype').getUIDVirtualConstructionFolder()
        rc = context.getAdapter('rc')()
        return rc.lookupObject(uid)

    def getPresentationFolder(self):
        """
        Gib den Container für alle Vorträge zurück;
        siehe auch @@presentation.getPresentationFolder
        """
        context = self.context
        uid = context.getBrowser('structuretype').getUIDPresentationFolder()
        rc = context.getAdapter('rc')()
        return rc.lookupObject(uid)

    def getPaperFolder(self):
        context = self.context
        uid = context.getBrowser('structuretype').getUIDPaperFolder()
        rc = context.getAdapter('rc')()
        return rc.lookupObject(uid)

    def getDocumentationFolder(self):
        context = self.context
        uid = context.getBrowser('structuretype').getUIDDocumentationFolder()
        rc = context.getAdapter('rc')()
        return rc.lookupObject(uid)

    def getInstructionsFolder(self):
        context = self.context
        rc = context.getAdapter('rc')()
        uid = context.getBrowser('structuretype').getUIDInstructionsFolder()
        return rc.lookupObject(uid)

    def getTechnicalInformationFolder(self):
        context = self.context
        uid = context.getBrowser('structuretype').getUIDTechnicalInformationFolder()
        rc = context.getAdapter('rc')()
        return rc.lookupObject(uid)
