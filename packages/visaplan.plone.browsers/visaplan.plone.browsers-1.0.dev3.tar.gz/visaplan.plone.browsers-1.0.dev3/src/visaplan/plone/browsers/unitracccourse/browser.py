# -*- encoding: UTF-8 -*-
from dayta.browser.public import Interface, BrowserView, implements

# Standardmodule:
import re

# Plone-Module:
from Products.CMFCore.utils import getToolByName
from plone.memoize import ram
from AccessControl import Unauthorized
from zExceptions import Redirect

# Installierte Module:
from xml.etree.cElementTree import Element
from xml.etree import cElementTree as cET
import demjson
from bs4 import BeautifulSoup

# Unitracc:
from ...permissions import Access_course_documents, ModifyPortalContent

# Unitracc-Tools:
from visaplan.kitchen.spoons import extract_uid
from visaplan.kitchen.spoons import extract_uid_from_qs
from ...tools.misc import looksLikeAUID
from visaplan.tools.sequences import inject_indexes
from visaplan.tools.coding import safe_decode
from visaplan.plone.tools.log import getLogSupport

# Andere Browser:
from ..unitraccgroups.utils import (LEARNER_SUFFIX, ALUMNI_SUFFIX,
        learner_group_id, alumni_group_id, generic_group_id,
        )
from ..booking.utils import extract_float
from ..groupsharing.browser import groupinfo_factory

# Dieser Browser:
from .crumbs import register_crumbs
register_crumbs()

# Logging und Debugging:
from ...tools.debug import (trace_this, log_call_and_result,
        log_call_and_result_length,
        )
logger, debug_active, DEBUG = getLogSupport('unitracccourse')
debug_active = 1
from visaplan.tools.debug import log_or_trace, pp

from pprint import pformat

# ------------------------------------------------------ [ Daten ... [
# TODO: mapping_ überarbeiten/dokumentieren; siehe ./TODO.txt!
mapping_ = {}
lot_kwargs = {'debug_level': debug_active,
              'logger': logger,
              'trace': 0,
              }
# ------------------------------------------------------ ] ... Daten ]


class IUnitraccCourseBrowser(Interface):

    def get_level(self):
        """ """

    def get_current(self, uid=None):
        """ """

    def crumbs(self):
        """ """

    def is_folderish(self):
        """ """

    def set(self):
        """ """

    def get_course_structure(self):
        """ """

    def element_item_info(self, course_uid, element_uid):
        """
        XXX dringend mal dokumentieren!
        """

    def load(self):
        """ """

    def search(self):
        """ """

    def get_visible_courses(self):
        """
        Buchbare und kostenlose Kurse
        """

    def get_brain_by_uid(self, uid=None):
        """ """

    def get_first(self):
        """ """

    def get_prev_and_next(self, current_uid):
        """ get next and previus UID from actual Foil """

    def get_last(self):
        """ """

    def get_course_page_count(self):
        """ """

    def get_item_position(self, dict_):
        """ """

    def get_ppt_navigation(self):
        """ """

    def get_content(self, prefix, current):
        """ """

    def get_agenda(self, uid):
        """ """

    def current_to_object(self, current):
        """ """

    def get_current_lesson(self, course_uid, uid):
        """ Gib die aktuelle Lektion zurück """

    def get_current_parent(self, course_uid, current):
        """ """

    def get_slides(self):
        """ """

    def get_page_images(self):
        """
        Gib eine Liste alle Bilder des Kurses zurück
        """

    def get_current_childs(self, course_uid, current):
        """ """

    def get_navigation(self, uid):
        """ """

    def build_learner_group_id(self):
        """ """

    def get_complete_tree(self):
        """ """

    def go_to(self, page):
        """
        Springe auf Seite
        """

    def get_related_group_desktop_group_id(self):
        """ """

    def create_associated_groups(self):
        """
        Erzeuge die zugeordneten Gruppen
        """

    def canViewDocuments(self):
        """
        Darf der angemeldete Benutzer die Kursdokumente sehen?
        """

    def authViewDocuments(self):
        """
        Wirf ggf. Unauthorized
        """

    def canEdit():
        """
        Darf der angemeldete Benutzer den Kurs bearbeiten?
        """

    def getDocumentsInfo(self, context):
        """
        Gib die Information über die Kursdokumente zurück
        """

    def get_uid():
        """
        Rettungsfunktion: wenn der Request eine komische UID enthält,
        extrahiere diese ggf. aus einer fälschlich übergebenen URL
        """


def cache__get_as_list(method, self):
    """
    Gib ein Tupel aus Änderungsdatum und UID (als Cache-Schlüssel) zurück
    """
    context = self.context
    pc = context.getAdapter('pc')()
    return str(context.modified()), context.UID(), pc.getCounter()


class Browser(BrowserView):

    implements(IUnitraccCourseBrowser)

    @log_or_trace(**lot_kwargs)
    def get_level(self):
        """
        Gib die auswählbaren Einträge der aktuellen Hierarchieebene
        zurück
        """
        context = self.context
        pc = context.getAdapter('pc')()
        partof = None
        query = {
            'path': {'query': context.getPath(),
                     'depth': 1,
                     },
            'review_state': ['inherit', 'restricted',
                             'visible', 'published',
                             ],
            'sort_on': 'sortable_title',
            }
        try:
            if context.portal_type == 'Plone Site':
                # die "ersten" n werden für das Menü verwendet,
                # also ist die Reihenmfolge hier interessant;
                # auf dieser Ebene nur Ordner ausgeben: 
                query['portal_type'] = 'Folder'
                # (nur für Menü- und Krümelgenerierung:) 
                # query['getExcludeFromNav'] = False
            else:
                # Code aus tomcom.adapter "getbrain":
                uid = context.UID()
                brains = pc._catalog(UID=uid)
                if brains:
                    if brains[1:]:
                        logger.error('.get_level: %d hits for UID %r!', len(brains), uid)
                    else:
                        # innerhalb von Strukturelementen ist die logische Reihenfolge wichtig;
                        # das Strukturelement selbst hat als partOf-Wert seine eigene UID:  
                        partof = brains[0].getPartOf
                        if partof:
                            query['sort_on'] = 'getObjPositionInParent'
                else:
                    logger.error('no hit for UID %r (context=%r, portal_type=%r',
                                 uid, context, context.portal_type)
        except AttributeError as e:
            logger.exception(e)
            logger.error('%r lacks attribute %r', context, e.args[0])

        # Nota bene: nach 'getExcludeFromNav' wird hier NICHT gefiltert,
        # damit z. B. Fragebögen zwar für die Verwendung in Kursen
        # ausgewählt werden können, aber nicht im Suchergebnis der
        # Vorträge auftauchen!
        if debug_active:
            logger.info('get_level(%r), partof=%r, query=\n%s',
                        context, partof, pformat(query))
        return pc(query)

    @log_or_trace(**lot_kwargs)
    def get_current(self, uid=None):

        context = self.context

        if not uid:
            form = context.REQUEST.form
            uid = form.get('uid', None)

        if not uid:
            portal = context.getAdapter('portal')()
            logger.info('%(context)r.get_current: returning %(portal)r',
                        locals())
            return portal

        rc = context.getAdapter('rc')()
        res = rc.lookupObject(uid)
        if res:
            return res
        logger.error('%(context)r.get_current: rc.lookupObject(%(uid)r) failed!',
                     locals())
        # Plan B: 
        pc = context.getAdapter('pc')()
        brains = pc._catalog(UID=uid)
        if brains:
            if brains[1:]:
                logger.error('%r.get_current: %d hits for UID %r!',
                             context,
                             len(brains), uid)
            return brains[0]
        else:
            logger.error('%r.get_current: no hit for UID %r!',
                         uid, context)

    def crumbs(self):

        context = self.context

        parents = [brain
                   for brain in context.getAdapter('aqparents')()
                   if brain.is_folderish
                   ]
        parents.reverse()
        return parents

    def is_folderish(self, brain):

        if brain.portal_type in ['Folder']:
            return True

    def set(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        xml = form.get('xml', '')
        if xml:
            xml = '''<?xml version="1.0" encoding="utf-8"?><root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">''' + xml + '</root>'

        context.setHtml_left(form.get('html_left', ''))
        context.setHtml_right(form.get('html_right', ''))
        self._validate_course_memberships(str(context.getXml()), str(xml))

        context.setXml(xml)
        context.reindexObject()

    def _validate_course_memberships(self, xml_old, xml_new):
        """ """
        context = self.context
        list_old = []
        if xml_old:
            list_old = self._parse(xml_old)

        list_new = self._parse(xml_new)
        groups = context.getBrowser('groups')
        unitraccgroups = context.getBrowser('unitraccgroups')
        course_group_id = self.build_learner_group_id()
        sg = context.getAdapter('acl')().source_groups

        for dict_ in list_old:
            current_group_id = unitraccgroups.buildStructureGroupName(dict_['uid_object'], 'Reader')
            group = groups.getById(current_group_id)
            if group:
                if course_group_id in group.getMemberIds():
                    sg.removePrincipalFromGroup(course_group_id, current_group_id)

        for dict_ in list_new:
            current_group_id = unitraccgroups.buildStructureGroupName(dict_['uid_object'], 'Reader')
            group = groups.getById(current_group_id)
            if group and course_group_id not in group.getMemberIds():
                group.addMember(course_group_id)

    def _get_learner_group_prefix(self):
        """
        *obsolet*
        """
        return LEARNER_SUFFIX

    def build_learner_group_id(self):
        """
        Ermittle die UID des Kontexts und gib die entsprechende Lerngruppen-ID zurück
        """

        context = self.context
        return learner_group_id(context.UID())

    def create_associated_groups(self):
        """
        Erzeuge die zugeordneten Gruppen
        """
        context = self.context
        myuid = context.UID()
        mytitle = context.Title()
        if not mytitle:
            return
        ggibi = groupinfo_factory(context, pretty=False, forlist=True)
        _add = []
        _rg = []

        for suffix in (u'learner', u'alumni'):
            gid = generic_group_id(myuid, suffix)
            dic = ggibi(gid)
            if not dic:
                _add.append((gid,
                             safe_decode(mytitle) + u' ' + suffix,
                             ))
                if suffix == u'learner':
                    _rg.append((gid, 'Reader'))
                elif suffix == u'alumni':
                    _rg.append((gid, 'UnitraccAlumnus'))
        if _add:
            print '_add =', _add
            groups = context.getBrowser('groups')
            for tup in _add:
                groups.add(*tup)
        if _rg:
            for gid, role in _rg:
                context.manage_setLocalRoles(gid, [role])

    def get_first(self):

        list_ = self.get_course_structure()
        if list_:
            return list_[0]

    def get_prev_and_next(self, current_uid):
        """ get Previous and Next element from the current"""
        list_ = self.get_course_structure()
        for foil in list_:
            if foil['uid_object'] == current_uid:
                index = foil['index']
                if index == len(list_) - 1:
                    comes = None
                else:
                    comes = list_[index + 1]
                prev = list_[index - 1]
                if index == 0:
                    prev = None

                res = {'prev': prev,
                       'next': comes}
                return res

    def get_last(self):

        list_ = self.get_course_structure()
        if list_:
            return list_[-1]

    def get_course_page_count(self):

        return len(self.get_course_structure())

    def get_item_position(self, dict_):

        return dict_['index'] + 1

    @ram.cache(cache__get_as_list)
    def _get_as_list(self):

        context = self.context
        xml = None
        try:
            xml = str(context.getXml())
        except AttributeError as e:
            logger.error('%(context)r: no attribute getXml (%(e)r)!',
                         locals())
            logger.exception(e)
            xml = None
        finally:
            if not xml:
                logger.error('Kein Kursinhalt fuer %(context)r gefunden!', locals())
                return []

        return self._parse(xml)

    @log_or_trace(debug_active, logger=logger)
    def _parse(self, xml):
        """
        Gib eine Liste von Dicts zurück
        """
        # Parse xml. Output is a list with dictionaries.
        context = self.context
        getbrain = context.getAdapter('getbrain')
        tree = cET.fromstring(xml)
        list_ = []
        counter = 0
        deleted = 0
        # import pdb; pdb.set_trace(); print 'Siehe Zeile 402, portal_type'
        for elementElement in tree.findall('.//element'):
            dict_ = {}
            dict_['uid_object'] = elementElement.findtext('uid_object').strip()
            dict_['uid_parent'] = elementElement.findtext('uid_parent').strip()
            # TH: die werden doch unten alle überschrieben, oder?!
            dict_['uid_next'] = elementElement.findtext('uid_next').strip()
            dict_['uid_prev'] = elementElement.findtext('uid_prev').strip()
            elementProperties = elementElement.find('properties')
            val = elementProperties.findtext('portal_type')
            if val:
                dict_['portal_type'] = val.strip()
            else:
                dict_['portal_type'] = None
                logger.warning('Element %r ohne portal_type! (%s)', elementElement, dict_)
            if debug_active:
                pp(elementElement, dict_)
                if not counter:
                    pp(elementElement, dir(elementElement))
            dict_['index'] = counter

            if dict_['portal_type'] == 'UnitraccLesson':
                dict_['title'] = elementProperties.findtext('title').strip()
                dict_['duration'] = elementProperties.findtext('duration').strip()
                dict_['summary'] = elementProperties.findtext('summary').strip()
                dict_['objective'] = elementProperties.findtext('objective').strip()
            else:
                try:
                    target_brain = getbrain(dict_['uid_object'])
                    dict_['title'] = target_brain.Title
                except AttributeError, e:
                    deleted += 1  # mutmaßlich im Vortrag gelöschte Folie:
                    continue     # ignorieren!

            list_.append(dict_)

            counter += 1

        DEBUG('%(context)r: %(counter)d elements', locals())
        if deleted:
            DEBUG('%(context)r: %(deleted)d elements apparently deleted', locals())

        for dic, prev_i, curr_i, next_i in inject_indexes(list_):
            if prev_i is None:
                dic['uid_prev'] = ''
            else:
                dic['uid_prev'] = list_[prev_i]['uid_object']
            if next_i is None:
                dic['uid_next'] = ''
            else:
                dic['uid_next'] = list_[next_i]['uid_object']

        return list_

    def get_course_structure(self):

        context = self.context

        # XXX global?! Wahrscheinlich problematisch!
        global mapping_

        list_ = self._get_as_list()
        # XXX TH: zugewiesener Wert wird nicht verwendet! Zweck?
        #     TH: Zweck ist mutmaßlich ein Caching der *kompletten* Struktur
        #         mit der Kurs-UID als Cache-Schlüssel; wird noch nicht gemacht.
        context_uid = context.UID()
        for dict_ in list_:
            mapping_[dict_['uid_object']] = dict_

        return list_

    def element_item_info(self, course_uid, element_uid):
        """
        XXX dringend mal dokumentieren!
        """
        res = None
        if element_uid:
            try:
                res = mapping_[element_uid]
            except KeyError:
                logger.info('no element_item_info for element %(element_uid)r', locals())
            else:
                if res:
                    return res
                else:
                    logger.info('element_item_info is %(res)r for element %(element_uid)r', locals())
        else:
            logger.info('element_item_info(%(course_uid)r, %(element_uid)r): trying course ...', locals())
        res = mapping_.get(course_uid)
        if res:
            logger.info('element_item_info is %(res)r for *course* uid %(course_uid)r', locals())
        else:
            logger.warn('element_item_info is %(res)r for *course* uid %(course_uid)r!', locals())
            raise Redirect('/resolveuid/%(course_uid)s' % locals())
        return res

    def load(self):
        """ """
        context = self.context
        json = context.getBrowser('json')

        dict_ = {}
        dict_['html_left'] = str(context.getHtml_left())
        dict_['html_right'] = str(context.getHtml_right())
        dict_['xml'] = str(context.getXml())

        return json.encode(dict_)

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

            query['portal_type'] = ['UnitraccCourse']
            query['getExcludeFromSearch'] = False
            query['sort_on'] = 'getObjPositionInParent'

            query['review_state'] = ['visible', 'inherit',
                                     'published', 'restricted']

            brains = pc(query)
        finally:
            sm.setOld()

        return brains

    # @trace_this
    def get_visible_courses(self):
        """
        Buchbare *und kostenlose* Kurse
        """
        context = self.context
        rc = context.getAdapter('rc')()
        res = []
        price = None
        durat = None
        for brain in self.search():
            uid = brain.UID
            try:
                course_obj = rc.lookupObject(uid)
                price = course_obj.getPrice_shop()
                extract_float(course_obj.getPrice_shop())
                durat = course_obj.getShopduration()
                float(course_obj.getShopduration())
            except Exception, e:
                price = course_obj.getPrice()
            else:
                res.append(brain)
                price = None
                durat = None
        return res

    def get_brain_by_uid(self, uid=None):

        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            form = context.REQUEST.form

            if not uid:
                uid = form.get('uid', None)

            if not uid:
                portal = context.getAdapter('portal')()
                return portal

            rc = context.getAdapter('rc')()
            object_ = rc.lookupObject(uid)
            brain = object_.getHereAsBrain()
            return brain
        finally:
            sm.setOld()

    @ram.cache(cache__get_as_list)
    def get_ppt_navigation(self):

        context = self.context
        list_ = []
        for dict_ in self.get_course_structure():
            dict_ = dict(dict_)

            if dict_.get('uid_parent'):
                uid_parent = dict_['uid_parent']
                counter = 1
                while uid_parent:
                    parent = mapping_[uid_parent]
                    if parent.get('uid_parent'):
                        uid_parent = parent['uid_parent']
                        counter += 1
                    else:
                        uid_parent = None
                dict_['level'] = counter
            else:
                dict_['level'] = 0

            list_.append(dict_)

        return list_

    @log_or_trace(**lot_kwargs)
    def get_content(self, prefix, current, course_url=None):
        """
        prefix -- z.B. 'js-page-' (ruft mit current['portal_type'] == 'Document'
                  -> js-page-document.pt auf)
        current -- ein dict
        """
        DEBUG('get_content(%(prefix)r, %(current)r)', locals())
        context = self.context
        portal_type = current['portal_type']
        template_name = prefix + portal_type.lower()
        # print '@@unitracccourse.get_content ->', template_name
        DEBUG('... template_name = %(template_name)r)', locals())
        return context.restrictedTraverse(template_name)(current=current,
                                                         course_url=course_url)

    def get_agenda(self, uid):
        """ """
        context = self.context
        list_ = self.get_ppt_navigation()
        agenda = self.get_navigation(uid, list_)

        def handle_childs(agenda_point):
            """
            Gehe durch alle Punkte und Prüfe
            ob nur Ordner/Lektionen vorhanden sind
            """
            list_of_childs = []
            for child in agenda_point['childs']:
                if not child['portal_type'] in ["UnitraccLesson", "Folder"]:
                    continue
                else:
                    if child['childs']:
                        if child['class'] == 'navigation-current':
                            child['childs'] = []
                        else:
                            child['childs'] = handle_childs(child)
                        list_of_childs.append(child)
                    else:
                        list_of_childs.append(child)
            return list_of_childs

        for agenda_point in agenda:
            if agenda_point['childs']:
                if agenda_point['class'] == 'navigation-current':
                    child['childs'] = []
                else:
                    agenda_point['childs'] = handle_childs(agenda_point)
        return agenda

    def get_current_lesson(self, course_uid, uid):
        """
        Gib die aktuelle Lektion zurück
        """
        # XXX: Argumente schlecht benannt: uid, ein Dict?!
        # XXX: erstes Argument course_uid wird nicht verwendet
        context = self.context
        try:
            if uid['portal_type'] == "UnitraccLesson":
                return uid
        except (TypeError, KeyError):
            logger.error('%(context)r.get_current_lesson(%(course_uid)r,'
                         ' %(uid)r): kein portal_type!',
                         locals())
            raise
        index = uid['index']
        if index == 0:
            return uid

        list_ = self.get_course_structure()
        range_list = range(0, index)
        range_list.reverse()
        for counter in range_list:
            if list_[counter]['portal_type'] in ['UnitraccLesson']:
                return list_[counter]

        return uid

    def get_current_parent(self, course_uid, current):

        context = self.context
        if current is None:
            DEBUG('get_current_parent(%(context)r, %(course_uid)r, %(current)r)',
                  locals())
        else:
            DEBUG('get_current_parent(%(context)r, %(course_uid)r, current)',
                  locals())
            if debug_active:
                logger.info('mit current=\n' + pformat(current))

        try:
            index = current['index']
            if index == 0:
                return current
        except TypeError as e:
            logger.error('get_current_parent(%(context)r, %(course_uid)r, %(current)r):'
                         ' current ist None; return!',
                         locals())
            return current  # pep 20.2

        """
        >>> index=5
        >>> list(range(index-1, -1, -1))
        [4, 3, 2, 1, 0]
        """
        range_list = list(range(index-1, -1, -1))
        list_ = self.get_course_structure()
        # gib den letzten Vorgänger passenden Typs zurück:
        for counter in range_list:
            if list_[counter]['portal_type'] in ['Folder', 'UnitraccLesson']:
                return list_[counter]
        return current

    def get_current_childs(self, course_uid, current):

        context = self.context
        list_ = self.get_course_structure()
        index = current['index']

        range_list = range(0, len(list_))

        childs = []
        for counter in range_list:
            dict_ = dict(list_[counter])
            if dict_['uid_parent'] == current['uid_object']:
                childs.append(dict_)
        return childs

    def current_to_object(self, current):

        context = self.context
        rc = context.getAdapter('rc')()

        # print '@@unitracccourse.current_to_object -> rc.lookupObject %(uid_object)r' % current
        return rc.lookupObject(current['uid_object'])

    def get_slides(self):
        """
        Gib eine Liste aller Folien des Kurses zurück (für Thumbnail-Ansicht)
        """
        context = self.context
        list_ = []
        getbrain = context.getAdapter('getbrain')
        book_templates = context.getBrowser('book').getBookTemplates()
        partsOf = {}

        for dict_ in self.get_ppt_navigation():
            dict_ = dict(dict_)
            target_brain = getbrain(dict_['uid_object'])
            if target_brain:
                uid = target_brain.getPartOf
                if uid:
                    if not partsOf.has_key(uid):
                        partsOf[uid] = getbrain(uid)

                    if partsOf[uid].getLayout not in book_templates:
                        dict_['url'] = './resolveUid/' + dict_['uid_object'] + '/@@viewpreview/get'

            if not dict_.get('url', ''):
                dict_['url'] = '/++resource++unitracc-images/slides_thumbnail_default.png'

            list_.append(dict_)

        return list_

    def get_page_images(self):
        """
        Gib eine Liste alle Bilder des Kurses zurück
        """

        context = self.context

        getbrain = context.getAdapter('getbrain')

        list_ = []

        logger.debug('%(context)r.get_page_images():'
                     ' get_ppt_navigation aufrufen ...',
                     locals())
        navi = self.get_ppt_navigation()
        logger.debug('%r.get_page_images(): navi, len: %d',
                     context, len(navi))

        for dict_ in navi:
            if dict_['portal_type'] == 'Document':
                target_brain = getbrain(dict_['uid_object'])
                text = safe_decode(target_brain.getRawText)
                soup = BeautifulSoup(text)
                for img in soup.find_all('img'):
                    try:
                        src = img.attrs['src']
                    except KeyError:
                        continue
                    else:
                        uid = extract_uid(src)
                        if uid is not None:
                            list_.append((dict_, uid))
        return list_

    def get_navigation(self, uid, list_=None):
        """
        Gib die Navigation für den Präsentationsmodus zurück
        """
        # TODO: dokumentieren!

        context = self.context
        # CHECKME: Besser vergleichen mit None, oder?!
        if not list_:
            list_ = self.get_ppt_navigation()
        # Alle erst einmal auf nicht aktiv, davon gibt es immer nur eins, das aktuelle Element
        # children sind für den aufbau des Baumes

        mapping_ = {}
        parent_children = {}
        for dict_ in list_:
            dict_['active'] = False
            dict_['childs'] = []
            dict_['class'] = ''
            mapping_[dict_['uid_object']] = dict_

            if not parent_children.has_key(dict_['uid_parent']):
                parent_children[dict_['uid_parent']] = []
            parent_children[dict_['uid_parent']].append(dict_)

        # XXX hier hat es schon geknallt (KeyError, für uid != None).
        #     Was ist, wenn <uid> im <mapping_> nicht vorkommt?!
        #     Jira: UNITRACC-752
        # ------------------- [ mutmaßlich unschädlich ... [
        # (was nicht wie eine UID aussieht,
        #  ist vermutlich eine kleine Ganzzahl)
        if not looksLikeAUID(uid):
            logger.warn('get_navigation(uid=%(uid)s); versuche Extraktion',
                        locals())
            val = extract_uid_from_qs(uid)
            if looksLikeAUID(val):
                uid = val
            # XXX Was passiert, wenn wir hier eine Zahl bekommen?!
        # ------------------- ] ... mutmaßlich unschädlich ]
        try:
            current = mapping_[uid]
        except KeyError:
            if list_:
                logger.error('get_navigation(uid=%(uid)s); Liste vorhanden',
                             locals())
                current = list_[0]
            else:
                logger.error('get_navigation(uid=%(uid)s): leere Liste!',
                             locals())
                return []
                current = None

        # Aktiv für das aktuelle
        current['active'] = True
        current['class'] = 'navigation-current'
        parent = mapping_.get(current['uid_parent'], None)

        # Wenn current Ordnerartig dann Inhalte einfügen
        if current['portal_type'] in ['Folder', 'UnitraccLesson']:
            uid = current['uid_object']
            current['childs'].extend(parent_children.get(uid, []))

        if not parent:
            return parent_children[current['uid_parent']]

        parent['class'] = 'navigation-open'
        # Ein Navigationsbaum besteht immer nur aus den ausgeklappten elementen der Navigierten Ebenen.
        # Sprich den Elternelementen des navigierten Pfades und Ihrer Inhalte
        parent['childs'].extend(parent_children[parent['uid_object']])
        while parent:
            if mapping_.has_key(parent['uid_parent']):
                parent = mapping_[parent['uid_parent']]
                parent['class'] = 'navigation-open'
                parent['childs'].extend(parent_children[parent['uid_object']])
            else:
                return parent_children[parent['uid_parent']]

    def get_complete_tree(self):

        context = self.context
        list_ = self.get_ppt_navigation()
        getbrain = context.getAdapter('getbrain')

        lessons = []
        mapping_ = {}
        for dict_ in list_:
            dict_['active'] = False
            dict_['childs'] = []
            dict_['class'] = ''
            mapping_[dict_['uid_object']] = dict_
            if dict_['portal_type'] == 'UnitraccLesson':
                lessons.append(dict_)
            else:
                dict_['current'] = getbrain(dict_['uid_object'])

        for dict_ in list_:
            if dict_['uid_parent']:
                mapping_[dict_['uid_parent']]['childs'].append(dict_)

        return lessons

    def go_to(self):
        """
        Springe auf Seite
        """

        context = self.context
        form = context.REQUEST.form
        rc = context.getAdapter('rc')()
        cuid = form.get('uid')
        self.context = rc.lookupObject(cuid)
        pages = self.get_course_structure()
        view = form.get('view')
        page = form.get('page')
        ajax = form.get('ajax')

        try:
            page = int(page)
        except:
            return None
        if 0 < page <= len(pages):
            page = pages[page - 1]['uid_object']
        else:
            return None
        if not ajax:
            url = self.context.absolute_url() + "/" + view + "?uid=%s" % page
            return context.REQUEST.response.redirect(url)

        return demjson.encode({'uid': page})

    def get_related_group_desktop_group_id(self, group_id=None):

        context = self.context

        groupbrowser = context.getBrowser('groups')
        groupsharing = context.getBrowser('groupsharing')

        if not group_id:
            group_id = self.build_learner_group_id()

        group = groupbrowser.getById(group_id)

        for dict_ in groupsharing.get_explicit_group_memberships(group_id):
            if dict_['type'] == 'group':
                if dict_['group_desktop']:
                    return dict_['id']
        return ''

    def canViewDocuments(self):
        """
        Darf der angemeldete Benutzer die Kursdokumente sehen?
        """
        context = self.context
        pm = getToolByName(context, 'portal_membership')
        return pm.checkPermission(Access_course_documents, context)

    def authViewDocuments(self):
        """
        Wirf ggf. Unauthorized
        """
        if not self.canViewDocuments():
            raise Unauthorized

    def canEdit(self):
        """
        Darf der angemeldete Benutzer den Kurs bearbeiten?
        """
        context = self.context
        pm = getToolByName(context, 'portal_membership')
        return pm.checkPermission(ModifyPortalContent, context)

    def getDocumentsInfo(self, context):
        """
        Gib die Information über die Kursdokumente zurück
        """
        context = self.getContext()
        import pdb; pdb.set_trace()
        getAdapter = context.getAdapter
        if not getAdapter('checkperm')(Access_course_documents):
            raise Unauthorized
        portal = getAdapter('portal')
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            res = {'title': safe_decode(context.getTitle()),
                   'text': None,
                   'main_template': context.restrictedTraverse('main_template'),
                   }
            text = context.getCourse_documents_text()
            if text:
                transform = getAdapter('transform').get
                res['text'] = transform(text)
            return res
        finally:
            sm.setOld()

    def get_uid(self):
        """
        Rettungsfunktion: wenn der Request eine komische UID enthält,
        extrahiere diese ggf. aus einer fälschlich übergebenen URL

        Wenn die Aufrufe dieser Methode bei erschöpfenden Tests nicht mehr protokolliert
        werden, können sie eliminiert und durch ein einfaches Auslesen der Formulardaten
        ersetzt werden.
        """
        context = self.context
        request = context.REQUEST
        form = request.form
        uid = form.get('uid')
        if uid:
            # wenn etwas als "uid" übergeben wurde, wird es genommen!
            if looksLikeAUID(uid):
                return uid
            logger.warn('@@unitracccourse.get_uid(%(uid)r)', locals())
            try:
                number = int(uid)
            except ValueError:
                logger.warn('...get_uid (2): %(uid)r ist keine Zahl', locals())
            else:
                logger.warn('...get_uid (3): gebe Zahl %(number)r zurueck', locals())
                return number

            val = extract_uid_from_qs(uid)
            if val is not None:
                if looksLikeAUID(val):
                    logger.warn('...get_uid (4): uid %(val)r extrahiert', locals())
                else:
                    if not isinstance(val, basestring):
                        pp(val=val, uid=uid)
                        import pdb; pdb.set_trace()
                    if val.startswith('uid-'):
                        tail = val[4:]
                        if looksLikeAUID(tail):
                            logger.warn('...get_uid (5): uid %(val)r extrahiert', locals())
                        else:
                            logger.warn('...get_uid (6): "uid" %(val)r extrahiert', locals())
                        return tail
                    else:
                        logger.warn('...get_uid (7): "uid" %(val)r extrahiert', locals())
                return val
            elif 1:
                pass
            elif qsdict:
                logger.warn('...get_uid (10): Query string ohne uid! (%s)',
                            (qsdict.keys(),
                             ))
        else:  # nichts als "uid" übergeben
            return None
        logger.warn('...get_uid (50): Was soll ich damit anfangen?!')
        import pdb; pdb.set_trace()
        return uid
