from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
from DateTime import DateTime
from xml.dom.minidom import parseString


class IUnitraccMigrator(Interface):

    def fixContent(self):
        """ """

    def sort(self):
        """ """

    def fixAuthors(self):
        """ """

    def linkTranslations(self):
        """ """

    def setGenerateStructureNumber(self):
        """ """

    def setResetNumbering(self):
        """ """

    def fixImageLanguage(self, reindex=True):
        """ """

    def fixExcludeFromNav(self, reindex=True):
        """ """

    def fixCaption(self, reindex=True):
        """ """

    def fixLegend(self, reindex=True):
        """ """

    def fixSoundComment(self):
        """ """


class Browser(BrowserView):

    implements(IUnitraccMigrator)

    def fixContent(self):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        portal = context.getAdapter('portal')()

        data = str(portal.aq_parent.restrictedTraverse('translations.doc'))
        dom = parseString(data)

        for infoElement in dom.getElementsByTagName('info'):
            if infoElement.getElementsByTagName('dc:title'):
                title = self.getText(infoElement.getElementsByTagName('dc:title')[0])
                description = self.getText(infoElement.getElementsByTagName('dc:description')[0])
                creator = self.getText(infoElement.getElementsByTagName('dc:creator')[0])
                language = self.getText(infoElement.getElementsByTagName('dc:language')[0])
                created = self.getText(infoElement.getElementsByTagName('xmp:CreateDate')[0])
                modified = self.getText(infoElement.getElementsByTagName('xmp:ModifyDate')[0])
                path = self.getText(infoElement.getElementsByTagName('path')[0])
                dict_ = {}
                for field in infoElement.getElementsByTagName('field'):
                    dict_[field.getAttribute('name')] = self.getText(field)
                if path.find('/vortraege/herrenknecht-en') != -1 or path.find('/vortraege/exclusive-utility-tunnelling--starting-and-target-shafts-en') != -1 or path.find('/vortraege/exclusive-utility-tunnelling--geotechnical-investigations-en') != -1  or path.find('/vortraege/exclusive-utility-tunnelling--jacking-pipes-en') != -1:
                    current = portal.restrictedTraverse(path, None)
                    print current.absolute_url()
                    if current:
                        current.setTitle(title)
                        if description:
                            current.setDescription(description)
                        if language:
                            current.setLanguage(language)
                        if dict_['code']:
                            current.setCode(dict_['code'])
                        current.setCreationDate(DateTime(created))
                        current.setModificationDate(DateTime(modified))
                        current.reindexObject()

        return 'ok'

    def getDom(self):
        """ """
        context = self.context
        portal = context.getAdapter('portal')()
        data = str(portal.aq_parent.restrictedTraverse('translations.doc'))
        dom = parseString(data)

        return dom

    def setResetNumbering(self):
        """ """
        context = self.context
        dom = self.getDom()
        portal = context.getAdapter('portal')()

        for infoElement in dom.getElementsByTagName('info'):
            dict_ = {}
            for field in infoElement.getElementsByTagName('field'):
                dict_[field.getAttribute('name')] = self.getText(field)
            if dict_.get('numbering_reset') == 'true':
                path = self.getText(infoElement.getElementsByTagName('path')[0])
                current = portal.restrictedTraverse(path, None)
                if current:
                    print current.absolute_url()
                    current.setResetNumbering(True)
                    current.reindexObject()
        return 'ok'

    def getText(self, item):
        """get the text from a textnode"""
        if item.childNodes:
            data = str(item.childNodes[0].nodeValue).strip()
            return data
        return ''

    def sort(self):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        portal = context.getAdapter('portal')()

        data = str(portal.aq_parent.restrictedTraverse('translations.doc'))
        dom = parseString(data)

        infos = {}
        for infoElement in dom.getElementsByTagName('info'):
            path = self.getText(infoElement.getElementsByTagName('path')[0])

            fields = {}
            for field in infoElement.getElementsByTagName('field'):
                fields[field.getAttribute('name')] = self.getText(field)

            infos[path] = fields

        pc = context.getAdapter('pc')()._catalog

        query = {}
        query['path'] = ['/unitracc/know-how/vortraege/herrenknecht-en',
                       '/unitracc/know-how/vortraege/exclusive-utility-tunnelling--starting-and-target-shafts-en',
                       '/unitracc/know-how/vortraege/exclusive-utility-tunnelling--geotechnical-investigations-en',
                       '/unitracc/know-how/vortraege/exclusive-utility-tunnelling--jacking-pipes-en',
                       #'/unitracc/know-how/dokumentation',
                       #'/unitracc/know-how/handlungsanweisungen',
                       #'/unitracc/know-how/vortraege',
                       #'/unitracc/know-how/skripte',
                       ]
        query['portal_type'] = 'Folder'

        for folderBrain in pc(query):
            query = {}
            query['path'] = {'query': folderBrain.getPath(),
                           'depth': 1}
            brains = pc(query)
            list_ = []
            for brain in brains:
                print brain.getURL()
                dict_ = {}
                dict_['brain'] = brain
                dict_['path'] = brain.getPath()

                list_.append(dict_)

            for dict_ in list_:
                if infos.has_key(dict_['path']):
                    dict_['sortId'] = int(infos[dict_['path']]['sortId'])
            list_.sort(lambda a, b: cmp(a.get('sortId', 0), b.get('sortId', 0)))

            context = folderBrain.getObject()

            ids = [dict_['brain'].getId for dict_ in list_]
            for id in ids:
                print id
                context.moveObject(id, ids.index(id))
            context.plone_utils.reindexOnReorder(context)
        return 'ok'

    def fixAuthors(self):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        pc = context.getAdapter('pc')()._catalog
        form = context.REQUEST.form

        for brain in pc(portal_type=['UnitraccEvent', 'UnitraccNews', 'UnitraccArticle']):
            object_ = brain.getObject()
            if object_:
                for creator in object_.Creators():
                    query = {}
                    query['portal_type'] = ['UnitraccAuthor', 'UnitraccContact']
                    query['Title'] = creator
                    brains = pc(query)
                    if len(brains) == 1:
                        brain = brains[0]
                        print [brain]
                        stage = object_.getBrowser('stage')
                        form.update({'relationship': 'creators'})
                        form.update({'uids': [brain.UID]})
                        stage.set()

    def linkTranslations(self):
        """ """
        context = self.context

        portal = context.getAdapter('portal')()
        rc = context.getAdapter('rc')()
        data = str(portal.aq_parent.restrictedTraverse('translations.doc'))
        dom = parseString(data)

        infos = {}
        for infoElement in dom.getElementsByTagName('info'):
            path = self.getText(infoElement.getElementsByTagName('path')[0])

            languages_ = {}
            for languages in infoElement.getElementsByTagName('languages'):
                for language in languages.getElementsByTagName('language'):
                    uid = str(self.getText(language)).strip()
                    langCode = language.getAttribute('lang')
                    languages_[language.getAttribute('lang')] = self.getText(language)
                    if uid:
                        canonical = portal.restrictedTraverse(path, None)
                        if canonical:
                            translation = rc.lookupObject(uid)
                            if translation and not translation.hasTranslation(canonical.Language()):
                                print '__________'
                                print translation
                                print canonical
                                print translation.hasTranslation(canonical.Language())
                                print translation.Language()
                                print canonical.Language()

                                translation.addTranslationReference(canonical)

    def setGenerateStructureNumber(self):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        pc = context.getAdapter('pc')()._catalog
        structurenumber = context.getBrowser('structurenumber')

        query = {}
        query['path'] = {'query': '/unitracc/know-how/fachinformationssysteme',
                       'depth': 1}
        query['portal_type'] = 'Folder'
        """
        for brain in context.portal_catalog(query):
            book=brain.getObject()
            currentLayout=book.getLayout()
            query['path']=book.getPath()
            for brain in context.portal_catalog(query):
                folder=brain.getObject()
                folder.setLayout('book_agenda_view')
            book.setLayout(currentLayout)
        """
        query = {}
        query['path'] = ['/unitracc/know-how/fachinformationssysteme/guidelines-for-impact-moling-en',
                       '/unitracc/know-how/fachinformationssysteme/guidelines-for-pipe-bursting-en',
                       '/unitracc/know-how/fachinformationssysteme/guidelines-for-pipe-ramming-en',
                       ]
        query['getExcludeFromNav'] = True

        for brain in pc(query):
            object_ = brain.getObject()
            object_.setGenerateStructureNumber(False)
            object_.reindexObject()

        del query['getExcludeFromNav']

        for brain in pc(query):
            structurenumber.set(brain)

        query['getExcludeFromNav'] = True
        for brain in pc(query):
            parent = brain.getParent().getObject()
            parent.setDefaultPage(brain.getId)

        return 'ok'

    def fixImageLanguage(self, reindex=True):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        migrationxml = context.getBrowser('migrationxml')

        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = 'UnitraccImage'
        query['Language'] = 'all'

        for brain in pc(query):
            print brain.getURL()
            langCode = migrationxml.getLanguageForUid(brain.UID)
            if langCode:
                object_ = brain.getObject()
                object_.setLanguage(langCode)
                if reindex:
                    pc.catalog_object(object_, object_.getPath())
        return 'ok'

    def fixExcludeFromNav(self, reindex=True):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        migrationxml = context.getBrowser('migrationxml')

        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = 'UnitraccImage'
        query['Language'] = 'all'

        for brain in pc(query):
            value = migrationxml.getExcludeFromNavForUid(brain.UID)
            print brain.getURL()

            if value:
                object_ = brain.getObject()
                object_.setExcludeFromNav(value)
                if reindex:
                    pc.catalog_object(object_, object_.getPath())

    def fixCaption(self, reindex=True):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        migrationxml = context.getBrowser('migrationxml')

        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = ['UnitraccTable', 'UnitraccFile', 'UnitraccImage']
        query['Language'] = 'all'

        for brain in pc(query):
            value = migrationxml.getCaption(brain.UID)
            if value:
                print brain.UID
                object_ = brain.getObject()
                #if not object_.getCaption():
                object_.setCaption(value)
                if reindex:
                    pc.catalog_object(object_, object_.getPath())

    def fixLegend(self, reindex=True):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        migrationxml = context.getBrowser('migrationxml')

        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = ['UnitraccTable', 'UnitraccFile', 'UnitraccImage']
        query['Language'] = 'all'

        for brain in pc(query):
            value = migrationxml.getLegend(brain.UID)
            if value:
                print brain.getURL()
                object_ = brain.getObject()
                object_.setLegend(value)
                if reindex:
                    pc.catalog_object(object_, object_.getPath())

    def fixSoundComment(self):
        """ """
        context = self.context

        context.getBrowser('authorized').managePortal()

        migrationxml = context.getBrowser('migrationxml')
        form = context.REQUEST.form
        pc = context.getAdapter('pc')()

        query = {}
        query['portal_type'] = ['Document']
        query['path'] = '/unitracc/know-how/vortraege'
        query['Language'] = 'all'

        for brain in pc(query):
            uid = migrationxml.getComment(brain.UID)
            if uid:
                print 'COMMENT'
                print brain.getURL()
                object_ = brain.getObject()
                stage = object_.getBrowser('stage')

                form.update({'relationship': 'presentation-comment'})
                form.update({'uids': [uid]})
                stage.set()

            uid = migrationxml.getSound(brain.UID)

            if uid:
                print 'SOUND'
                print brain.getURL()
                object_ = brain.getObject()
                stage = object_.getBrowser('stage')

                form.update({'relationship': 'presentation-sound'})
                form.update({'uids': [uid]})
                stage.set()
