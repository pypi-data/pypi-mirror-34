# -*- coding: utf-8 -*-
"""
Browser @@temp - Zugriff auf den temp-Ordner
"""
# Standardmodule:
from random import randint
from DateTime import DateTime

# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface
from AccessControl import Unauthorized
import transaction

# Unitracc-Tools:
from visaplan.tools.classes import Counter
from ...tools.forms import tryagain_url, merge_qvars
from ...tools.misc import translate_dummy as _
from visaplan.tools.debug import pp

# Andere Browser:
from ..unitraccfeature.utils import TEMP_UID

# Logging und Debugging:
import logging
logger = logging.getLogger('unitracc@@temp')
copylog = logging.getLogger('Copy@@temp')


def copyid():
    """
    Gib einen Marker zurück, um den einzelnen Kopiervorgang in den Logdateien
    identifizierbar zu machen
    """
    return '%08x' % randint(0, 2 ** 32)


class ITemp(Interface):

    def create(self):
        """ """

    def getTempFolder(self):
        """ """

    def addImage(self):
        """ """

    def addFormula(self):
        """ """

    def addVideo(self):
        """ """

    def addAnimation(self):
        """ """

    def addStandard(self):
        """ """

    def addGlossary(self):
        """ """

    def addArticle(self):
        """ """

    def addLiterature(self):
        """ """

    def addNews(self):
        """ """

    def addEvent(self):
        """ """

    def addTable(self):
        """ """

    def addCourse(self):
        """ """

    def authAdd(self):
        """ """

    def addPresentation(self):
        """ """

    def addTechnicalInformation(self):
        """ """

    def addInstructions(self):
        """ """

    def addDocumentation(self):
        """ """

    def addPaper(self):
        """ """

    def addBinary(self):
        """ """

    def addAnimation(self):
        """ """

    def addAudio(self):
        """ """

    def addVideo(self):
        """ """

    def copyPresentation(self):
        """ """

    def canAddArticle(self):
        """ """

    def canAddNews(self):
        """ """

    def canAddEvent(self):
        """ """

    def canAddImage(self):
        """ """

    def getTranslatedSchemaLabel(self):
        """ """

    def canAddGlossary(self):
        """ """

    def canAddLiterature(self):
        """ """

    def canAddFormula(self):
        """ """

    def canModifyObject(self, uid):
        """ """

    def canDeleteObject(self, uid):
        """ """

    def canAddStandard(self):
        """ """

    def copyTechnicalInformation(self):
        """ """

    def cleanupTemp(self):
        """ """

    def copyInstruction(self):
        """ """

    def copyPaper(self):
        """ """

    def copyDocumentation(self):
        """ """

    def publishStructure(self):
        """
        Veröffentliche das per Formular angegebene Strukturelement.

        Ersetzt die bisherigen (jeweils identischen!) Methoden
        publishDocumentation, publishInstruction, publishPaper,
        publishPresentation und publishTechnicalInformation.
        Es wird weiterhin für die eigentliche Arbeit _publish
        aufgerufen.
        """

    def setStructureGroups(self):
        """ """

    def setSubportal(self):
        """
            Setze die Subportale für die Strukturelemente
        """

    def deletePrivateStructure(self):
        """ """

    def canAdd(self, portal_type):
        """
        Darf der angemeldete Benutzer den uebergebenen Typ im temp-Ordner hinzufuegen?
        """

    def canAddCourse(self):
        """ """


class Browser(BrowserView):

    implements(ITemp)

    def getTempFolder(self):
        """ """
        context = self.context
        rc = context.getAdapter('rc')()

        return rc.lookupObject(TEMP_UID)

    def create(self):
        """ """
        context = self.context

        if context.getAdapter('isanon')():
            raise Unauthorized

        portal = context.getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            rc = context.getAdapter('rc')()
            form = context.REQUEST.form

            folder = self.getTempFolder()

            object_ = rc.lookupObject(form.get('uid'))

            errors = {}
            errors = object_.validate(REQUEST=context.REQUEST, errors=errors, data=1, metadata=0)

            if errors:
                form.update({'errors': errors})
                return object_.restrictedTraverse(form.get('template_id'))()

            object_.processForm()

            object_.getBrowser('workflow').change('make_private')
        finally:
            sm.setOld()

        return context.REQUEST.RESPONSE.redirect(object_.absolute_url())

    def temp(self, portal_type, templateId):
        context = self.context

        if context.getAdapter('isanon')():
            raise Unauthorized

        userId = context.getAdapter('auth')().getId()
        items = []

        portal = context.getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        try:
            sm.setNew()

            folder = self.getTempFolder()
            form = context.REQUEST.form

            # Derzeit wichtig, um beim Erzeugen neuer Objekte Brotkrümel für
            # den Gruppenschreibtisch auszugeben.
            # FIXME: nach Speichern des neuen Objekts ist man dann trotzdem
            #        in myContent gelandet ...
            gid = form.get('gid', None)
            if gid is not None:
                items.append(('gid', gid))

            form.update({'template_id': templateId})

            createObject = folder.getAdapter('createobject')
            object_ = createObject(portal_type, '')

            changeowner = object_.getBrowser('changeowner')
            changeowner.set(userId)

            object_.getBrowser('workflow').change('make_private')

            object_.unindexObject()
            self.object_ = object_
        finally:
            sm.setOld()

        url = merge_qvars('/'.join((object_.absolute_url(), templateId)),
                          items)
        return context.REQUEST.RESPONSE.redirect(url)

    def addImage(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccImage')
        return self.temp('UnitraccImage', 'base_edit')

    def addBinary(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccBinary')
        return self.temp('UnitraccBinary', 'base_edit')

    def addAnimation(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccAnimation')
        return self.temp('UnitraccAnimation', 'base_edit')

    def addAudio(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccAudio')
        return self.temp('UnitraccAudio', 'base_edit')

    def addVideo(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccVideo')
        return self.temp('UnitraccVideo', 'base_edit')

    def addFormula(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccFormula')

        return self.temp('UnitraccFormula', 'base_edit')

    def addStandard(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccStandard')
        return self.temp('UnitraccStandard', 'base_edit')

    def addGlossary(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccGlossary')
        return self.temp('UnitraccGlossary', 'base_edit')

    def addArticle(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccArticle')
        return self.temp('UnitraccArticle', 'base_edit')

    def addNews(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccNews')
        return self.temp('UnitraccNews', 'base_edit')

    def addEvent(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccEvent')
        return self.temp('UnitraccEvent', 'base_edit')

    def addTable(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccTable')
        return self.temp('UnitraccTable', 'base_edit')

    def addCourse(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccCourse')
        return self.temp('UnitraccCourse', 'base_edit')

    def addLiterature(self):
        """ """
        context = self.getTempFolder()
        context.getAdapter('authorized')('unitracc: Add UnitraccLiterature')
        return self.temp('UnitraccLiterature', 'base_edit')

    def addTechnicalInformation(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getTechnicalInformationFolder()
        return self._addStructure(folder, 'technical_information_view')

    def addInstructions(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getInstructionsFolder()
        return self._addStructure(folder, 'instructions_view')

    def addDocumentation(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getDocumentationFolder()
        return self._addStructure(folder, 'documentation_view')

    def addPaper(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getPaperFolder()
        return self._addStructure(folder, 'paper_view')

    def addPresentation(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')
        folder = storagefolder.getPresentationFolder()
        return self._addStructure(folder, 'presentation_view', False)

    def _addStructure(self, folder, templateId, isBook=True):

        context = self.context
        context.getAdapter('authorized')('unitracc: Add structure types')

        message = context.getAdapter('message')
        request = context.REQUEST
        form = request.form
        response = request.RESPONSE
        unitraccgroups = context.getBrowser('unitraccgroups')
        groups = context.getBrowser('groups')

        code = context.getBrowser('industrialsector').buildDomainFromRequest()

        if not form.get('title') or not form.get('language') or not code:
            message('Please fill all required fields.')
            return response.redirect(request['HTTP_REFERER'])

        createObject = folder.getAdapter('createobject')

        object_ = createObject('Folder', form.get('title'))

        object_.setLanguage(form.get('language'))
        object_.setLayout(templateId)
        object_.setCode(code)
        object_.processForm()

        if isBook:
            object_.getBrowser('book').addPortlets()

        object_.getBrowser('workflow').change('make_private')

        for prefix in unitraccgroups.getStructureGroupPrefixes():
            parentGroupId = unitraccgroups.buildStructureGroupName(folder.UID(), prefix)
            if not groups.getById(parentGroupId):
                groups.add(parentGroupId, folder.Title() + ' ' + prefix)

            groupId = unitraccgroups.buildStructureGroupName(object_.UID(), prefix)
            group = groups.add(groupId, object_.Title() + ' ' + prefix)
            group.addMember(unitraccgroups.buildStructureGroupName(object_.aq_parent.UID(), prefix))
            object_.manage_setLocalRoles(groupId, [prefix])
        object_.reindexObjectSecurity()

        message('Changes saved.')

        return response.redirect(merge_qvars(object_.absolute_url(),
                                             [('set_language', form.get('language')),
                                              ]))

    def addVirtualConstruction(self):
        """ """
        pass

    def authAdd(self):
        """ """
        context = self.context
        authorized = context.getAdapter('authorized')
        authorized('unitracc: Add to temp')
        authorized('unitracc: Add structure types')

    def copyPresentation(self):  # --------------- [ copyPresentation ... [
        """ """
        context = self.context
        request = context.REQUEST
        getAdapter = context.getAdapter
        getBrowser = context.getBrowser

        getAdapter('authorized')('unitracc: Copy structure types')

        back2 = tryagain_url(request,
                             ['copyFrom',
                              'title',
                              'language',
                              'user_id',
                              ])
        if self._validateStructureSettings():
            return request.RESPONSE.redirect(back2)
            return request.RESPONSE.redirect(request['HTTP_REFERER'])
        COPYID = copyid()

        rc = getAdapter('rc')()
        pc = getAdapter('pc')()
        unitraccgroups = getBrowser('unitraccgroups')
        groups = getBrowser('groups')
        message = getAdapter('message')
        form = request.form
        relationship = 'presentation-comment'  # ???

        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')
        user_id = form.get('user_id')

        if not uid or not title or not language or not user_id:
            message('Please fill all required fields.')
            return request.RESPONSE.redirect(back2)
            return request.RESPONSE.redirect(request['HTTP_REFERER'])

        # ---------------------------------------- ... copyPresentation ...
        folder = rc.lookupObject(uid)
        parent = folder.aq_parent
        INFO = {'COPYID': COPYID,
                'title_orig': folder.Title(),
                'id_orig': folder.getId(),
                }
        INFO.update(form)
        for txt in (
                '[ Start [',
                ' title (original): %(title_orig)s',
                ' id (original):    %(id_orig)s',
                ' uid (original):   %(copyFrom)s',
                ' title of copy:    %(title)s',
                ' type of copy:     %(copyType)s',
                ' owner of copy:    %(user_id)s',
                ' language of copy: %(language)s',
                ):
            copylog.info('%(COPYID)s ' + txt, INFO)

        transaction.begin()
        # Root Folder
        copylog.info('%(COPYID)s  { raw copy of folder %(id_orig)s ...', INFO)
        cp = parent.manage_copyObjects(ids=[folder.getId()])
        copylog.info('%(COPYID)s   } ... raw copy of folder %(id_orig)s', INFO)
        # SubFolder und Seiten
        copylog.debug("Copy Subfolders: " + ",".join(folder.getId()))
        copylog.info('%(COPYID)s  { pasting copy ...', INFO)
        ids = parent.manage_pasteObjects(cb_copy_data=cp)
        INFO['pasted_ids'] = ids
        copylog.info('%(COPYID)s    copy pasted (%(pasted_ids)s) ...', INFO)
        transaction.savepoint()
        copylog.info('%(COPYID)s   } pasted copy committed', INFO)

        INFO['new_id'] = ids[0]['new_id']
        rootNew = parent[INFO['new_id']]
        INFO['old_id'] = ids[0]['id']
        rootOld = parent[INFO['old_id']]
        INFO['new_uid'] = rootNew.UID()

        copylog.info('%(COPYID)s  old id: %(old_id)s', INFO)
        copylog.info('%(COPYID)s  new id: %(new_id)s', INFO)

        #Rename
        copylog.info('%(COPYID)s  setting title to %(title)s', INFO)
        rootNew.setTitle(title)
        newId = rootNew._renameAfterCreation()
        INFO['new_id'] = newId
        copylog.info('%(COPYID)s  changed new id to %(new_id)s', INFO)
        transaction.savepoint()
        rootNew = parent[newId]

        # ---------------------------------------- ... copyPresentation ...
        # wichtig für die Suche:
        # XXX erstmal auskommentiert, um Wichtigkeit zu untersuchen!
        copylog.info('%(COPYID)s  { reindex new object ...', INFO)
        rootNew.reindexObject()
        copylog.info('%(COPYID)s   } ... reindex new object', INFO)

        query = {}
        query['Language'] = 'all'
        query['path'] = rootOld.getPath()

        query = {}
        query['Language'] = 'all'
        query['path'] = rootNew.getPath()

        copylog.info('%(COPYID)s  { make private (and set language to %(language)s) ...', INFO)
        made_private = 0
        #Set language and make private
        for brain in pc(query):
            object_ = brain._unrestrictedGetObject()
            object_.setLanguage(language)
            object_.getBrowser('workflow').change('make_private')
            made_private += 1
        INFO['made_private'] = made_private
        copylog.info('%(COPYID)s   } ... %(made_private)d objects made private', INFO)
        INFO['parent_uid'] = rootNew.aq_parent.UID()

        # neue Gruppen anlegen für das Element
        for prefix in unitraccgroups.getStructureGroupPrefixes():
            groupId = unitraccgroups.buildStructureGroupName(rootNew.UID(), prefix)
            groupTitle = rootNew.Title() + ' ' + prefix
            copylog.info('%(COPYID)s  { new group %(groupId)s: %(groupTitle)s ...', locals())
            group = groups.add(groupId, groupTitle)
            copylog.info('%(COPYID)s    ... group created ...', INFO)
            # wer alle Vorträge lesen darf (Reader-Gruppe des Elternelements),
            # darf auch diesen lesen; also ist die übergeordnete Reader-Gruppe
            # auch lokaler Reader (und entsprechend)
            parent_groupId = unitraccgroups.buildStructureGroupName(INFO['parent_uid'], prefix)
            group.addMember(parent_groupId)
            copylog.info('%(COPYID)s    added member: %(parent_groupId)s', locals())
            if prefix == 'Author':
                group.addMember(INFO['user_id'])
                copylog.info('%(COPYID)s    added member: %(user_id)s', INFO)
            rootNew.manage_setLocalRoles(groupId, [prefix])
            copylog.info('%(COPYID)s   } new group %(groupId)s has local %(prefix)r role', locals())
        # ---------------------------------------- ... copyPresentation ...
        try:
            changeowner = rootNew.getBrowser('changeowner')
            copylog.info('%(COPYID)s   Changing ownership ...', INFO)
            changeowner.set(INFO['user_id'], recursive=0)
            copylog.info('%(COPYID)s   Owner of copy is %(user_id)s', INFO)
        except Exception, e:
            copylog.error('%(COPYID)s   Change of ownership for copy failed!', INFO)
            copylog.exception(e)

        copylog.info('%(COPYID)s   reindexObjectSecurity ...', INFO)
        rootNew.reindexObjectSecurity()
        copylog.info('%(COPYID)s   ... reindexObjectSecurity', INFO)

        rootNew.setCopyFrom(uid)
        transaction.commit()

        copylog.info('%(COPYID)s   _copyExternalContent(%(new_uid)s) ...', INFO)
        rootNew.getBrowser('copystructure')._copyExternalContent(rootNew.UID())
        copylog.info('%(COPYID)s   ... _copyExternalContent(%(new_uid)s)', INFO)
        transaction.commit()
        copylog.info('%(COPYID)s   sending mail ...', INFO)
        self._mailCopySuccess(INFO)
        copylog.info('%(COPYID)s   ... mail sent to %(mailsentto)s)', INFO)
        copylog.info('%(COPYID)s ] Done ]', INFO)
        message('Changes saved.')

        return request.RESPONSE.redirect(rootNew.absolute_url() + '?set_language=' + form.get('language'))
        # ---------------------------------------- ] ... copyPresentation ]

    def canAdd(self, portal_type):
        """
        Darf der angemeldete Benutzer den uebergebenen Typ im temp-Ordner hinzufuegen?
        """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add %s' % portal_type)

    def canAddCourse(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccCourse')

    def canAddArticle(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccArticle')

    def canAddNews(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccNews')

    def canAddEvent(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccEvent')

    def canAddImage(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccImage')

    def canAddBinary(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccBinary')

    def canAddAnimation(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccAnimation')

    def canAddAudio(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccAudio')

    def canAddVideo(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccVideo')

    def canAddGlossary(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccGlossary')

    def canAddLiterature(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccLiterature')

    def canAddFormula(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccFormula')

    def canAddStandard(self):
        """ """
        context = self.getTempFolder()
        return context.getAdapter('checkperm')('unitracc: Add UnitraccStandard')

    def getTranslatedSchemaLabel(self, fieldset):
        context = self.context
        translate = context.getAdapter('translate')
        label = "label_schema_unitracc_%s" % fieldset
        return translate(label)

    def canModifyObject(self, uid):
        """
        Checks, if user has the permission to modify the object with the specified UID
        """
        context = self.context

        rc = context.getAdapter('rc')()
        object_ = rc.lookupObject(uid)
        return object_.getAdapter('checkperm')('Modify portal content')

    def canDeleteObject(self, uid):
        """
        Checks, if user has the permission to delete the object with the specified UID
        """
        context = self.context

        rc = context.getAdapter('rc')()
        object_ = rc.lookupObject(uid)
        return object_.getAdapter('checkperm')('Delete objects')

    def copyTechnicalInformation(self):
        """ """
        context = self.context

        context.getAdapter('authorized')('unitracc: Manage structure types')

        message = context.getAdapter('message')
        form = context.REQUEST.form
        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')

        if self._validateStructureSettings():
            return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

        rootOld, rootNew = self._copyStructure(uid, title, language)
        rootNew.getBrowser('copystructure')._copyExternalContent(rootNew.UID())
        self._mailCopySuccess()

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(rootNew.absolute_url() + '?set_language=' + form.get('language'))

    def copyInstruction(self):
        """ """
        context = self.context

        context.getAdapter('authorized')('unitracc: Manage structure types')

        message = context.getAdapter('message')
        form = context.REQUEST.form
        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')

        if self._validateStructureSettings():
            return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

        rootOld, rootNew = self._copyStructure(uid, title, language)
        rootNew.getBrowser('copystructure')._copyExternalContent(rootNew.UID())
        self._mailCopySuccess()

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(rootNew.absolute_url() + '?set_language=' + form.get('language'))

    def copyDocumentation(self):
        """ """
        context = self.context

        context.getAdapter('authorized')('unitracc: Manage structure types')

        message = context.getAdapter('message')
        form = context.REQUEST.form
        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')

        if self._validateStructureSettings():
            return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

        rootOld, rootNew = self._copyStructure(uid, title, language)
        rootNew.getBrowser('copystructure')._copyExternalContent(rootNew.UID())
        self._mailCopySuccess()

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(rootNew.absolute_url() + '?set_language=' + form.get('language'))

    def copyPaper(self):
        """ """
        context = self.context

        context.getAdapter('authorized')('unitracc: Manage structure types')

        message = context.getAdapter('message')
        form = context.REQUEST.form
        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')

        if self._validateStructureSettings():
            return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

        rootOld, rootNew = self._copyStructure(uid, title, language)
        rootNew.getBrowser('copystructure')._copyExternalContent(rootNew.UID())
        self._mailCopySuccess()

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(rootNew.absolute_url() + '?set_language=' + form.get('language'))

    def _validateStructureSettings(self):
        """ """
        context = self.context
        message = context.getAdapter('message')
        form = context.REQUEST.form

        uid = form.get('copyFrom')
        title = form.get('title')
        language = form.get('language')

        if not uid or not title or not language:
            message('Please fill all required fields.')
            return True

        if form.get('copyType') == '2':
            if form.get('sourceLanguage')[-2:] == language:
                message('Source and target language cannot be the same if copy type is "create translation".', 'error')
                return True

    def _copyStructure(self, uid, title, language):
        """ """
        context = self.context
        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()
        unitraccgroups = context.getBrowser('unitraccgroups')
        groups = context.getBrowser('groups')

        folder = rc.lookupObject(uid)
        parent = folder.aq_parent

        cp = parent.manage_copyObjects(ids=[folder.getId()])
        ids = parent.manage_pasteObjects(cb_copy_data=cp)
        transaction.commit()

        rootNew = parent[ids[0]['new_id']]
        rootOld = parent[ids[0]['id']]

        objects = rootOld.getBrowser('stage').get('book-start-page')
        if objects:
            copyStartPage = rootNew[objects[0].getId()]
            rootNew.addReference(copyStartPage, 'book-start-page')
            rootNew.reindexObject()
            transaction.commit()

        objects = rootOld.getBrowser('stage').get('illustration')
        if objects:
            tempFolder = self.getTempFolder()
            parentIllustration = rc.lookupObject(objects[0].UID()).aq_parent
            cp = parentIllustration.manage_copyObjects(ids=[objects[0].getId()])
            ids = tempFolder.manage_pasteObjects(cb_copy_data=cp)
            copy_ = tempFolder[ids[0]['new_id']]
            copy_.setLanguage(rootNew.Language())
            copy_.reindexObject()
            transaction.commit()

        #Rename
        rootNew.setTitle(title)
        newId = rootNew._renameAfterCreation()
        transaction.commit()
        rootNew = parent[newId]

        for prefix in unitraccgroups.getStructureGroupPrefixes():
            groupId = unitraccgroups.buildStructureGroupName(rootNew.UID(), prefix)
            group = groups.add(groupId, rootNew.Title() + ' ' + prefix)
            group.addMember(unitraccgroups.buildStructureGroupName(rootNew.aq_parent.UID(), prefix))
            rootNew.manage_setLocalRoles(groupId, [prefix])
        rootNew.reindexObjectSecurity()

        query = {}
        query['Language'] = 'all'
        query['path'] = rootNew.getPath()

        #Set language
        for brain in pc(query):
            object_ = brain._unrestrictedGetObject()
            object_.setLanguage(language)
            object_.getBrowser('workflow').change('make_private')

        rootNew.setCopyFrom(uid)
        transaction.commit()
        return rootOld, rootNew

    def cleanupTemp(self):
        """ """
        context = self.context

        context.getAdapter('authorized')('unitracc: Manage structure types')

        message = context.getAdapter('message')
        getbrain = context.getAdapter('getbrain')
        folder = self.getTempFolder()

        for id, object_ in folder.objectItems():
            if object_._isIDAutoGenerated(id):
                if not getbrain(object_.UID()):
                    if object_.created() < (DateTime() - 7):
                        object_.getBrowser('unlock').unlock(redirect=False)
                        folder.manage_delObjects(ids=[object_.getId()])
                        transaction.commit()

        message('Changes saved.')
        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def _mailCopySuccess(self, infodict=None):
        """ """
        context = self.context
        member = context.getAdapter('auth')()
        portal = context.getAdapter('portal')()

        email = member.getProperty('email')
        if email:
            mail = context.getBrowser('unitraccmail')
            subject = 'Kopiervorgang erfolgreich abgeschlossen.'
            mail.set('utf-8', 'mail_copy_success', subject)
            mail.renderAsPlainText()
            mail.sendMail(portal.email_from_address, email)
            if infodict:
                infodict['mailsentto'] = email
        elif infodict:
            infodict['mailsentto'] = None

    def publishStructure(self):
        """
        Veröffentliche das per Formular angegebene Strukturelement.

        Ersetzt die bisherigen (jeweils identischen!) Methoden
        publishDocumentation, publishInstruction, publishPaper,
        publishPresentation und publishTechnicalInformation.
        Es wird weiterhin für die eigentliche Arbeit _publish
        aufgerufen.
        """
        context = self.context
        message = context.getAdapter('message')

        context.getAdapter('authorized')('unitracc: Manage structure types')

        published = self._publish()

        message('Changes saved.')
        request = context.REQUEST
        redirect = request.RESPONSE.redirect

        if request.form.get('redirect_to') == 'changed':
            to_path = published.getPath()
            return redirect(tryagain_url(request, path=to_path))
        return redirect(tryagain_url(request))

    def _publish(self):
        """
        veröffentliche das per UID angegebene Strukturelement.

        Formulardaten:
        uid -- die UID
        transition -- Veröffentlichungsaktion ('make_inherit' o.ä.)
        include_references -- für verwendete Objekte

        Nota bene:
        - 'make_inherit' wird evtl. auf Manager eingeschränkt
        - 
        """

        context = self.context
        request = context.REQUEST
        form = request.form

        uid = form.get('uid')
        if not uid:
            message = context.getAdapter('message')
            _ = context.getAdapter('translate')
            message(_('No folder given'),
                    'error')
            return request.RESPONSE.redirect(tryagain_url(
                request,
                ('uid', 'include_references', 'transition')))

        transition = form.get('transition')
        include_references = form.get('include_references')
        self._include_all_references =  include_references == 'all'
        self._include_temp_references = include_references == 'temp'
        self._moved = {}
        self._processed = {}
        rc = context.getAdapter('rc')()

        folder = rc.lookupObject(uid)
        if folder is None:
            message = context.getAdapter('message')
            _ = context.getAdapter('translate')
            message(_('Element %(uid)s not found') % locals(),
                    'error')
            return request.RESPONSE.redirect(tryagain_url(
                request,
                ('uid', 'include_references', 'transition')))

        query = {}
        query['Language'] = 'all'
        query['path'] = folder.getPath()
        query['sort_on'] = 'created'

        pc = context.getAdapter('pc')()
        pw = context.getAdapter('pw')()
        et = pw.dayta_workflow._executeTransition
        make_inherit = pw.dayta_workflow.transitions['make_inherit']
        make_specified = pw.dayta_workflow.transitions[transition]

        for brain in pc(query):
            page = brain.getObject()
            self._publishRelated(page, transition)
            et(page, make_inherit)
            page.reindexObject()

        et(folder, make_specified)
        folder.reindexObjectSecurity()
        folder.reindexObject()
        return folder

    def _publishRelated(self, object_, transition):
        """
        TODO:
        - Referenzkatalog verwenden
          - als Ersatz für copystructure._extractLinks
          - zum Schutz von Objekten, die auch anderweitig verwendet werden
        """
        context = self.context
        mediathek = context.getBrowser('mediathek')
        pw = context.getAdapter('pw')()
        copystructure = object_.getBrowser('copystructure')
        tempFolder = self.getTempFolder()

        for field in object_.schema.fields():
            if field.__dict__['type'] == 'text':
                text = field.get(object_)
                if text:
                    info = copystructure._extractLinks(text)
                    for dict_ in info:
                        o = dict_['object_']
                        uid = dict_['uid']
                        # process referenced objects, which are in /temp folder

                        if self._include_temp_references \
                           and o.aq_parent == tempFolder \
                           and not self._moved.has_key(uid):

                            pw.dayta_workflow._executeTransition(o, pw.dayta_workflow.transitions[transition])
                            mediathek.move(o)
                            self._moved[uid] = 1
                            self._processed[uid] = 1
                            self._publishRelated(o, transition)

                        # process all referenced objects

                        if self._include_all_references \
                           and o.portal_type not in ['Document', 'Folder'] \
                           and not self._processed.has_key(uid):

                            pw.dayta_workflow._executeTransition(o, pw.dayta_workflow.transitions[transition])
                            self._processed[uid] = 1
                            o.reindexObject()
                            self._publishRelated(o, transition)

    def deletePrivateStructure(self):
        """ """
        context = self.context
        message = context.getAdapter('message')

        context.getAdapter('authorized')('unitracc: Delete structure types')

        self._delete()

        message('Changes saved.')
        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def move(self, _object):
        """
        Moves an object back from mediathek to temp folder.
        """
        # Check if we are not inside temp folder
        if not _object.isTemporary():
            rc = self.context.getAdapter('rc')()
            portal = self.context.getAdapter('portal')()
            _object.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
            # get parent and temp folder
            parent = _object.aq_parent
            target = self.getTempFolder()
            # cut and paste into temp dir
            cp = parent.manage_cutObjects([_object.getId()])
            target.manage_pasteObjects(cp)

            _object = rc.lookupObject(_object.UID())
            _object.reindexObject()
            transaction.commit()
            #return self.context.REQUEST.RESPONSE.redirect(portal.absolute_url() + "/temp/" + _object.getId())

    def _delete(self):
        """
        LÖSCHE das per uid angegebene Strukturelement und je nach Wert des
        Formularfelds include_references)
        - alle referenzierten Objekte oder
        - nur die im temp-Ordner
        """

        context = self.context
        form = context.REQUEST.form
        uid = form.get('uid')
        transition = form.get('transition')
        self._include_all_references = (form.get('include_references') == 'all')
        self._include_temp_references = (form.get('include_references') == 'temp')
        self._delete = {}
        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()
        pw = context.getAdapter('pw')()

        form.update({'delete_all': 1})

        folder = rc.lookupObject(uid)
        folder.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
        parent = folder.aq_parent
        query = {}
        query['Language'] = 'all'
        query['path'] = folder.getPath()
        query['sort_on'] = 'created'

        for brain in pc(query):
            object_ = brain.getObject()
            if object_:
                self._deleteRelated(object_)

        parent.manage_delObjects(ids=[folder.getId()])

        self._deleteStructureGroups(folder)

    def _deleteRelated(self, object_):
        """
        LÖSCHE die referenzierten Objekte: alle oder die im temp-Ordner

        TODO:
        - Referenzkatalog verwenden
          - als Ersatz für copystructure._extractLinks
          - zum Schutz von Objekten, die auch anderweitig verwendet werden
        - Objekt zum Sammeln von Informationen:
          - welche UIDs sind schon erledigt?
        """
        context = self.context
        mediathek = context.getBrowser('mediathek')
        pw = context.getAdapter('pw')()
        copystructure = object_.getBrowser('copystructure')

        tempFolder = self.getTempFolder()

        for field in object_.schema.fields():
            if field.__dict__['type'] == 'text':
                text = field.get(object_)
                if text:
                    info = copystructure._extractLinks(text)
                    for dict_ in info:
                        o = dict_['object_']
                        uid = dict_['uid']
                        #only do this vor objects wich are in tempFolder
                        if (self._include_temp_references
                            and o.aq_parent == tempFolder
                            and not self._delete.has_key(uid)
                            ):
                            self._delete[uid] = 1
                            self._deleteRelated(o)
                            parent = o.aq_parent
                            parent.manage_delObjects(ids=[o.getId()])

                        if (self._include_all_references
                            and not self._delete.has_key(uid)
                            ):
                            self._delete[uid] = 1
                            self._deleteRelated(o)
                            parent = o.aq_parent
                            parent.manage_delObjects(ids=[o.getId()])

    def _deleteStructureGroups(self, folder):
        """
        Deletes Reader- and Author-Group for specified structure folder
        @param folder
                The folder to delete the groups for
        """
        context = self.context

        if folder and hasattr(folder, "UID"):
            unitraccgroups = context.getBrowser('unitraccgroups')
            groups = context.getBrowser('groups')
            # Retrieve groupId for Reader and Author Group and remove both
            for prefix in unitraccgroups.getStructureGroupPrefixes():
                groupId = unitraccgroups.buildStructureGroupName(folder.UID(), prefix)
                groups.delete(groupId)

    def setStructureGroups(self):
        """
        Iteriere über alle Objekte unter dem per UID angegebenen Ordner:
        - verschiebe die Medienobjekte in den Temp-Ordner
        - weise die korrekte Gruppe zu (--> _setStructureGroupsRelated)
        """
        context = self.context
        getAdapter = context.getAdapter

        getAdapter('authorized')('unitracc: Manage structure types')

        message = getAdapter('message')
        form = context.REQUEST.form
        uid = form.get('uid')
        transition = form.get('transition')
        failures = []
        infolist = []

        rc = getAdapter('rc')()
        folder = rc.lookupObject(uid)

        self._setStructureGroups(folder, transition, failures, infolist)
        if failures:
            pages = "\n".join(failures)
            message("Fehler bei Validierung. Folgende Seiten sind defekt: \n%s" % pages, "Error")

            return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

        _ = getAdapter('translate')
        vinfo = 'structure'
        if infolist:
            message('\n'.join([_('%s validated:') % (vinfo,)] +
                              infolist))
        else:
            message(_('Validation of %s: nothing to do; error?'
                      ) % (vinfo,),
                    'warning')
        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def _setStructureGroups(self, folder, transition, failures, infolist, logger=logger):
        # pp(**locals())
        context = self.context
        getAdapter = context.getAdapter

        self._moved = {}  # verschobene Objekte merken
        pc = context.getAdapter('pc')()
        pw = context.getAdapter('pw')()
        book = context.getBrowser('book')
        tempFolder = self.getTempFolder()

        unitraccgroups = context.getBrowser('unitraccgroups')
        self.editorGroups = {}
        for prefix in unitraccgroups.getStructureGroupPrefixes():
            groupId = unitraccgroups.buildStructureGroupName(folder.UID(), prefix)
            self.editorGroups[prefix] = groupId

        query = {}
        query['Language'] = 'all'
        query['path'] = folder.getPath()
        query['sort_on'] = 'created'

        isBookType = False
        isPresentation = False

        # Check if folder is presentation root folder
        if folder.getLayout() == 'presentation_view':
            isPresentation = True
            stype = 'presentation'
        # Check if folder is book type root folder (book, instruction, dokumentation, paper/lecture notes)
        elif folder.getLayout() in book.getBookTemplates():
            isBookType = True
            stype = 'book'
        else:
            stype = 'structure'
        try:
            vinfo = ('"%s" (%s)' %
                     (folder.title_or_id(), query['path']))
        except:
            vinfo = ('s %s' %
                     (query['path']))
        logger.info('[ validation of %s %s ... [', stype, vinfo)
        self.cnt = Counter()
        # --------------- [ iteriere über alle Objekte unter folder.getPath() ... [
        for brain in pc(query):
            object_ = brain.getObject()

            if transition:
                workflow = object_.getBrowser('workflow')
                workflow.change(transition)

            if object_.portal_type not in ['Document', 'Folder']:
                # solche Sachen gehoeren nicht in die Struktur, sondern
                # (ueber temp) in die Mediathek, also nach temp
                # verschieben:
                object_.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
                cp = object_.aq_parent.manage_cutObjects(ids=[object_.getId()])
                tempFolder.manage_pasteObjects(cb_copy_data=cp)
                transaction.commit()
                self.cnt['moved-to-tmp'] += 1
            elif object_.portal_type == 'Folder':
                if object_.UID() != folder.UID():
                    object_.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)

                    if isBookType:
                        # Object is book type subfolder. Switch to book_agenda_view layout if it has
                        # accidently book type root folder layout
                        if object_.getLayout() in book.getBookTemplates():
                            object_.setLayout('book_agenda_view')
                    elif isPresentation:
                        # Object is presentation subfolder. Switch to folder_listing layout if it has
                        # accidently presentation root folder layout
                        if object_.getLayout() == 'presentation_view':
                            object_.setLayout('folder_listing')

                if object_.reindexObject():  # Fehler beim Validieren
                    failures.append("Titel: %s URL: %s/%s/edit" % (object_.Title(),
                                                            context.absolute_url(),
                                                            object_.getPath()))

            if self._setStructureGroupsRelated(object_):
                failures.append("Titel: %s URL: %s/%s/edit" % (object_.Title(),
                                                            context.absolute_url(),
                                                            object_.getPath()))
        # --------------- ] ... iteriere über alle Objekte unter folder.getPath() ]

        if failures:
            return

        for brain in pc(query):
            object_ = brain.getObject()
            self._setStructureGroupsRelated(object_)

        translate = context.getAdapter('translate')
        cnt = self.cnt

        def tell(nn, txt):
            if nn:
                infolist.append(translate(txt) % nn)
                logger.info(' ::: %s' % (txt % nn))
        # absichtlich translate_dummy verwenden; Uebersetzung erst bei Verwendung:
        tell(cnt['scanned-objects'], _('%d objects scanned'))
        tell(cnt['scanned-textfields'], _('%d textfields scanned'))
        tell(cnt['processed-objects'], _('%d objects processed'))
        tell(cnt['skipped-objects'], _('%d ordinary pages skipped'))
        tell(cnt['refered-more-than-once'], _('%d reference repetitions'))
        tell(cnt['moved-to-tmp'], _('%d misplaced objects moved to temp folder'))
        logger.info(' ] ... validation of %s %s: done ]', stype, vinfo)

    def _setStructureGroupsRelated(self, object_, level=0):
        """
        rekursive Verarbeitung aller verknuepften Objekte, die keine
        Inhaltsseiten des Strukturelements sind, und die nicht schon
        verarbeitet wurden:
        Lies alle Textfelder aus, durchsuche sie nach Links und
        verarbeite alle verlinkten Objekte

        TODO:
        - Referenzkatalog verwenden
          - als Ersatz für copystructure._extractLinks
          - zum Schutz von Objekten, die auch anderweitig verwendet werden
        """

        context = self.context
        copystructure = object_.getBrowser('copystructure')
        uid = copystructure._uid = object_.UID()
        tempFolder = self.getTempFolder()
        self.cnt['scanned-objects'] += 1
        scanned_objects = self.cnt['scanned-objects']
        space = level * ' '
        logger.info('_setStructureGroupsRelated: %(space)s%(scanned_objects)d. (%(uid)s)',
                    locals())

        for field in object_.schema.fields():
            if field.__dict__['type'] == 'text':
                self.cnt['scanned-textfields'] += 1
                text = field.get(object_)
                if text:
                    try:
                        info = copystructure._extractLinks(text)
                    except Exception as e:
                        logger.error('Fehler bei Extraktion der Links aus %(field)r! (%(e)r)',
                                     locals())
                        logger.exception(e)
                        return 1
                    for dict_ in info:
                        obj = dict_['object_']
                        ouid = obj.UID()
                        if self._moved.has_key(ouid):
                            self.cnt['refered-more-than-once'] += 1
                            continue        # schon erledigt
                        #Es werden alle Objekte beruecksichtigt, die nicht in einem
                        #Strukturelement selber liegen.
                        # (TH: bei denen werden die entsprechenden Rollen akquiriert)
                        book = obj.getBrowser('book')
                        if book.isBookPage():
                            self.cnt['skipped-objects'] += 1
                            continue
                        presentation = obj.getBrowser('presentation')
                        if presentation.isPresentationPage():
                            self.cnt['skipped-objects'] += 1
                            continue
                        self.cnt['processed-objects'] += 1
                        for prefix, groupId in self.editorGroups.items():
                            done = False
                            if prefix == 'Author':
                                try:
                                    obj.addUnitraccGroups([groupId])
                                    logger.info('%(obj)r.addUnitraccGroups([%(groupId)r]): OK',
                                                 locals())
                                    done = True
                                except AttributeError as e:
                                    logger.error('%(obj)r.addUnitraccGroups([%(groupId)r])',
                                                 locals())
                            if not done:
                                obj.manage_setLocalRoles(groupId, [prefix])
                        obj.reindexObjectSecurity()
                        # Änderungen vorgenommen; jetzt vor
                        # Rekursion Doppelausführung vermeiden:
                        self._moved[ouid] = 1
                        self._setStructureGroupsRelated(obj)
        return 0

    def setSubportal(self):
        """
            Setze die Subportale für die Strukturelemente
        """

        context = self.context
        context.getAdapter('authorized')('unitracc: Manage structure types')
        message = context.getAdapter('message')

        self._setSubportal()

        message("Changes Saved.")

        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def _setSubportal(self):
        """Setze Subportal für einzelnes Element"""
        context = self.context
        form = context.REQUEST.form
        uid = form.get('uid')
        self._processed = {}
        pc = context.getAdapter('pc')()
        rc = context.getAdapter('rc')()
        default_portal = context.getBrowser('subportal').get()['default_uid']
        self._include_all_references = (form.get('include_references') == 'all')
        self._include_temp_references = (form.get('include_references') == 'temp')
        self._subportals = [default_portal]
        if form.get('subportals'):
            self._subportals.append(form.get('subportals'))

        folder = rc.lookupObject(uid)
        query = {}
        query['Language'] = 'all'
        query['path'] = folder.getPath()
        query['sort_on'] = 'created'

        for brain in pc(query):
            page = brain.getObject()
            self._setSubportalRelated(page)
        return 0

    def _setSubportalRelated(self, object_):
        """
            Setze Subportal für related Content

        TODO:
        - Referenzkatalog verwenden
          - als Ersatz für copystructure._extractLinks
          - zum Schutz von Objekten, die auch anderweitig verwendet werden
        """
        context = self.context
        mediathek = context.getBrowser('mediathek')
        pw = context.getAdapter('pw')()
        copystructure = object_.getBrowser('copystructure')
        tempFolder = self.getTempFolder()
        for field in object_.schema.fields():
            if field.__dict__['type'] == 'text':
                text = field.get(object_)
                if text:
                    info = copystructure._extractLinks(text)
                    # Externe Inhalte
                    for dict_ in info:
                        o = dict_['object_']
                        uid = dict_['uid']
                        # Nur Temp
                        if (self._include_temp_references
                            and o.aq_parent == tempFolder
                            ):
                            o.setSubPortals(self._subportals)
                            self._processed[uid] = 1

                        # Alle Inhalte
                        if (self._include_all_references
                            and o.portal_type not in ['Document', 'Folder']
                            and not self._processed.has_key(uid)
                            ):
                            o.setSubPortals(self._subportals)
                            self._processed[uid] = 1

        object_.setSubPortals(self._subportals)
        object_.reindexObject()

# vim: ts=8 sts=4 sw=4 si et hls
