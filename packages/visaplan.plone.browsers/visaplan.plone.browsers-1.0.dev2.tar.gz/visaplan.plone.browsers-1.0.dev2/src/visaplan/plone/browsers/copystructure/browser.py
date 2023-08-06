# -*- coding: utf-8 -*-
from dayta.browser.public import BrowserView, implements, Interface
import transaction

# Unitracc-Tools:
from visaplan.kitchen.spoons import get_tag_info
from visaplan.plone.tools.log import getLogSupport

# Installierte Pakete:
from bs4 import BeautifulSoup

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport('copystructure')
from visaplan.tools.debug import pp


class ICopyStructure(Interface):

    def get(self):
        """ """


class Browser(BrowserView):

    implements(ICopyStructure)

    def get(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        form.update({'copyType': '2'})
        self._copyExternalContent(context.UID())

    def _buildRelationIndex(self):
        """
         Mapping altes Objec -> neues Object
        """
        context = self.context
        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()

        oldRoot = rc.lookupObject(context.getCopyFrom())
        newRoot = context

        query = {}
        query['Language'] = 'all'
        query['path'] = newRoot.getPath()
        query['sort_on'] = 'created'

        dict_ = {}
        index = len(newRoot.getPath())

        for brain in pc(query):
            query = {}
            query['Language'] = 'all'
            query['path'] = {'query': oldRoot.getPath() + brain.getPath()[index:],
                             'depth': 0}

            dict_[pc(query)[0].UID] = brain  # TH: ???
        self.relationIndex = dict_

    def _copyExternalContent(self, uid):
        """
        Bearbeite die kopierten Objekte
        """
        logger.info('_copyExternalContent(uid=%s) ...', uid)
        context = self.context
        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()
        unitraccgroups = context.getBrowser('unitraccgroups')
        self._buildRelationIndex()
        folder = rc.lookupObject(uid)
        form = context.REQUEST.form
        self.user_id = form.get('user_id', '')
        if self.user_id:
            logger.info('fuer Benutzer-ID %(user_id)r', form)
        else:
            logger.warn('keine Benutzer-ID in Formulardaten!')

        self.editorGroups = {}
        for prefix in unitraccgroups.getStructureGroupPrefixes():
            groupId = unitraccgroups.buildStructureGroupName(folder.UID(), prefix)
            self.editorGroups[prefix] = groupId

        query = {}
        query['Language'] = form.get('language', 'all') or 'all'
        query['path'] = folder.getPath()
        query['sort_on'] = 'created'
        if debug_active:
            pp(query=query)

        # Speichere schon kopierte mehrfach referenzierte Objekte:
        self.copyObjects = {}

        changedowners = 0
        no_co = 0
        found = 0
        list_ = []
        for brain in pc(query):
            found += 1
            object_ = brain.getObject()
            list_.append(object_)
            self.langCode = object_.Language()
            self._handleFields(object_)

            # Neuer Benutzer fuer die Strukturinhalte. Ordner und Dokumente
            if self.user_id:
                object_.getBrowser('changeowner').set(self.user_id)
                changedowners += 1
            else:
                no_co += 1
        (found > 0 and logger.info or logger.warn)(
                '%d Objekte gefunden', found)
        logger.info('changeowner-Aufruf fuer %d Objekte', changedowners)
        logger.info('KEIN changeowner-Aufruf fuer %d Objekte', no_co)

        for uid, dict_ in self.copyObjects.items():
            if dict_.has_key('copy'):
                self._handleFields(dict_['copy'])

        for object_ in list_:
            for field in object_.schema.fields():
                replaced = False
                if field.__dict__['type'] == 'text':
                    text = field.get(object_)
                    if text:
                        text, replaced = self._handleAnker(text, replaced)
                        if replaced:
                            field.set(object_, text)
                if replaced:
                    object_.reindexObject()

        for object_ in list_:
            object_.getAdapter('notifyedit')()
        logger.info('... _copyExternalContent(uid=%s)', uid)

    def _handleAnker(self, text, replaced):
        """ """
        for uid, dict_ in self.copyObjects.items():
            uidOriginal = dict_['original'].UID()
            if dict_.has_key('copy'):
                uidCopy = dict_['copy'].UID()
                if text.find(uidOriginal) != -1:
                    text = text.replace(uidOriginal, uidCopy)
                    replaced = True

        return text, replaced

    def _handleFields(self, object_):
        """ """
        self._uid = object_.UID()
        for field in object_.schema.fields():
            replaced = False
            if field.__dict__['type'] == 'text':
                text = field.get(object_)
                if text:
                    text, replaced = self._handleText(text)
                    #fix page links and page ankers
                    for uid, brain in self.relationIndex.items():
                        if text.find(uid) != -1:
                            text = text.replace(uid, brain.UID)
                            replaced = True
                    text, replaced = self._handleAnker(text, replaced)
                    if replaced:
                        field.set(object_, text)
            if replaced:
                object_.reindexObject()

    def _extractLinks(self, text):
        """
        parse den übergebenen Text und gib eine Liste von Verweisen zurück
        (als Dictionarys).
        """
        info = []
        if not text:
            return info
        elif isinstance(text, unicode):
            space = u' '
        else:
            space = ' '
        context = self.context
        transform = context.getBrowser('transform')
        rc = context.getAdapter('rc')()
        message = context.getAdapter('message')

        searchableText = text + space + transform.get(text)

        for msgstr in getattr(transform, 'warnings', []):
            message(msgstr, 'warning')
            #Je nach Verwendung und Einbindung ist diese Info vorhanden oder nicht.
            if hasattr(self, '_uid'):
                message('Page UID: ' + self._uid, 'warning')

        soup = BeautifulSoup(text)
        for elem in soup.find_all(['a', 'img']):
            dic = get_tag_info(elem)
            uid = dic.get('uid', None)
            if uid is not None:
                o = rc.lookupObject(uid)
                if o:
                    # 'tag' : in _handleText zunächst über str
                    dic.update({
                        'tag': elem,
                        'object_': o,
                        })
                    info.append(dic)
        return info

        # ... toter Code; demnächst zu löschen:
        for imgTag in transform._getImages(searchableText):
            uidImg = transform._getImgUid(imgTag)
            if uidImg:
                object_ = rc.lookupObject(uidImg)
                if object_:
                    dict_ = {}
                    dict_['uid'] = object_.UID()
                    dict_['object_'] = object_
                    dict_['tag'] = imgTag
                    info.append(dict_)

        for aTag in transform._getLinks(searchableText):
            #its no anker source
            # kein Link zu einem lokalen Anker, ...
            if aTag.find('href="#') == -1:
                #its no anker target
                # aber es ist ein href-Attribut vorhanden ...
                if aTag.find('href') != -1:
                    # ... also extrahiere die UID aus dem Element:
                    uidA = transform._getUid(aTag)[0]
                    if uidA:
                        object_ = rc.lookupObject(uidA)
                        # ... es wurde ein entsp. Objekt gefunden!
                        if object_:
                            dict_ = {}
                            dict_['uid'] = object_.UID()
                            dict_['object_'] = object_
                            dict_['tag'] = aTag
                            info.append(dict_)

        return info

    def _handleText(self, text):
        """
        lies Textfelder aus, die Verweise auf Objekte enthalten, die kopiert
        werden müssen; die Kopie hat dann eine neue UID, die sich im Text
        entsprechend niederschlagen muß
        """
        context = self.context
        rc = context.getAdapter('rc')()
        pc = context.getAdapter('pc')()
        form = context.REQUEST.form
        tempFolder = context.getBrowser('temp').getTempFolder()

        info = self._extractLinks(text)

        replaced = False
        for dict_ in info:
            object_ = dict_['object_']
            uid = dict_['uid']
            object_.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)
            if not self.copyObjects.has_key(uid):
                self.copyObjects[uid] = {'original': object_}

            if not self.copyObjects[uid].has_key('copy'):
                # Sprachabhängige Kopie (Übersetzung erstellen)
                if form.get('copyType') == '2':
                    translations = object_.getTranslations()
                    #found a translation
                    if translations.get(self.langCode) and translations.get(self.langCode)[0].UID() != uid:
                        copy_ = translations.get(self.langCode)[0]

                        self.copyObjects[uid]['copy'] = copy_
                    else:
                        #copy to temp
                        copy_ = self._copyObject(object_, tempFolder)
                        #link tranlation
                        try:
                            if copy_:
                                canonical = object_.getCanonical()
                                copy_.addTranslationReference(canonical)
                        except Exception, e:
                            logger.info(str(e))

                #make a copy of every linked object
                if form.get('copyType') == '1':
                    #copy to temp
                    copy_ = self._copyObject(object_, tempFolder)
            else:
                copy_ = self.copyObjects[uid]['copy']

            # Falls kopier erzeugt (egal ob referenz oder komplett
            if copy_:
                # TODO: Umstellung auf direkte Elementmanipulation!
                # 'tag' enthält ein BeautifulSoup-Element:
                oldTag = str(dict_['tag'])
                newTag = oldTag.replace(uid, copy_.UID())
                # Text ersetzen (linkurl und Text)
                text = text.replace(oldTag, newTag)
                replaced = True

        return text, replaced

    def _copyObject(self, object_, tempFolder):
        """
        Aufgerufen aus _handleText:
        Lege eine Kopie des verknüpften Objekts an.
        """
        parent = object_.aq_parent
        if object_.portal_type == 'Document':
            #Dokumente duerfen nicht kopiert werden, weil dies Verweise aus einer Struktur sind.
            return
        else:
            logger.info("Copying Object: %s (Title: %s ) portal_type: %s" \
            % (object_.getId(), object_.Title(), object_.portal_type))

            cp = parent.manage_copyObjects(ids=[object_.getId()])
            ids = tempFolder.manage_pasteObjects(cb_copy_data=cp)

            logger.info("New UID: %s" % ids[0]['new_id'])

            new_uid = ids[0]['new_id']
            copy_ = tempFolder[ids[0]['new_id']]
            copy_.setLanguage(self.langCode)
            for prefix, groupId in self.editorGroups.items():
                copy_.manage_setLocalRoles(groupId, [prefix])
            if self.user_id:
                copy_.getBrowser('changeowner').set(self.user_id)

            copy_.getBrowser('workflow').change('make_private')
            transaction.savepoint()
            self.copyObjects[object_.UID()]['copy'] = copy_

            copy_.getAdapter('notifyedit')()
