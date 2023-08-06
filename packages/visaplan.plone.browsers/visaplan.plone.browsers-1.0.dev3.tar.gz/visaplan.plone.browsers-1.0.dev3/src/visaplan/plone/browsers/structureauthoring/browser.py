# -*- coding: utf-8 -*- äöü
# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface
import transaction

# Unitracc-Tools:
from visaplan.tools.coding import safe_decode
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.debug import log_or_trace

# Logging und Debugging:
from pprint import pformat
logger, debug_active, DEBUG = getLogSupport()
lot_kwargs = {'debug_level': int(debug_active),
              'logger': logger,
	      }

# -------------------------------------------------- [ Interface ... [
class IStructureAuthoring(Interface):

    def addSlideBefore(self):
        """ """

    def delete(self):
        """ """

    def save(self):
        """ """

    def addSlideAfter(self):
        """ """

    def addPresentationFolderBefore(self):
        """ """

    def addPresentationFolderAfter(self):
        """ """

    def cut(self):
        """ """

    def copy(self):
        """ """

    def titleMappingByUid(self):
        """ """

    def pasteBefore(self):
        """ """

    def pasteAfter(self):
        """ """

    def edit(self):
        """ """

    def canAddSlideInPresentation(self):
        """ """

    def canAddFolderInPresentation(self):
        """ """

    def addStructureFolder(self):
        """ """

    def canCopyMoveDelete(self):
        """ """

    def addSlide(self):
        """ """

    def canAddSlideForPresentation(self):
        """ """

    def canAddFolderForPresentation(self):
        """ """

    def addPresentationFolder(self):
        """ """

    def canPasteInFolder(self):
        """ """

    def pasteInFolder(self):
        """ """

    def getDefaultView(self):
        """ """

    def canAddFolderForStructure(self):
        """ """

    def canAddFolderInStructure(self):
        """ """

    def addStructureFolderBefore(self):
        """ """

    def addStructureFolderAfter(self):
        """ """

    def getPresentationLevel(self):
        """ """

    def canAddPageInStructure(self):
        """ """

    def addPageBefore(self):
        """ """

    def addSlide(self):
        """ """

    def addPageAfter(self):
        """ """

    def canAddPageForStructure(self):
        """ """

    def addPage(self):
        """ """

    def setAgendaView(self):
        """ """

    def canSetAgendaView(self):
        """ """

    def setDefaultPage(self):
        """ """

    def canSetDefaultPage(self):
        """ """

    def editFolder(self):
        """ """

    def cancel(self):
        """ """
# -------------------------------------------------- ] ... Interface ]

class Browser(BrowserView):


    implements(IStructureAuthoring)

    @log_or_trace(debug_active, logger=logger, log_result=0)
    def getPresentationLevel(self, uid):

        context = self.context
        getbrain = context.getAdapter('getbrain')
        tree = context.getBrowser('tree')
        brain = getbrain(uid)
        # XXX An dieser Stelle tritt manchmal ein Fehler auf, weil offenbar getbrain None ergibt! 
        if brain is None:
            request = context.REQUEST
            referer = request['HTTP_REFERER']
            form = pformat(dict(request.form))
            logger.error('getPresentationLevel(%(uid)r): nichts gefunden!'
                         '\n  referer=%(referer)r'
                         '\n  form=%(form)s',
                         locals())
            # TODO: weiteres Vorgehen? Kann mit dem Fehler sinnvoll verfahren werden?

        return tree.getLevel(brain)

    def authAddSlide(self):
        """ """
        context = self.context
        context.getAdapter('authorized')('unitracc: Add UnitraccSlide')

    def authAddPresentationFolder(self):
        """ """
        context = self.context
        context.getAdapter('authorized')('unitracc: Add UnitraccPresentationFolder')

    def authAddStructureFolder(self):
        """ """
        context = self.context
        context.getAdapter('authorized')('unitracc: Add UnitraccStructureFolder')

    def addPageBefore(self):
        """ """
        return self._addSlide('-')

    def addPage(self):
        """ """
        return self.addSlide()

    def addSlide(self):
        """ """
        context = self.getContext()

        self.authAddSlide()

        pu = context.getAdapter('pu')()
        object_ = self._temp('Document', context)
        return object_.restrictedTraverse('kss-slide-edit')()

    def addPageAfter(self):
        """ """
        return self._addSlide('+')


    def addSlideBefore(self):
        """ """
        return self._addSlide('-')

    def addSlide(self):
        """ """
        context = self.getContext()

        self.authAddSlide()

        pu = context.getAdapter('pu')()
        object_ = self._temp('Document', context)
        return object_.restrictedTraverse('kss-slide-edit')()

    def addSlideAfter(self):
        """ """
        return self._addSlide('+')

    def _addSlide(self, operator):
        """
        Erzeuge eine neue Folie

        operator -- wenn '+', wird nach dem aktuellen Element eingefuegt.
                    Etwaige andere Werte werden ignoriert.
        """

        context = self.getContext()

        self.authAddSlide()

        parent = context.aq_parent
        pu = context.getAdapter('pu')()
        form = context.REQUEST.form

        counter = 0

        for id in parent.objectIds():
            parent.moveObject(id, counter)
            counter+=1

        object_ = self._temp('Document')

        position = parent.getObjectPosition(context.getId())

        if operator == '+':
            position += 1

        parent.moveObject(object_.getId(), position)
        pu.reindexOnReorder(parent)

        return object_.restrictedTraverse('kss-slide-edit')()

    def addPresentationFolderBefore(self):
        """ """
        return self._addPresentationFolder('-')

    def addPresentationFolderAfter(self):
        """ """
        return self._addPresentationFolder('+')

    def addStructureFolderBefore(self):
        """ """
        return self._addStructureFolder('-')

    def addStructureFolderAfter(self):
        """ """
        return self._addStructureFolder('+')

    def addStructureFolder(self):
        """ """
        context=self.getContext()

        self.authAddPresentationFolder()

        pu = context.getAdapter('pu')()
        object_ = self._temp('Folder', context)
        object_.setLayout('book_agenda_view')
        object_.getAdapter('notifyedit')()
        object_.reindexObject()
        return object_.restrictedTraverse('kss-structure-folder-edit')()

    def addPresentationFolder(self):
        """ """
        context = self.getContext()

        self.authAddPresentationFolder()

        pu = context.getAdapter('pu')()
        object_ = self._temp('Folder', context)
        return object_.restrictedTraverse('kss-structure-folder-edit')()

    def _addStructureFolder(self, operator):
        """
        Erzeuge einen neuen Ordner

        operator -- wenn '+', wird nach dem aktuellen Element eingefuegt.
                    Etwaige andere Werte werden ignoriert.
        """

        context = self.getContext()

        self.authAddStructureFolder()

        parent = context.aq_parent
        pu = context.getAdapter('pu')()
        form = context.REQUEST.form

        counter = 0

        for id in parent.objectIds():
            parent.moveObject(id, counter)
            counter+=1

        object_ = self._temp('Folder')
        object_.setLayout('book_agenda_view')
        object_.getAdapter('notifyedit')()
        object_.reindexObject()
        position = parent.getObjectPosition(context.getId())

        if operator == '+':
            position += 1

        parent.moveObject(object_.getId(), position)
        pu.reindexOnReorder(parent)

        return object_.restrictedTraverse('kss-structure-folder-edit')()


    def _addPresentationFolder(self, operator):
        """
        Erzeuge einen neuen Vortragsordner

        operator -- wenn '+', wird nach dem aktuellen Element eingefuegt.
                    Etwaige andere Werte werden ignoriert.
        """

        context = self.getContext()

        self.authAddPresentationFolder()

        parent = context.aq_parent
        pu = context.getAdapter('pu')()
        form = context.REQUEST.form

        counter = 0

        for id in parent.objectIds():
            parent.moveObject(id, counter)
            counter+=1

        object_ = self._temp('Folder')

        position = parent.getObjectPosition(context.getId())

        if operator == '+':
            position += 1

        parent.moveObject(object_.getId(), position)
        pu.reindexOnReorder(parent)

        return object_.restrictedTraverse('kss-structure-folder-edit')()


    def _temp(self, portal_type, folder=None):
        context = self.getContext()

        userId = context.getAdapter('auth')().getId()

        portal = context.getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        form = context.REQUEST.form

        if not folder:
            folder = context.aq_parent

        createObject = folder.getAdapter('createobject')
        object_ = createObject(portal_type)

        changeowner = object_.getBrowser('changeowner')
        changeowner.set(userId)

        object_.getBrowser('workflow').change('make_private')

        object_.setCode(folder.getCode())
        object_.setLanguage(folder.Language())

        if portal_type == 'Folder':
            object_.setLayout('folder_listing')
            object_.getAdapter('notifyedit')()
            object_.reindexObject()


        sm.setOld()

        transaction.commit()

        return object_

    @log_or_trace(**lot_kwargs)
    def delete(self):
        """ """
        context = self.getContext()
        context.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
        parent = context.aq_parent
        _ = parent.getAdapter('translate')
        json = parent.getBrowser('json')
        title = safe_decode(context.Title())
        parent.manage_delObjects(ids=[context.getId()])

        dict_ = {}
        dict_['uid'] = parent.UID()
        dict_['message'] = _('"${title}" deleted.', mapping={'title': title})

        return json.encode(dict_)

    @log_or_trace(**lot_kwargs)
    def save(self):
        """
        Speichere die aktuellen Änderungen und gib eine UID zurück:
        - für Document-Objekte die des Objekts (die mutmaßlich schon in den
          Formulardaten übergeben wurde;
        - ansonsten die UID des Elternobjekts
        """
        context = self.context
        # DEBUG('%(context)r.save() ...', locals())
        form = context.REQUEST.form

        uid = form.get('uid', '')
        # DEBUG('uid=%(uid)r', locals())
        rc = context.getAdapter('rc')()

        context = rc.lookupObject(uid)
        # DEBUG('`-> neuer Kontext: %(context)r', locals())
        errors = {}
        # DEBUG('%(context)r.validate ...', locals())
        errors = context.validate(REQUEST=context.REQUEST, errors=errors, data=1, metadata=0)
        # DEBUG('%(context)r.processForm ...', locals())
        context.processForm()

        pt = context.portal_type
        if pt == 'Document':
            uid2 = context.UID()
        else:
            uid2 = context.aq_parent.UID()
        DEBUG('save(): pt=%(pt)r; uid=%(uid)r', locals())
        return uid2

    @log_or_trace(**lot_kwargs)
    def cut(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        _ = context.getAdapter('translate')
        json = context.getBrowser('json')

        uid = form.get('uid', '')
        rc = context.getAdapter('rc')()

        context = rc.lookupObject(uid)
        context.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
        parent = context.aq_parent
        dict_ = {}
        dict_['cp'] = parent.manage_cutObjects(ids=[context.getId()])
        dict_['message'] = _('"${title}" cutted.',
                             mapping={'title': safe_decode(context.Title()),
                                      })
        return json.encode(dict_)

    @log_or_trace(**lot_kwargs)
    def copy(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        _ = context.getAdapter('translate')
        json = context.getBrowser('json')

        uid = form.get('uid', '')
        rc = context.getAdapter('rc')()

        context = rc.lookupObject(uid)
        context.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
        parent = context.aq_parent
        dict_ = {}
        dict_['cp'] = parent.manage_copyObjects(ids=[context.getId()])
        dict_['message'] = _('"${title}" copied.',
                             mapping={'title': safe_decode(context.Title()),
                                      })

        return json.encode(dict_)

    def pasteBefore(self):
        """ """
        return self._paste('-')

    def pasteAfter(self):
        """ """
        return self._paste('+')

    def pasteInFolder(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        uid = form.get('uid')
        rc = context.getAdapter('rc')()
        object_ = rc.lookupObject(uid)

        return self._paste(None, object_)

    def _paste(self, operator, parent=None):
        """
        Fuege ein Element aus der Zope-Zwischenablage ein

        operator -- wenn '+', wird nach dem aktuellen Element eingefuegt.
                    Etwaige andere Werte werden ignoriert.
        """

        context = self.getContext()

        self.authAddPresentationFolder()

        pu = context.getAdapter('pu')()
        rc = context.getAdapter('rc')()
        portal = context.getAdapter('portal')()
        clipboard = context.getBrowser('clipboard')
        _ = context.getAdapter('translate')
        form = context.REQUEST.form
        json = context.getBrowser('json')


        cp = form.get('cp')
        uid = form.get('uid')

        object_ = rc.lookupObject(uid)
        if not parent:
            parent = object_.aq_parent

        cpReadable = clipboard._get_clipboard(cp, context.REQUEST, '__cp')

        dict_ = {}
        dict_['uids'] = []

        #it's cut
        if cpReadable[0] == 1:
            for tuple_ in cpReadable[1]:
                oldObject = portal.unrestrictedTraverse(tuple_)
                oldParent = oldObject.aq_parent
                if oldParent.UID() not in dict_['uids']:
                    dict_['uids'].append(oldParent.UID())
                #move only
                if parent.UID()==oldParent.UID():
                    newId = oldObject.getId()
                else:
                    ids = parent.manage_pasteObjects(cp)
                    newId = ids[0]['new_id']

                if operator:

                    position = parent.getObjectPosition(object_.getId())

                    if operator == '+':
                        position += 1

                    parent.moveObject(newId, position)
                    pu.reindexOnReorder(parent)

        #it's copy
        if cpReadable[0] == 0:
            for tuple_ in cpReadable[1]:
                cpObject = portal.unrestrictedTraverse(tuple_)
                cpParent = cpObject.aq_parent
                if cpParent.UID() not in dict_['uids']:
                    dict_['uids'].append(cpParent.UID())

            ids = parent.manage_pasteObjects(cp)
            newId = ids[0]['new_id']

            position = parent.getObjectPosition(object_.getId())

            if operator == '+':
                position += 1

            parent.moveObject(newId, position)
            pu.reindexOnReorder(parent)

        dict_['uids'].append(parent.UID())

        dict_['message'] = _('"${title}" copied.',
                             mapping={'title': safe_decode(context.Title()),
                                      })

        return json.encode(dict_)

    @log_or_trace(**lot_kwargs)
    def titleMappingByUid(self):
        """ """
        context = self.context
        translate = context.getAdapter('translate')
        getbrain = context.getAdapter('getbrain')
        form = context.REQUEST.form

        msgid = form.get('msgid')
        uid = form.get('uid')

        brain = getbrain(uid)

        json = context.getBrowser('json')

        dict_ = {}
        dict_['uid'] = uid
        dict_['message'] = translate(msgid,
                                     mapping={'title': safe_decode(brain.Title),
                                              })

        return json.encode(dict_)

    @log_or_trace(**lot_kwargs)
    def edit(self):
        """ """
        context = self.context
        form = context.REQUEST.form

        rc = context.getAdapter('rc')()
        presentation = context.getBrowser('presentation')
        book = context.getBrowser('book')

        json = context.getBrowser('json')
        uid = form.get('uid')

        context = rc.lookupObject(uid)

        html = context.restrictedTraverse('kss-slide-edit')()

        dict_ = {}
        dict_['uid'] = uid
        dict_['html'] = html
        return json.encode(dict_)

    def canAddPageInStructure(self):

        return self._canAddIn('unitracc: Add UnitraccStructurePage')


    def canAddSlideInPresentation(self):

        return self._canAddIn('unitracc: Add UnitraccSlide')

    def canAddFolderInPresentation(self):

        return self._canAddIn('unitracc: Add UnitraccPresentationFolder')

    def canAddFolderInStructure(self):

        return self._canAddIn('unitracc: Add UnitraccStructureFolder')

    def canCopyMoveDelete(self):
        """ """
        context = self.context
        if not context.getAdapter('checkperm')('Copy or Move'):
            return False

        return self._canAddIn('Delete objects')

    def _canAddIn(self, permission):
        context = self.context

        if context.getAdapter('checkperm')(permission):
            presentation = context.getBrowser('presentation')
            folder = presentation.getPresentationFolder()
            if folder and folder.UID()!=context.UID():
                return True

            book = context.getBrowser('book')
            folder = book.getBookFolder()
            if folder and folder.UID()!=context.UID():
                return True

    def canAddSlideForPresentation(self):

        return self._canAddFor('unitracc: Add UnitraccSlide')

    def canAddPageForStructure(self):

        return self._canAddFor('unitracc: Add UnitraccStructurePage')

    def canAddSlideForPresentation(self):

        return self._canAddFor('unitracc: Add UnitraccStructurePage')

    def canAddFolderForPresentation(self):

        return self._canAddFor('unitracc: Add UnitraccPresentationFolder')

    def canAddFolderForStructure(self):

        return self._canAddFor('unitracc: Add UnitraccStructureFolder')

    def _canAddFor(self, permission):

        context = self.context
        if context.getAdapter('checkperm')(permission):
            presentation = context.getBrowser('presentation')
            book = context.getBrowser('book')

            for folder in [presentation.getPresentationFolder(), book.getBookFolder()]:
                if folder and folder.UID()==context.UID():
                    return True
                if context.portal_type == 'Folder':
                    return True

    def canPasteInFolder(self):
        """ """
        context = self.context

        pc = context.getAdapter('pc')()

        query = {}
        query['path'] = {'query': context.getPath(),
                         'depth': 1}

        if not len(pc(query)):
            return True

    def getDefaultView(self):

        context = self.context
        dict_ = {}

        if context.portal_type == 'Folder':
            pu = context.getAdapter('pu')()  # plone_utils
            id = pu.getDefaultPage(context)
            if id:
                dict_['context'] = context.restrictedTraverse(id)
                dict_['template'] = context.restrictedTraverse('kss-structure-document-view')
            else:
                dict_['context'] = context
                dict_['template'] = context.restrictedTraverse(context.getLayout())

        else:
            dict_['context'] = context
            dict_['template'] = context.restrictedTraverse('kss-structure-document-view')

        if context.getLayout() in context.getBrowser('book').getBookTemplates():
            brains = context.getBrowser('stage').getAsBrains('book-start-page', context.UID())
            if brains:
                dict_['context'] = brains[0].getObject()
                dict_['template'] = dict_['context'].restrictedTraverse('kss-structure-document-view')

        return dict_

    @log_or_trace(**lot_kwargs)
    def setAgendaView(self):
        """ """
        context = self.context
        rc = context.getAdapter('rc')()
        _ = context.getAdapter('translate')
        json = context.getBrowser('json')
        self._showDefaultPage(context)
        context.setLayout('book_agenda_view')
        context.getAdapter('notifyedit')()
        context.reindexObject()

        dict_ = {}
        dict_['uid'] = context.UID()
        dict_['message'] = _('View changed.')

        return json.encode(dict_)

    @log_or_trace(**lot_kwargs)
    def setDefaultPage(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        rc = context.getAdapter('rc')()
        uid = form.get('uid', '')
        _ = context.getAdapter('translate')
        context = rc.lookupObject(uid)
        json = context.getBrowser('json')

        self._showDefaultPage(context)

        objectId = form.get('objectId', '')
        context.setDefaultPage(objectId)
        context.reindexObject()

        defaultPage = context.restrictedTraverse(objectId)
        defaultPage.setExcludeFromNav(True)
        defaultPage.reindexObject()

        dict_ = {}
        dict_['uid'] = context.UID()
        dict_['message'] = _('Changes saved.')
        dict_['html'] = context.restrictedTraverse('kss-structure-content')()

        return json.encode(dict_)

    def canSetAgendaView(self):

        context = self.context
        if not self._isBookTypeRootFolder():
            pu = context.getAdapter('pu')()
            id = pu.getDefaultPage(context)
            if id:
                return True

    def canSetDefaultPage(self):

        context = self.context
        pc = context.getAdapter('pc')()

        if not self._isBookTypeRootFolder():
            # Check if context-folder already has a default-page-view
            pu = context.getAdapter('pu')()
            id = pu.getDefaultPage(context)

            dict_ = {}
            dict_['path'] = {'query': context.getPath(),
                             'depth': 1}
            if pc(dict_) and not id:
               return True

    def _showDefaultPage(self, context):
        pu = context.getAdapter('pu')()
        id = pu.getDefaultPage(context)
        if id:
            object_ = context.restrictedTraverse(id)
            object_.setExcludeFromNav(False)
            object_.reindexObject()

    def editFolder(self):
        """ """
        context = self.context
        return context.restrictedTraverse('kss-structure-folder-edit')()

    def _isBookTypeRootFolder(self):
        """
        Checks if context is the root folder of a book type (book, paper, instruction, documentation)
        """
        context = self.context
        book = context.getBrowser('book')

        if context.portal_type == 'Folder':
            if context.getLayout() in book.getBookTemplates():
                return True
            else:
                return False
        else:
            return False

    @log_or_trace(**lot_kwargs)
    def cancel(self):
        """ """
        context=self.context

        form=context.REQUEST.form

        context.getBrowser('tpcheck').auth_modify_portal_content()

        rc=context.getAdapter('rc')()
        object_=rc.lookupObject(form['uid'])
        if object_.checkCreationFlag() and not object_.Title() and object_._isIDAutoGenerated(object_.getId()):
            parent=object_.aq_parent
            parent.manage_delObjects(ids=[object_.getId()])
            uid=parent.UID()
        else:
            uid=object_.UID()
        return uid
