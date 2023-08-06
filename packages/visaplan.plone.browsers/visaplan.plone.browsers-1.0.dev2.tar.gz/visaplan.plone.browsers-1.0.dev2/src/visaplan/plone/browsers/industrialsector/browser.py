# -*- coding: utf-8 -*- äöü
from dayta.browser.public import BrowserView, implements, Interface
from xml.dom.minidom import parseString
from plone.memoize import ram

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.coding import safe_decode
from visaplan.tools.lands0 import groupstring

# Dieser Browser:
from .crumbs import register_crumbs

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport('industrialsector')
from pprint import pformat


class IIndustrialSector(Interface):

    def get(self):
        """ """

    def getValue(self, key):
        """ """

    def getImage(code):
        """ """

    def setConfigure(self):
        """ """

    def getConfigure(self):
        """ """

    def getValueForSearch(self):
        """ """

    def getLevel2(self, code1):
        """ """

    def getLevel3(self, code1, code2):
        """ """

    def search(self, string_):
        """
        Interpretiere einen (aktuell ein bis sechs Zeichen langen)
        Fachbereichscode und gib eine Liste zurück
        """

    def getIndex(self, code):
        """ """

    def buildDomainFromRequest(self):
        """ """


def cache_key_lang_code(method, self):
    """ """
    langCode = self.context.getAdapter('langcode')()
    return langCode


def cache_key_lang_code_level(method, self, level):
    """ """
    langCode = self.context.getAdapter('langcode')()
    return (langCode, level)


def cache_key_code(method, self, code):
    """ """
    return code


def cache_key_code_language(method, self, code):
    """ """
    langCode = self.context.getAdapter('langcode')()
    return (code, langCode)


class Browser(BrowserView):

    implements(IIndustrialSector)

    storageKey = 'industrialdropdownselection'

    @ram.cache(cache_key_lang_code)
    def build(self):
        """ """
        # TODO: Dringend dokumentieren! 
        context = self.context
        list_ = []
        langCode = context.getAdapter('langcode')()
        if not context.unrestrictedTraverse('domains-%s' % langCode, None):
            langCode = 'en'
        string_ = context.unrestrictedTraverse('domains-%s' % langCode).raw
        dom = parseString(string_)

        self.recurseBuild(dom, list_)
        return list_

    @ram.cache(cache_key_code_language)
    def getValue(self, code):
        """ """
        list_ = self.get()
        for k, v in list_:
            if k == code:
                while v.startswith('-'):
                    v = v[1:]
                return v

    @ram.cache(cache_key_lang_code)
    def get(self):
        """ """
        list_ = []
        self.recurseGet(self.build()[0]['childs'][0]['childs'], list_, 0, '')
        return list_

    @ram.cache(cache_key_code)
    def getImage(self, code):
        """ """
        # TODO: Dringend dokumentieren! 
        return self.recurseImage(self.build()[0]['childs'][0]['childs'], code)

    @ram.cache(cache_key_lang_code)
    def getLevel1(self):
        """ """
        list_ = []
        for child in self.build()[0]['childs'][0]['childs']:
            list_.append((child['shortcut'], child['title']))
        return list_

    @ram.cache(cache_key_lang_code_level)
    def getCompleteLevel(self, level):
        """ """
        list_ = []
        for child in self.build()[0]['childs'][0]['childs']:
            if level == '1':
                list_.append((child['shortcut'], child['title']))
            if level == '2':
                for item in child['childs']:
                    list_.append((item['shortcut'], item['title']))
            if level == '3':
                for item in child['childs']:
                    for item in child['childs']:
                        list_.append((item['shortcut'], item['title']))
        return list_

    def getLevel2(self, code1):
        context = self.context

        if not code1:
            return []

        list_ = []
        for child in self.build()[0]['childs'][0]['childs']:
            if child['shortcut'] == code1:
                for item in child.get('childs', []):
                    list_.append((item['shortcut'], item['title']))
        return list_

    def getLevel3(self, code1, code2):
        context = self.context
        form = context.REQUEST.form

        if not code1 and code2:
            return []

        list_ = []
        for child in self.build()[0]['childs'][0]['childs']:
            if child['shortcut'] in code1:
                for item in child.get('childs', []):
                    if item['shortcut'] in code2:
                        for child in item.get('childs', []):
                            list_.append((child['shortcut'], child['title']))
        return list_

    def recurseImage(self, childs, code, shortcut=''):
        """ """
        # TODO: Dringend dokumentieren! 
        for dict_ in childs:
            if shortcut + dict_['shortcut'] == code:
                if not dict_.get('imgName', ''):
                    if code:
                        imgName = self.recurseImage(self.build()[0]['childs'][0]['childs'], code[:-2])
                        if imgName:
                            return imgName
                return dict_.get('imgName', '')
            if dict_.get('childs', []):
                imgName = self.recurseImage(dict_['childs'], code, shortcut + dict_['shortcut'])
                if imgName:
                    return imgName

    def recurseGet(self, childs, list_, level, shortcut):
        for dict_ in childs:
            list_.append((shortcut + dict_['shortcut'], '-' * level + dict_['title']))
            if dict_.get('childs', []):
                self.recurseGet(dict_['childs'], list_, level + 1, shortcut + dict_['shortcut'])

    def recurseBuild(self, element, childs):
        # TODO: Dringend dokumentieren! 
        dict_ = {}
        dict_['childs'] = []

        for node in element.childNodes:
            if self.getText(node):
                dict_[node.nodeName] = self.getText(node)
            if len(node.childNodes) > 1:
                self.recurseBuild(node, dict_['childs'])

        if not dict_['childs']:
            del dict_['childs']
        if dict_:
            childs.append(dict_)

    def getText(self, element):
        if len(element.childNodes) == 1:
            return safe_decode(element.childNodes[0].nodeValue).strip()
            return str(element.childNodes[0].nodeValue).strip()

        return ''

    def setConfigure(self):
        """ """
        context = self.context
        context.getAdapter('authorized')('Manage portal')
        message = context.getAdapter('message')
        form = context.REQUEST.form
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')

        changeFrom = form.get('changeFrom', '')
        changeTo = form.get('changeTo', '')
        if changeFrom and changeTo:
            form[changeTo] = form[changeFrom]
            del form[changeFrom]
            form['relationships'] = form['relationships'].replace(changeFrom, changeTo)

        settings._set(self.storageKey, form)

        message('Changes saved.')
        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def getConfigure(self):
        """ """
        context = self.context
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')

        return settings.get(self.storageKey, {})

    def getValueForSearch(self):
        """
        Gib den Wert für die Suche zurück
        """
        # XXX Standardwert für neuen Objekte ist '_' --> ['_', '_*'] ?!
        # verwendet für getCustomSearch; siehe ../../patches.py 
        context = self.context
        field = context.getField('code')
        list_ = []
        if field:
            value = field.get(context)
            if not value or value == '_':
                return list_
            values = groupstring(value, 2)
            values.extend([item + '*' for item in values])
            list_.extend(values)
            list_.append(value)
        return list_

    def search(self, string_):
        """
        Interpretiere einen (aktuell ein bis sechs Zeichen langen)
        Fachbereichscode und gib eine Liste zurück
        """
        context = self.context

        self.dict_ = {}

        original = str(string_)
        DEBUG('search(%r)', original)

        if string_.find(':') != -1:
            assert ':' in string_
            level, code = string_.split(':')
            code = code.replace('*', '')
            self.recurseSearch(int(level),
                               0,
                               code,
                               self.build()[0]['childs'],
                               [])
            DEBUG('  search(%r):\n'
                    '    self.dict_=%s',
                  original, pformat(self.dict_))
        else:
            assert ':' not in string_

        if string_.endswith('*'):
            string_ = string_.replace('*', '')
        else:
            if not len(string_) % 2:
                DEBUG('  search(%r) --> (266)\n    [%r]',
                      original, string_)
                return [string_]

        values = groupstring(string_, 2)
        counter = 0
        query = {}
        for item in values:
            if len(item) == 2:
                query['code' + str(counter + 1)] = item
            if len(item) != 2:
                method = getattr(self, 'getLevel' + str(counter + 1))
                for pair in method(**query):
                    if pair[0].startswith(item):
                        self.dict_[''.join(values[:values.index(item)]) + pair[0]] = 1
            counter += 1

        if not len(string_) % 2 and original.endswith('*'):
            #Search over all sublevels
            if len(values) == 1:
                self.dict_[values[0]] = 1
                for pair2 in self.getLevel2(values[0]):
                    self.dict_[values[0] + pair2[0]] = 1
                    for pair3 in self.getLevel3(values[0], pair2[0]):
                        self.dict_[values[0] + pair2[0] + pair3[0]] = 1
            if len(values) == 2:
                self.dict_[values[0] + values[1]] = 1
                for pair3 in self.getLevel3(values[0], values[1]):
                    self.dict_[values[0] + values[1] + pair3[0]] = 1

        DEBUG('  search(%r) --> (296)\n    %r',
              original, self.dict_.keys())
        return self.dict_.keys()

    def recurseSearch(self, level, currentLevel, code, childs, parents):
        """ """
        context = self.context
        for child in childs:
            if currentLevel < level:
                self.recurseSearch(level, int(currentLevel) + 1, code, child.get('childs', []), parents + [child])

            if currentLevel == level:
                if child['shortcut'].startswith(code):
                    self.dict_[''.join([dict_.get('shortcut', '')
                                        for dict_ in parents
                                        ]) + child.get('shortcut', '')
                               ] = 1

    def getIndex(self, code):
        # XXX dokumentieren oder entfernen!
        context = self.context

        if not code:
            return 'XXX' * self.getIndexLength()

        values = groupstring(code, 2)

        self.index = ''

        if values:
            self.getIndexRecurse(values, self.build()[0]['childs'][0]['childs'])

        self.index += (self.getIndexLength() - len(values)) * '0'

        return self.index

    def getIndexRecurse(self, list_, childs):
        # XXX dokumentieren oder entfernen!
        code = list_[0]
        list_.pop(0)

        counter = 0
        for child in childs:
            counter += 1
            if child['shortcut'] == code:
                self.index += str(counter)
                if list_:
                    self.getIndexRecurse(list_, child['childs'])

    def getIndexLength(self):
        # XXX dokumentieren oder entfernen!
        return 4

    def buildDomainFromRequest(self):
        context = self.context
        form = context.REQUEST.form

        return form.get('code1', [''])[0] + form.get('code2', [''])[0] + form.get('code3', [''])[0]
