# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß
# siehe --> LIESMICH.txt

# Plone/Zope/dayta:
from dayta.browser.public import BrowserView, implements, Interface
from AccessControl import Unauthorized
from Products.CMFCore.utils import _checkPermission
from Products.CMFCore.permissions import (
        AccessInactivePortalContent,
        ModifyPortalContent,  # 'Modify portal content'
        )

# Standardmodule:
from re import compile as compile_re
from DateTime import DateTime
from json import dumps as json_dumps

# Dieser Browser:
from .utils import (normalizeQueryString, lsfactory_portal, create_lsfactory,
        create_flatlsfactory,
        )
from .data import (localsearch_presets_default, layout_to_action_suffix,
        localsearch_json_presets_default, localsearch_json_default,
        FORBIDDEN_BRAIN_ATTRIBUTES, DATATABLES_TEMPLATE, DISPLAY_ITEM_MACROS,
        )
from .crumbs import OK

# Andere Browser:
from ..unitraccsettings.utils import vanilla_factory

# Unitracc-Tools:
from ...tools.debug import asciibox
from visaplan.tools.debug import log_or_trace, pp
from visaplan.plone.tools.log import getLogSupport
from visaplan.tools.dicts import updated
from visaplan.tools.lands0 import groupstring
from ...tools.forms import make_input
from ...tools.search import queries_nonthumbnail_types_only
from visaplan.tools.classes import make_proxy
from ...tools.misc import make_names_tupelizer, make_dict_sequencer
from ...tools.forms import tryagain_url, back_to_referer
from ...tools.context import make_permissionChecker
from visaplan.plone.tools.setup import make_reindexer

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport(defaultFromDevMode=1)
from pprint import pformat

from ...tools.context import make_userdetector
watched_user = make_userdetector(('therp',))
from pdb import set_trace

lot_kwargs = {'debug_level': debug_active,
              'logger': logger,
              'trace': debug_active >= 2,
              }
from Globals import DevelopmentMode

# qua Vorgabe als system-Benutzer suchen:
AS_SYSTEM_USER = True

lsfactory = create_lsfactory(get_okey=True)
# Funktion, die etwaige fehlerhafte Attributnamen ausfiltert:
normal_names_tuple = make_names_tupelizer(FORBIDDEN_BRAIN_ATTRIBUTES,
                                          onerror='remove',
                                          logger=logger)
dict_factory = create_flatlsfactory(normal_names_tuple)
# Ein Dict., Namensliste --> Funktion(brain --> dict)
make_dict4json = make_proxy(dict_factory,
                            normalize=normal_names_tuple)
dict_to_dicts_sequence = make_dict_sequencer(firstkey='default',
                                             key='key',
                                             val_key='val',
                                             selected_key='selected')

class IUnitraccSearch(Interface):

    def search(self):
        """ """

    def search_in_structures(self):
        """
        Suche innerhalb von Büchern/Präsentationen/Kursen
        """

    def getLocalsearch_jsondata(self, raw=False, limit=None,
                                asdict=False,
                                **dump_kwargs):
        """
        Gib das Ergebnis der Lokalen Suche als JSON-codierte Liste zurück

        siehe (gf) templates/localsearch_json.js.pt

        limit -- eine Zahl > 0, zur Einschränkung auf die ersten <limit> Suchergebnisse
        raw -- Ergebnis unformatiert zurückgeben
        asdict -- gib ein Dict mit folgenden Schlüsseln zurück:
            result_length -- die Anzahl der gefundenen Objekte
            data -- das Ergebnis, nach Maßgabe von limit und raw
        **dump_kwargs -- für json_dumps, z. B. indent=2
        """

    def getCustomSearch(self):
        """ """

    def transformGetCode(self):
        """ """

    def getSearchInArea(self):
        """ """

    def getAreaOfInterest():
        """
        Gib das Wurzelelement der "lokalen Suche" zurück

        Rückgabewert ist ein dict mit den Schlüsseln "uid" und "o"
        oder None.
        """

    def getItemMacroChoices():
        """
        für templates/manage_localsearch_json_preset.pt
        """

    def inheritedLocalSearch(self):
        """
        Wie --> getAreaOfInterest, aber:
        - nur für den Kontext
        - gibt ein dict mit folgenden Schlüsseln zurück;
          'root' -- wie Rückgabe von getAreaOfInterest
          'data' -- immer vorhanden; None oder ein Dict
          'distance' -- eine Ganzzahl >= 0
                        (immer dann garantiert vorhanden, wenn 'data' nicht None ist)
        """

    def getLocalSearch(self):
        """
        Lies die konfigurierten Filterkriterien für den (anhand einer UID)
        übergebenen oder den aktuellen Kontext aus

        (wenn die UID nicht übergeben wird oder "False" ist, wird sie aus dem
        Kontext ermittelt)

        (in ./templates/configure_localsearch.pt der "konfigurierte Wert";
        siehe --> createLocalQuery)
        """

    def getLocalSearchHiddenInput(self, **kwargs):
        """
        Erzeuge ein oder mehrere hidden-Eingabefelder für die Parameter der
        lokalen Suche;
        gib None oder einen HTML-String zurück
        """

    def formatInputData(self, data):
        """
        Gib die übergebenen Formulardaten als Eingabefelder zurück (ein Stríng,
        mit structure-Prefix zu verwenden).

        Rückgabewert wie von --> getLocalSearchHiddenInput
        """

    def setLocalSearch(self):
        """ """

    def chooseJsonPreset(self):
        """
        Eine JSON-Konfiguration persistent auswählen.
        """

    def getCheckedSearchIn(self):
        """ """

    def getCheckedSearchInGlobal(self):
        """ """

    def result(self):
        """ """

    def getlocalsearchPreset(self):
        """
        Gib ein Dictionary der konfigurierten Sichten bzw. Makros zurück
        """

    def getLocalsearchPresetsVocabulary(self):
        """
        Gib die Auswahlmöglichkeiten für die Lokale Suche zurück.

        Aus Sicherheitsgründen kann es natürlich nicht erlaubt werden,
        daß normalsterbliche Anwender die Verwendung konkreter Sichten
        und Makros anfordern; deshalb gibt es vorgefertigte
        Konfigurationen (Presets), die namentlich ausgewählt werden
        können.
        """

    def list_local(self, **kwargs):
        """
        Suche Objekte im aktuellen Ordner.
        Suchkriterien können als benannte Argumente übergeben werden.
        """

    def createLocalQuery(self):
        """
        Wenn eine lokale Suche konfiguriert ist, gib die konfigurierten
        Parameter zurück (inheritedLocalSearch()['data']), mit den üblichen
        Ergänzungen (soweit nicht unterdrückt).

        Aus getLocalsearch_kwargs ausgekoppelt, um bei Konfiguration der
        Lokalen Suche genauer zu wissen, was passiert (d.h. incl. impliziter
        Ergänzungen).

        (in ./templates/configure_localsearch.pt der "effektive Wert";
        siehe --> getLocalSearch)
        """

    def getLocalsearch_kwargs(self):
        """
        Gib das kwargs-Dict. zurück für den Aufruf von
        --> ./templates/localsearch_listing.pt
        """

    def getLocalSearches(self, **kwargs):
        """
        Gib die "lokalen Suchen" der Unterseiten des Kontexts zurück
        """

    def getReviewStates(label_key='title'):
        """
        Gib die Arbeitsablauf-Statuus zurück

        (eine dict-Liste mit den Schlüsseln 'id' und 'title')
        """

    def getActionURL(**kwargs):
        """
        Gib die URL zurück, die für das action-Attribut des <form>-Elements
        verwendet werden soll.
        """

    def getJsonPresetsManageFormData():
        """
        Gib die Daten für das Bearbeitungsformular der Presets zurück,
        und nimm ggf. die geforderten Änderungen vor
        """

    def refreshBrain():
        """
        Aktualisiere das Katslogobjekt des Kontexts
        """

    def canRefreshBrains(self):
        """
        Darf der angemeldete Benutzer Katalogobjekte erneuern? (Wahrheitswert zurückgeben)
        """

    def authRefreshBrains(self):
        """
        Wirf Unauthorized ...
        """
        if not self.canRefreshBrains():
            raise Unauthorized


class Browser(BrowserView):

    implements(IUnitraccSearch)

    storageKey = 'localsearch'

    def canRefreshBrains(self):
        """
        Darf der angemeldete Benutzer Katalogobjekte erneuern?
        """
        check = make_permissionChecker(self.context, verbose=True)
        for perm in (ModifyPortalContent,
                     ):
            if check(perm):
                return True
        return False

    def authRefreshBrains(self):
        """
        Wirf Unauthorized ...
        """
        if not self.canRefreshBrains():
            raise Unauthorized

    def search(self, personal=False, related=False):  # [ search ... [
        """
        Build Querys to search for content with given criterias.

        personal -- auch eigene Objekte des angemeldeten Benutzers finden
                    und dabei excludeFromSearch ignorieren

        related -- nur mit personal: auch über Gruppen vermittelte
                   Eigentümerschaft auflösen; ansonsten wird das
                   Creator-Attribut geprüft

        (beide sind nur wirksam, wenn ein Benutzer angemeldet ist, also nicht
        bei sog. "anonymer Suche"
        """
        context = self.context

        getAdapter = context.getAdapter
        pc = getAdapter('pc')()
        industrialsector = context.getBrowser('industrialsector')

        form = context.REQUEST.form
        wuid = watched_user(getAdapter=getAdapter, getid=True)
        if wuid:
            DBG = logger.info
            DBG('@search(), watched user: %(wuid)r'
                    '\n\tpersonal: %(personal)r'
                    '\n\trelated: %(related)r'
                    , locals())
            # set_trace()
        else:
            DBG = DEBUG
        ldebug = debug_active or bool(wuid)
        if ldebug:
            DBG('@search(), Formulardaten:\n%s', pformat(form))

        # --------------------------------------------- ... search ...
        DBG('search(personal=%r, related=%r);\n   form=%s',
              personal, related, pformat(form))

        query = {
            'review_state': ['inherit',
                             'published',
                             'visible',
                             'restricted',
                             ]
            }
        if context.getAdapter('isanon')():
            query['getExcludeFromSearch'] = False
        else:
            query['review_state'].append('restricted')
            if personal:
                # Search for all personal related content
                # even if excluded from search.
                query['review_state'].append('private')

                # check for own content
                author = self.context.getAdapter('auth')()
                if not related:
                    query['Creator'] = author.getId()
                # query['contributors'] = [author.UID]
            else:
                # Only check for non personal related content
                # that is not excluded from search.
                query['getExcludeFromSearch'] = False
        # --------------------------------------------- ... search ...

        # --------------------------- [ SearchableText, sort_on ... [
        SearchableText = form.get('SearchableText', '')
        DBG('search: SearchableText (1) = %(SearchableText)r', locals())
        queryList = normalizeQueryString(SearchableText)
        DBG('search: queryList (2.nQS) = %(queryList)r', locals())

        if queryList:
            query['SearchableText'] = queryList
            sort_default = None  # --> Ausgabe nach Relevanz!
        else:
            sort_default = 'sortable_title'
        sort_on = form.get('sort_on', sort_default)
        if sort_on:
            query['sort_on'] = sort_on
            query['sort_order'] = form.get('sort_order', '')
        # --------------------------- ] ... SearchableText, sort_on ]

        # --------------------------------- [ Fachbereichssuche ... [
        # TODO: diese Funktionität mit einer oder zwei geeigneten Methoden
        #       des Browsers industrialsector erledigen
        # Wenn der Request "code1" enthält, wurde das Formular der
        # Fachbereichssuche verwendet; in diesem Fall wird ein etwaiges
        # getCode ignoriert.
        # Wenn code2 oder code3 leer ist, kann der letzte gefüllte
        # Code mehrere Schlüssel enthalten.
        code1 = form.get('code1', [])
        getCode = form.get('getCode')
        codeslist = []
        if code1:
            DBG('Fachbereichsangaben aus Formular')
            if getCode:
                logger.warn('code1 gefunden (%s); getCode (%s) wird ignoriert',
                            code1, getCode)
            codeslist = []
            code2 = form.get('code2')
        # --------------------------------------------- ... search ...
            if code2:
                code3 = form.get('code3')
                if code3:
                    DBG('Fachbereichstiefe: 3 (%s %s ...)',
                          code1, code2)
                    prefix = code1[0] + code2[0]
                    for code in code3:
                        if len(code) == 2:  # immer so erwartet!
                            codeslist.append(prefix + code)
                        else:               # sicherheitshalber
                            codeslist.extend(industrialsector.search(prefix + code + '*'))
                else:
                    DBG('Fachbereichstiefe: 2 (%s ...)',
                          code1)
                    prefix = code1[0]
                    for code in code2:
                        codeslist.extend(industrialsector.search(prefix + code + '*'))
            else:
                DBG('Fachbereichstiefe: 1 (%s)', code1)
                for code in code1:
                    if code == '_':
                        if codeslist:
                            del codeslist[:]
                        break
                    codeslist.extend(industrialsector.search(code + '*'))
        elif getCode:
            DBG('Fachbereichsangabe aus Link: %r', getCode)
            if len(getCode) < 6 and not getCode.endswith('*'):
                getCode += '*'
                DBG('ergaenze ein Asterisk --> %r', getCode)
            codeslist = industrialsector.search(getCode)

        # --------------------------------------------- ... search ...
        if codeslist:
            DBG('Fachbereichssuche nach %s', codeslist)
            query['getCode'] = {'query': codeslist,
                                'operator': 'or'}
        # --------------------------------- ] ... Fachbereichssuche ]

        searchIn = form.get('searchIn', '')  # eine UID
        search_mediathek = False
        # --------------------------------- [ zu suchende Typen ... [
        customSearch = [value
                        for value in form.get('getCustomSearch', [])
                        if value
                        ]
        if customSearch:  # aus Suchformular
            DBG('Typen aus Formular: %s', customSearch)
            query['getCustomSearch'] = {'query': customSearch,
                                        'operator': 'or'}
        else:
            localCustomSearch = self.getLocalSearch(searchIn)
            if localCustomSearch:
                DBG('Typen lokal konfiguriert fuer %s:\n%s',
                      searchIn and ('UID %s' % searchIn)
                               or 'Kontext',
                      pformat(localCustomSearch))
                # vermutlich zu umständlich, aber erstmal so
                # beibehalten:
                localCustomSearch['getCustomSearch'] = {
                        'query': localCustomSearch['getCustomSearch'],
                        'operator': 'or'}
                DBG('localCustomSearch nach Transformation (Schluessel %s):\n%s',
                      localCustomSearch.keys(),
                      pformat(localCustomSearch))
                query.update(localCustomSearch)
                if searchIn:
                    search_mediathek = True

        # --------------------------------------------- ... search ...
            else:
                DBG('Typen gem. globaler Konfiguration')
                query['getCustomSearch'] = {
                        'query': [pair[0]
                                  for pair in self.getCustomSearch()
                                  ],
                        'operator': 'or'}
        # --------------------------------- ] ... zu suchende Typen ]

        # ------------------------------------------ [ searchIn ... [
        if searchIn == 'root':
            if 'path' in query:
                deleted_path = query.pop('path')
                DBG('searchIn == %(searchIn)r --> deleted path %(deleted_path)r',
                    locals())
        else:
            paths = []
            if search_mediathek:
                mediathek_path = context.getBrowser('mediathek').getMediathekPath()
                DBG('mediathek_path = %(mediathek_path)r',
                    locals())
                if mediathek_path:
                    paths.append(mediathek_path)
            if looksLikeAUID(searchIn):
                getbrain = getAdapter('getbrain')()
                brain = getbrain(searchIn)
                if brain:
                    paths.append(brain.getPath())
                else:
                    logger.error('"searchIn" root UID %(searchin)r not found',
                                 locals())
            else:
                paths.append(searchIn)
            if paths:
                query['path'] = paths
        # ------------------------------------------ ] ... searchIn ]

        # ------------------- [ Veröffentlichungsdatum beachten ... [
        # siehe (gf):
        # ../../../../parts/omelette/Products/CMFPlone/CatalogTool.py
        show_inactive = form.get('show_inactive', False)
        if show_inactive:  # TH 30.03.2017: noch ungetestet
            show_inactive = _checkPermission(AccessInactivePortalContent, self)
            if not show_inactive:
                logger.error("Can't show inactive entries!")
        if not show_inactive:
            query['effective'] = {'query': DateTime(),
                                  'range': 'max'}
        # ------------------- ] ... Veröffentlichungsdatum beachten ]

        DBG('search: query=%s', pformat(query))
        try:
            res = pc(query)
            DBG('%d Treffer', len(res))
            if debug_active:
                pp(res=res)
            return res

            return pc(query)
        except UnicodeEncodeError as e:
            dest, txt, start, end, msg = e.args
            logger.error('Encoding fehlgeschlagen (-> %(dest)s, msg: %(msg)s', locals())
            logger.error('Zeichen %d: %r', start, txt[start:end])
            logger.error('(max.) %d Zeichen davor: %r', 20, txt[start-20:start])
            logger.exception(e)
            raise
        # --------------------------------------------- ] ... search ]

    def search_in_structures(self, portal=None):
        """
        Suche innerhalb von Büchern/Präsentationen/Kursen
        portal = Plattformmodus andere Ausgabe
        """
        context = self.context
        form = context.REQUEST.form
        getAdapter = context.getAdapter
        pc = getAdapter('pc')()
        rc = getAdapter('rc')()
        root_uid = form.get('uid')

        template_id = form.get('template_id')
        if template_id and template_id.endswith('.pt'):
            template_id = template_id[:-3]

        wuid = watched_user(getAdapter=getAdapter, getid=True)
        if wuid:
            DBG = logger.info
            DBG('@search_in_structures(), watched user: %(wuid)r'
                    '\n\ttemplate_id: %(template_id)r', locals())
            # set_trace()
        else:
            DBG = DEBUG
        ldebug = debug_active or bool(wuid)
        if ldebug:
            DBG('@search_in_structures(), Formulardaten:\n%s', pformat(form))

        query = {}

        kw = {'context': context,
              }
        # Falls Kurs suche nach UIDs
        in_course = bool(form.get('portal_type') or form.get('course'))
        if in_course:
            DBG('Kurs erkannt')
            cb = context.getBrowser('unitracccourse')
            course = rc.lookupObject(root_uid)
            list_ = cb._parse(str(course.getXml()))
            uids = [x['uid_object']
                    for x in list_
                    if len(x['uid_object']) > 1
                    ]
            # nicht für Suche verwendet:
            path = course.getPath()
            """
            Suche nach UIDs für Objekte in Kurs
            """
            query['UID'] = uids
        # Strukturtyp suche über path angabe
        else:
            DBG('Kein Kurs erkannt, also normaler Vortrag')
            folder = rc.lookupObject(root_uid)
            path = folder.getPath()
            query['path'] = path + "/"
        if template_id:
            path_s = path.split('/')
            # ID des Plone-Portalobjekts ('unitracc' oder 'vdz') entfernen:
            topseg = path_s.pop(1)
            path_s.append(template_id)
            kw['path'] = '/'.join(path_s)
            kw['url_suffix'] = 'template_id='+template_id
            if template_id == 'ppt_view':  # *nicht* für course_ppt_view!
                kw['uid_prefix'] = 'uid-'

        # Suchstring Handling
        SearchableText = form.get('SearchableText', '')
        DBG('search_in_structures: SearchableText (1) = %(SearchableText)r', locals())
        queryList = normalizeQueryString(SearchableText)
        DBG('search_in_structures: queryList (2.nQS) = %(queryList)r', locals())
        if queryList:
            query['SearchableText'] = queryList
            sort_default = None  # --> Ausgabe nach Relevanz!
        else:
            sort_default = 'sortable_title'
        sort_on = form.get('sort_on', sort_default)
        if sort_on:
            query['sort_on'] = sort_on
            query['sort_order'] = form.get('sort_order', '')

        result = pc(query)
        if ldebug:
            DBG('search_in_structures,'
                  '\n  watched user=%r,'
                  '\n  query:\n%s'
                  '\n  len(result), raw: %d',
                    wuid,
                    pformat(query),
                    len(result))
        result = [x
                  for x in result
                  if x.UID != root_uid
                  ]
        if portal or form.get('course'):
            # ../../skins/unitracc_templates/kss-search-result.pt
            tid = 'kss-search-result'  # mit Sortierung und Paging
        else:
            # ../../skins/unitracc_templates/search-result-ppt.pt
            tid = 'search-result-ppt'  # nur eine einfache Liste
        kw['brains'] = result
        if ldebug:
            DBG('search_in_structures,'
                  '\nportal=%r,'
                  '\nform.get(course)=%r,'
                  '\nin_course=%r,'
                  '\ntid=%r',
                  portal,
                  form.get('course'),
                  in_course,
                  tid)
        string_ = context.restrictedTraverse(tid)(**kw)
        if ldebug:
            print string_
        return string_

    def searchQs(self):
        """
        Search Querys
        Creating the Search Query to lookup for no personal related content
        and to look up personal related content.
        """
        # Get general result
        nonpersonal = self.search()
        # Check if we need to check for personal stuff
        # if not self.context.getAdapter('isanon')():

        # Get self created content
        # personal = self.search(True)
        # return personal + nonpersonal

        return nonpersonal

    def getCustomSearch(self):
        context = self.context
        return context.getBrowser('unitracctype').getAllSearchableTypes()

    def transformGetCode(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        string_ = form.get('getCode')

        dict_ = {}

        if not string_:
            return dict_

        industrialsector = context.getBrowser('industrialsector')
        list_ = industrialsector.search(string_)

        if list_:
            for i in range(1, (len(list_[0]) / 2) + 1):
                dict_['code' + str(i)] = []

        for string_ in list_:
            values = groupstring(string_, 2)
            for i in range(len(values)):
                if values[i] not in dict_['code' + str(i + 1)]:
                    dict_['code' + str(i + 1)].append(values[i])
        return dict_

    def getSearchInArea(self):
        """ """
        context = self.context
        if context.portal_type == "UnitraccCourse":
            return context.getHereAsBrain()
        aqparents = context.getAdapter('aqparents')()

        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')
        data = settings.get(self.storageKey, {})

        if len(aqparents) > 1:
            for parent in aqparents:
                if data.has_key(parent.UID):
                    return parent

    def getAreaOfInterest(self):
        """
        Gib das Wurzelelement der "lokalen Suche" zurück

        Rückgabewert ist ein dict mit den Schlüsseln "uid" und "o",
        mit dem bislang einzigen Schlüssel 'brain',
        oder None.
        """
        # TODO: Brains und etwaige UIDs (aus Request) verarbeiten;
        #       siehe ../../skins/unitracc_templates/search_view.pt
        context = self.context
        pt = context.portal_type
        if pt == "UnitraccCourse":
            brain = context.getHereAsBrain()
            return {'brain': brain,
                    # (noch?) kein entsprechendes Katalog-Metadatum:
                    # 'path': brain.getPath,
                    }
        elif pt == 'Plone Site':
            return None
        getAdapter = context.getAdapter
        aqparents = getAdapter('aqparents')()

        portal = getAdapter('portal')()
        settings = portal.getBrowser('settings')
        data = settings.get('localsearch', {})

        for parent in aqparents:
            uid = parent.UID
            if data.has_key(uid):
                return {'o': parent,
                        'uid': uid,
                        'path': parent.getPath(),
                        }
        return None  # pep 20.2

    # -------------------------------- [ Konfiguration speichern ... [
    def setLocalSearch(self):
        """
        Speichere die Änderungen der Lokalen Suche.
        """
        return self._setLocalSettings(self.storageKey)

    def setJsonSettings(self):
        """
        Parameter für die JSON-generierte DataTables-Ausgabe

        (wenn die UID nicht übergeben wird oder "False" ist, wird sie aus dem
        Kontext ermittelt)

        Siehe ./templates/configure_localsearch.pt
        """
        # pp(form=self.REQUEST.form)
        return self._setLocalSettings('localsearch_json')

    def chooseJsonPreset(self):
        """
        Eine JSON-Konfiguration persistent auswählen.

        Siehe ./templates/configure_localsearch_json.pt
        """
        # pp(form=self.context.REQUEST.form)
        return self._setLocalSettings('localsearch_json_preset')

    def _setLocalSettings(self, storage_key, **kwargs):
        """
        Das Web-Formular enthält die Änderungen üblicherweise für *ein* Objekt
        (Top-Level-Schlüssel: die UID).

        Für jede UID wird ein Python-Dict in den Formulardaten erwartet;
        Schlüssel, die in den/dem jeweilgen Dict(s) fehlen, werden aus den
        gespeicherten Daten entfernt.

        Siehe ./templates/configure_localsearch.pt
        """
        # TODO: Locking (siehe Modul fcntl sowie die Klasse MaintenanceLock,
        # ../../../../scripts/itools/control.py
        context = self.context

        context.getBrowser('authorized').managePortal()

        form = context.REQUEST.form
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')
        message = context.getAdapter('message')

        data = settings.get(storage_key, {})
        uid = context.UID()

        data.update(form)

        if not form:
            if data.has_key(context.UID()):
                del data[context.UID()]

        # pp(storage_key, data)
        settings._set(storage_key, data)

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])
    # -------------------------------- ] ... Konfiguration speichern ]

    # ------------------------------------ [ Konfiguration lesen ... [
    @log_or_trace(**lot_kwargs)
    def getLocalSearch(self, uid=''):
        """
        Lies die konfigurierten Filterkriterien für den (anhand einer UID)
        übergebenen oder den aktuellen Kontext aus

        (wenn die UID nicht übergeben wird oder "False" ist, wird sie aus dem
        Kontext ermittelt)

        (in ./templates/configure_localsearch.pt der "konfigurierte Wert")
        """
        return self._getLocalSettings(self.storageKey, uid=uid)

    @log_or_trace(**lot_kwargs)
    def getJsonSettings(self, uid=''):
        """
        Parameter für die JSON-generierte DataTables-Ausgabe

        (wenn die UID nicht übergeben wird oder "False" ist, wird sie aus dem
        Kontext ermittelt)
        """
        context = self.context
        settings = context.getBrowser('unitraccsettings')
        preset_key = settings._getInherited('localsearch_json_preset',
                                            factory=vanilla_factory,
                                            default='default')
        presets = self.getJsonPresets(forform=False)
        try:
            # pp(presets=presets, preset_key=preset_key)
            if not isinstance(preset_key, basestring):
                preset_key = 'default'
            dic = dict(presets[preset_key])
            dic['key'] = preset_key
            return dic
        except KeyError as e:
            logger.error('%(context)r: No display preset %(preset_key)r found!',
                         locals())
            return localsearch_json_default

    def getJsonPreset(self):
        """
        Der Name der zu verwendenden JSON-Konfiguration;
        templates/configure_localsearch_json.pt

        Gegenstück: --> chooseJsonPreset
        """
        return self._getLocalSettings('localsearch_json_preset',
                                      default='default')

    @log_or_trace(**updated(lot_kwargs, trace=0))
    def getJsonPresets(self, forform=True):
        """
        Zur Auswahl einer JSON-Konfiguration zur Lokalen Suche; gf:
        templates/configure_localsearch_json.pt

        forform -- wenn True (Vorgabe; Aufruf durch Formular),
                   Rückgabe als Liste von Dicts (für Auswahlformular);
                   ansonsten das rohe konfigurierte Dict.
        """
        dic = self._getPortalSettings('localsearch_json_presets',
                                      default=localsearch_json_presets_default)
        if not forform:
            return dic
        current = self.getJsonPreset()
        return list(dict_to_dicts_sequence(dic, curval=current))

    @log_or_trace(**lot_kwargs)
    # @log_or_trace(**updated(lot_kwargs, trace=1))
    def getJsonPresetsManageFormData(self):
        """
        Gib die Daten für das Bearbeitungsformular der Presets zurück,
        und nimm ggf. die geforderten Änderungen vor
        """
        tag = 'gJPMFD'  # Abkürzung, für Logging
        all_presets = self.getJsonPresets(forform=False)  # sic!
        # pp(all_presets=all_presets)
        context = self.context
        context.getBrowser('authorized').managePortal()
        getAdapter = context.getAdapter
        message = getAdapter('message')
        form = context.REQUEST.form
        preset_data = None
        errors = 0
        preset_name = form.get('preset_name', None)
        if preset_name:
            preset_name = preset_name.strip()
        save_action = form.get('save_action', None)
        """
        Aktionen:
        edit - Bearbeitungsformular (Vorgabe, wenn Name angegeben)
        create - Bearbeitungsformular für neues Preset

        Formulardaten:
        action - Die Aktion (s.o.)
        preset_data:record - die zu speichernden Daten
        save_action - 'Save', 'Create' oder 'Delete'
        """
        url = None
        action = form.get('action', None)
        res = {'preset_name': preset_name,
               }
        if action in (None, 'edit'):
            if preset_name:
                preset_data = all_presets.get(preset_name, {})
                if preset_data:
                    res['preset_data'] = preset_data
                    if action is None:
                        action = 'edit'
                else:
                    if action == 'edit':
                        message('Preset "${preset_name}" not found!',
                                'error',
                                mapping=locals())
                        errors += 1
                    else:
                        action = 'create'
            elif action == 'edit':
                action = 'create'
            elif 0:
                message('Please specify a preset!',
                        'error')
                errors += 1
        # Formular für neues Preset:
        if save_action is None:
            if action == 'edit':
                save_action = 'Save'
            elif action == 'create':
                save_action = 'Create'
            else:
                action = 'list'
                res['preset_names'] = all_presets.keys()
                res['current_presets'] = liz = []
                for key, dic in all_presets.items():
                    liz.append({'name': key,
                                'label': dic.get('label', key),
                                })
            res['save_action'] = save_action
            res['form_action'] = action
            return res

        q_items = []
        q_kw = {'url': '/manage_localsearch_json_preset',
                'context': context,
                }
        if not preset_name:
            logger.error('%(tag)s, save_action=(save_action)r: no preset_name',
                         locals())
            message('Please specify a preset!',
                    'error')
            errors += 1

        if errors:
            return back_to_referer(**q_kw)

        portal = getAdapter('portal')()
        settings = portal.getBrowser('settings')
        if save_action == 'Delete':
            if preset_name == 'default':
                message("Won't delete preset \"${preset_name}\"!",
                        'error',
                        mapping=locals())
                errors += 1
                q_items.append(('action', 'list'))
            try:
                del all_presets['preset_name']
            except KeyError:
                message('No preset ${preset_name} found.',
                        'warning',
                        mapping=locals())
            else:
                settings._set('localsearch_json_presets',
                              all_presets)
                message('Preset "${preset_name}" deleted.',
                        mapping=locals())
            q_items.append(('action', 'list'))
        else:
            if save_action == 'Create':
                if preset_name in all_presets:
                    message('Preset "${preset_name}" already found!',
                            'error',
                            mapping=locals())
                    errors += 1
            elif save_action != 'Save':
                message('Invalid save action "${save_action}"!',
                        'error',
                        mapping=locals())
                errors += 1
            all_presets.update({
                preset_name: form['preset'],
            })
            if not errors:
                settings._set('localsearch_json_presets',
                              all_presets)
                if save_action == 'Create':
                    message('Preset "${preset_name}" created.',
                            mapping=locals())
                else:
                    message('Preset "${preset_name}" saved.',
                            mapping=locals())
        return back_to_referer(items=q_items, **q_kw)

    def getItemMacroChoices(self):
        """
        für templates/manage_localsearch_json_preset.pt
        """
        return DISPLAY_ITEM_MACROS

    def _getLocalSettings(self, storage_key, **kwargs):
        """
        Ermittle lokal erwartete Konfiguration, z. B.:
        * 'localsearch'
        * 'localsearch_json'
        """
        context = self.context
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')
        data = settings.get(storage_key, {})
        uid = kwargs.pop('uid', None)
        default = kwargs.pop('default', {})

        if not uid:
            try:
                uid = context.getUID()
            except AttributeError as e:  # Auf Rootebene
                return None

        return data.get(uid, default)

    @log_or_trace(**lot_kwargs)
    def inheritedLocalSearch(self):
        """
        Wie --> getAreaOfInterest, aber:
        - nur für den Kontext
        - gibt ein dict mit folgenden Schlüsseln zurück;
          'root' -- wie Rückgabe von getAreaOfInterest
          'data' -- immer vorhanden; None oder ein Dict
          'distance' -- eine Ganzzahl >= 0
                        (immer dann garantiert vorhanden, wenn 'data' nicht None ist)
        """
        context = self.context
        return context.getBrowser('unitraccsettings')._getInherited(
                'localsearch',
                factory=lsfactory,
                factory_portal=lsfactory_portal,
                default={'data': None})

    def inherited_json_options(self):
        """
        zur Ergänzung von inheritedLocalSearch:
        gibt die Optionen zurück für den Fall, daß das Suchergebnis als
        JSON-Daten zurückgegeben wird.
        """
        context = self.context
        return context.getBrowser('unitraccsettings')._getInherited(
                'localsearch_json',
                factory=lsfactory,
                default={'data': None})

    def _getLocalsearchPresets(self, **kwargs):
        """
        Gib die gespeicherten (oder Standard-) Presets zurück.

        Aus Sicherheitsgründen kann es natürlich nicht erlaubt werden,
        daß normalsterbliche Anwender die Verwendung konkreter Sichten
        und Makros anfordern; deshalb gibt es vorgefertigte
        Konfigurationen (Presets), die namentlich ausgewählt werden
        können.
        """
        return self._getPortalSettings('localsearch_preset_choices',
                                       default=localsearch_presets_default,
                                       **kwargs)

    def _getPortalSettings(self, storage_key, **kwargs):
        context = kwargs.pop('context', None)
        if context is None:
            context = self.context
        default = kwargs.pop('default', None)
        portal = context.getAdapter('portal')()
        settings = portal.getBrowser('settings')
        dic = settings.get(storage_key, None)
        if dic is None:
            # kopieren, wg. etwaiger pop-Aktion in aufrufender Methode
            dic = dict(default)
        return dic
    # ------------------------------------ ] ... Konfiguration lesen ]

    @log_or_trace(**lot_kwargs)
    def getLocalSearchHiddenInput(self, **kwargs):
        """
        Erzeuge ein oder mehrere hidden-Eingabefelder für die Parameter der
        lokalen Suche;
        gib None oder einen HTML-String zurück

        CHECKME: obsolet?
        """
        if 'uid' in kwargs:
            uid = kwargs.pop('uid')
        elif 'ls_root' in kwargs:  # von --> getAreaOfInterest
            ls_root = kwargs.pop('ls_root')
            if ls_root:
                # hier interessieren wir uns nicht für Katalogobjekte:
                uid = ls_root.pop('uid', None)
            else:
                uid = None
        else:
            context = self.context
            uid = context.getUID()
        if kwargs:
            raise TypeError('Surplus / unknown arguments: %r'
                            % (kwargs,))
        if uid is None:
            return None
        data = self.getLocalSearch(uid=uid)
        if data:
            return make_input(data)
        return None  # pep 20.1

    @log_or_trace(**lot_kwargs)
    def formatInputData(self, data):
        """
        Gib die übergebenen Formulardaten als Eingabefelder zurück (ein Stríng,
        mit structure-Prefix zu verwenden).

        Rückgabewert wie von --> getLocalSearchHiddenInput;
        Eingabe von --> inheritedLocalSearch()['data']
        """
        if data:
            return make_input(data)
        return None  # pep 20.1

    def getCheckedSearchIn(self):
        """ """
        context = self.context
        form = context.REQUEST.form

        if form.has_key('searchIn'):
            if form.get('searchIn') and form.get('searchIn') != 'root':
                return True
            else:
                return False
        else:
            return True

    def getCheckedSearchInGlobal(self):
        """ """
        context = self.context
        form = context.REQUEST.form

        if form.has_key('searchIn'):
            if form.get('searchIn') == 'root':
                return True
            else:
                return False

    def result(self):
        """ """
        context = self.context
        string_ = ''
        try:
            res = {'brains': self.search()}
            string_ = context.restrictedTraverse('kss-search-result')(**res)
        except Unauthorized:
            string_ = "Unauthorized"
        except UnicodeEncodeError as e:
            dest, txt, start, end, msg = e.args
            logger.error('Encoding fehlgeschlagen (-> %(dest)s, msg: %(msg)s', locals())
            logger.error('Zeichen %d: %r', start, txt[start:end])
            logger.error('(max.) %d Zeichen davor: %r', 20, txt[start-20:start])
            logger.exception(e)
            string_ = "ENCODING ERROR"
        # finales "except Exception" würde den Ort des Fehlers maskieren!
        finally:
            return string_

    # ------------------------ [ Konfiguration der Lokalen Suche ... [
    def getLocalsearchPresetsVocabulary(self):
        """
        Gib die Auswahlmöglichkeiten für die Lokale Suche zurück
        """
        dic = self._getLocalsearchPresets()
        res = [('', '')]
        default = dic.pop('default')
        res.append(('default', default['label']))
        for key in dic:
            res.append(key, dic[key]['label'])
        return res
    # ------------------------ ] ... Konfiguration der Lokalen Suche ]

    # ------------------------ [ Konfiguration der JSON-Optionen ... [
    # (angepaßte Kopie, --> Konfiguration der Lokalen Suche)
    def getLocalsearchJsonPresetsVocabulary(self):
        """
        Die Auswahlmöglichkeiten für die Lokale Suche zurück (JSON-Ausgabe)
        """
        dic = self._getLocalsearchPresets()
        res = [('', '')]
        default = dic.pop('default')
        res.append(('default', default['label']))
        for key in dic:
            res.append(key, dic[key]['label'])
        return res
    # ------------------------ ] ... Konfiguration der JSON-Optionen ]

    @log_or_trace(**lot_kwargs)
    def getlocalsearchPreset(self):
        """
        Gib ein Dictionary der konfigurierten Sichten bzw. Makros zurück

        Schlüssel:
        spec -- die ermittelte Spezifikation (ein Dict)
        func -- ein Dict mit denselben Schlüsseln wie spec, aber
                aufgelöst zu Templates und Makros
        """
        context = self.context
        request = context.REQUEST
        form = request.form
        try:
            preset_key = form['localsearch_preset']
        except KeyError:
            preset_key = None
        if not preset_key:
            preset_key = 'default'

        # Die Formularvariable wird erwartet, darf aber leer sein:
        presets = self._getLocalsearchPresets(context=context)
        find_template = context.restrictedTraverse
        spec = presets[preset_key]
        func = {}
        for key, val in spec.items():
            if key == 'label':  # nur für getLocalsearchPresetsVocabulary
                continue
            # direkte Suche nach Makros mit restrictedTraverse
            # zeitigte Unauthorized-Fehler; also manuelle Auflösung:
            liz = val.split('/macros/', 1)
            name = liz.pop(0)
            tmpl = find_template(name)
            if liz:
                func[key] = tmpl['macros'][liz[0]]
            else:
                func[key] = tmpl
        return {'spec': spec,
                'func': func,
                }

    def list_local(self, **kwargs):
        """
        Suche Objekte im aktuellen Ordner.
        Suchkriterien können als benannte Argumente übergeben werden.
        """
        context = self.context
        query = {'path': context.getPath(),
                 'getExcludeFromSearch': False,
                 }
        query.update(kwargs)
        pc = context.getAdapter('pc')()
        postprocess = 1
        if not postprocess:
            return pc(query)
        res = []
        makedict = (context.REQUEST.get('year_column', False)
                    and custom_rowdict1
                    or  custom_rowdict0)
        for brain in pc(query):
            res.append(makedict(brain))
        return res

    def _resolve_path_args(self, query, **kwargs):
        """
        Modifiziere das Abfrage-Dict. <query> gemäß den übergebenen Schlüsselwort-Argumenten.
        Ausgewertet werden:

        root (optional) - die Vorgabe für die Suche nach 'path'
        path - ein Pfad '/unitracc/...', oder 'NOPATH', oder 'SPEC'
        path_spec - verwendet, wenn SPEC angegeben
        """
        default_root = kwargs.pop('root', None)  # wird immer übergeben
        if default_root is None:
            default_root = self.context.getPath()
            logger.info('_resolve_path_args: default_root --> %(default_root)', locals())
        path_raw = kwargs.pop('path', None)
        path_spec = kwargs.pop('path_spec', None)
        if path_raw == '.':
            query['path'] = default_root
        elif path_raw == '..':
            query['path'] = '/'.join(default_root.split('/')[:-1])
        elif path_raw == 'NOPATH':
            pass
        elif path_raw == 'SPEC':
            if path_spec:
                query['path'] = path_spec
            else:
                logger.warning('_cLQ: path=%(path_raw)r, '
                               'aber path_spec ist leer!', locals())
        elif not path_raw:  # Vorgabe verwenden
            query['path'] = default_root
        else:
            logger.warning('_rPA: was tun mit path=%(path_raw)r, '
                           'path_spec=%(path_spec)r?', locals())
        if 'root' in query:
            del query['root']
        if 'path_spec' in query:
            del query['path_spec']

    @log_or_trace(**lot_kwargs)
    def _createLocalQuery(self, **kwargs):
        """
        Erzeuge die Argumente für eine Katalogsuche;
        aufgerufen von --> createLocalQuery

        Alle Argumente müssen benannt übergeben werden;
        außerdem werden folgende Formularfelder ggf. verwendet:
        - SearchableText
        """
        context = self.context
        form = context.REQUEST.form

        """ "auskommentiert":
            'portal_type': ['Folder', # ggf. unten überschrieben
                            'UnitraccAnimation',
                            ],
        """
        query = {
            # 'getExcludeFromNav': False,
            'getExcludeFromSearch': False,
            # 'sort_on': 'getObjPositionInParent',
            'review_state': ['visible', 'inherit',
                             'published', 'restricted'],
            'effective': {'query': DateTime(),
                          'range': 'max'},
            }
        self._resolve_path_args(query, **kwargs)

        # -------------------------- [ getCustomSearch ... [
        # erst eine Liste erzeugen ...
        gcs = kwargs.pop('getCustomSearch', None)
        gcs_op = 'or'
        gcs_list = []
        if gcs is not None:
            if isinstance(gcs, basestring):
                if gcs:
                    gcs_list.append(gcs)
            elif gcs:
                gcs_list.extend([item
                            for item in gcs
                            if item
                            ])
        # ... dann etwaige Ergänzungen:
        val = form.get('source')
        if val:
            if gcs_list[1:]:
                logger.warning('getCustomSearch %(gcs_list)s zur '
                               '%(gcs_op)s-Kombination mit source %(val)s!',
                               locals())
            else:
                gcs_op = 'and'
            # aus ../standard/browser.py, search:
            gcs_list.append('source=%(val)s' % locals())
        # ... und schließlich finalisieren:
        if gcs_list[1:]:
            query['getCustomSearch'] = {
                    'query': gcs_list,
                    'operator': gcs_op,
                    }
        elif gcs_list:
            query['getCustomSearch'] = gcs_list[0]
        # -------------------------- ] ... getCustomSearch ]

        # --------------- [ direkt übernehmbare Felder ... [
        # TODO: language --> Language
        # (benötigt, wenn standard_folder_view.pt und @@standard/search
        # substituiert werden)
        for key in ('portal_type',  # z. B. 'UnitraccStandard'
                    'Subject',
                    'sort_on',
                    ):
            val = form.get(key)
            if val:
                try:
                    val = val.strip()
                    if not val:
                        continue
                except (AttributeError, TypeError):
                    pass
                query[key] = val
        # --------------- ] ... direkt übernehmbare Felder ]

        # --------------------- [ allgemeine Textsuche ... [
        queryString = form.get('SearchableText')
        if queryString:
            query['SearchableText'] = queryString

        # diese wurde durch ._resolve_path_args() erledigt:
        for donekey in ['path',
                        'path_spec',
                        'root',
                        ]:
            try:
                del kwargs[donekey]
            except KeyError:
                pass

        if kwargs:
            # pp(query=query)
            # pp('restliche Argumente', kwargs)
            query.update(kwargs)
            queryString = query.get('SearchableText')
        # pp(query=query)

        if queryString:
            # txng/lightsearch sorgt für safe_decode-Aufruf
            DEBUG('search: queryString (1) = %(queryString)r', locals())
            txng = context.getBrowser('txng')
            queryString = txng.processWords(queryString).strip()
            DEBUG('search: queryString (2.txng) = %(queryString)r', locals())

        if queryString:
            queryString = '*' + queryString + '*'
            query['SearchableText'] = queryString
            DEBUG('search: queryString (3) = %(queryString)r', locals())
            # pp(query=query)
        elif 'SearchableText' in query:
            DEBUG('search: queryString (4): deleting "SearchableText" %(SearchableText)r', query)
            del query['SearchableText']
            # pp(query=query)
        # --------------------- ] ... allgemeine Textsuche ]
        return query

    # @log_or_trace(**updated(lot_kwargs, trace=1))
    @log_or_trace(**lot_kwargs)
    def createLocalQuery(self):
        """
        Wenn eine lokale Suche konfiguriert ist, gib die konfigurierten
        Parameter zurück (inheritedLocalSearch()['data']), mit den üblichen
        Ergänzungen (soweit nicht unterdrückt).

        Aus getLocalsearch_kwargs ausgekoppelt, um bei Konfiguration der
        Lokalen Suche genauer zu wissen, was passiert (d.h. incl. impliziter
        Ergänzungen).

        (in ./templates/configure_localsearch.pt der "effektive Wert";
        siehe --> getLocalSearch)
        """
        # Suchargumente:
        ils = self.inheritedLocalSearch()
        # pp(ils=ils)
        root = ils.get('root')
        if not root:
            root = None
        else:
            root = root['path']

        data = ils.get('data') or {}
        # ils['data'] enthält jetzt getCustomSearch
        query = self._createLocalQuery(
                root=root,
                **data)
                # getCustomSearch=gcs)
        if query.pop('override_workflow', False) and 'review_state' in query:
            del query['review_state']
        return query

    def getLocalsearch_kwargs(self):
        """
        Gib das kwargs-Dict. zurück für den Aufruf von
        --> ./templates/localsearch_listing.pt
        """
        query = self.createLocalQuery()
        context = self.context
        getAdapter = context.getAdapter
        portal = getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            # ausführbare Templates:
            dic = self.getlocalsearchPreset()
            # Suche durchführen:
            dic['brains'] = query and getAdapter('pc')()(query) or []
            # nur für Entwicklungszwecke:
            dic['query'] = query
            # mit enthaltenen Makros wird diese Ausgabe sehr (!) lang,
            # außerdem natürlich mit 'brains':
            dic['with_thumbnails'] = not queries_nonthumbnail_types_only(query)
            return dic
        finally:
            sm.setOld()

    @log_or_trace(**lot_kwargs)
    def getLocalsearch_jsondata(self, raw=False, limit=None,
                                asdict=False,
                                **dump_kwargs):
        """
        Gib das Ergebnis der Lokalen Suche als JSON-codierte Liste zurück

        siehe (gf) templates/localsearch_json.js.pt

        limit -- eine Zahl > 0, zur Einschränkung auf die ersten <limit> Suchergebnisse
        raw -- Ergebnis unformatiert zurückgeben
        asdict -- gib ein Dict mit folgenden Schlüsseln zurück:
            result_length -- die Anzahl der gefundenen Objekte
            data -- das Ergebnis, nach Maßgabe von limit und raw
        **dump_kwargs -- für json_dumps, z. B. indent=2
        """
        query = self.createLocalQuery()
	if not query:
	    return '[]'
        context = self.context
        getAdapter = context.getAdapter
        getBrowser = context.getBrowser
        portal = getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            jsonopt = self.getJsonSettings()
            names = jsonopt['names']
            lang = getAdapter('langcode')()

            # dictfactory = make_dict4json[names, lang]
            dictfactory = make_dict4json[names]

            # Suche durchführen:
            brains = getAdapter('pc')()(query) or []
            res = [dictfactory(brain)
                   for brain in brains
                   ]
            if limit is None:
                pass
            elif limit <= 0:
                raise ValueError('limit - if given - must be a number > 0 (%(limit)r'
                                 % locals())
            elif not asdict:
                del res[limit:]
            if asdict:
                dic = {'result_length': len(res),
                       }
                if limit is not None:
                    del res[limit:]
                if raw:
                    dic['data'] = res
                else:
                    dic['data'] = json_dumps(res, **dump_kwargs)
                return dic
            if raw:
                return res
            return json_dumps(res, **dump_kwargs)
        except KeyError as e:
            logger.error('%(context)r.getLocalsearch_jsondata(%(raw)r) FAILED',
                         locals())
            logger.exception(e)
            res = []
            if raw:
                return res
            return '[]'
        finally:
            sm.setOld()

    def getLocalSearch_jscode(self):
        """
        Erzeugt den Javascript-Code für die lokale Datatables-Konfiguration;
        siehe (gf) templates/localsearch_datatables.js.pt
        (eingebunden von templates/localsearch_ajax_view.pt)
        """
        jsonopt = self.getJsonSettings()
        # TODO: Anzahl der Datensätze in deferRender-Option
        spice = self.getLocalsearch_jsondata(
            # limit=500 and 11,
            # indent=2,
            asdict=True)
        jsonopt.update(spice)
        # pp(jsonopt)
        # return DATATABLES_TEMPLATE % jsonopt

        txt = """\
$(document).ready(function () {
    $.each($('.datatb-ajax'),
        function (i, v) {
            // i - Index
            // v - das Tabellenobjekt (Herleitung des Namens?)
            var options = Unitracc.datatables_config(i, v);
            options.data = %(data)s;
            options.columns = %(columns)s;
            options.deferRender = true;
            options.deferLoading = %(result_length)s;
            console.log(options);
            $(v).dataTable(options);
        }
    );
});
""" % jsonopt
        # pp(txt)

        return txt
        """  // funktioniert so noch nicht:
            var table = $(v).dataTable(options);
            table.ajax.url('localsearch_json.js').load();
        """

    @log_or_trace(**lot_kwargs)
    def getLocalSearches(self, **kwargs):
        """
        Gib die "lokalen Suchen" der Unterseiten des Kontexts zurück

        Argumente:
        - uids -- eine Sequenz der UIDs der entsprechenden Seiten
          (optional; wenn nicht angegeben, wird die nächste Menüebene des Kontexts ermittelt)
        - exclude_uids -- alternativ: die UIDs explizit auszuschließender Unterseiten
        - maxcount - die maximale Anzahl jeweils zurückzugebender Brains
        - execute - soll die Suche ausgeführt werden? (Vorgabe: ja)
        - getmenulevel_kwargs - wenn nicht <uids> angegeben, die Argumente zur
          Ermittlung der Kindelemente ("Untermenüpunkte")

        Rückgabe: ein Dict mit den Schlüsseln:
        - 'kwargs' - die übergebenen Argumente
        - 'maxcount' - der angegebene oder vorgabegemäße Wert
        - 'children' - eine Sequenz der "Kindelemente", mit den Schlüsseln:
          - 'title' - die Überschrift
          - 'brains' - wenn <execute>
          - 'query' - die jeweilige Abfrage (zu Entwicklungszwecken)
          - 'uid' - die UID
          - 'config_url' - der Pfad zur jeweiligen Konfigurationsseite (configure_localsearch),
            wenn die lokale Suche für die jeweige UID nicht konfiguriert ist, oder None
        """
        res = {'kwargs': dict(kwargs),
               'children': [],
               }
        maxcount = kwargs.pop('maxcount', 12) or 12
        execute = kwargs.pop('execute', True)
        uids = kwargs.pop('uids', None)
        context = self.context
        getAdapter = context.getAdapter
        if uids is None:
            gml_kwargs = kwargs.pop('getmenulevel_kwargs',
                {'portal_types': 'Folder',
                 'filter': False,
                 'plain': True,
                 'exclude_uids': kwargs.pop('exclude_uids', None),
                })
            children = getAdapter('getmenulevel')(**gml_kwargs)
            uids = [child.UID
                    for child in children
                    ]
        if kwargs:
            logger.warning('gLSes: ungenutzte Argumente (%(kwargs)s)', locals())

        asu = AS_SYSTEM_USER
        asu_msg = 'Key %%(key)r ignored (%%(asu)r, default: %(AS_SYSTEM_USER)r' % globals()
        portal = getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            pc = portal.getAdapter('pc')()

            def make_uid2brain(pc, strict=True):
                func = pc._catalog
                def u2b(uid):
                    liz = func(UID=uid)
                    if not liz or (strict and liz[1:]):
                        raise ValueError('uid %(uid)r ist nicht eindeutig'
                                         ' oder fehlt! (%(liz)s)' % locals())
                    return func(UID=uid)[0]
                return u2b
            uid2brain = make_uid2brain(pc)

            settings = portal.getBrowser('settings')
            data = settings.get('localsearch', {})
            unique_uids = set()
            for uid in uids:
                if uid in unique_uids:
                    continue
                unique_uids.add(uid)
                brain = uid2brain(uid)
                o = brain and brain.getObject() or None
                dic = {'brain': brain,
                       'uid': uid,
                       'object': o,
                       'config_url': None,
                       'subpage_id': None,
                       'title': None,
                       }
                if o is not None:
                    oid = o.getId()
                    dic.update({
                       'config_url': '%(oid)s/configure_localsearch'
                                     % locals(),
                       'subpage_id': oid,
                       'title': o.title_or_id(),
                       })

                if uid in data:
                    # type(...) --> <type 'instance'>, und ohne pop-Methode!
                    query = dict(data[uid])
                    # auch wenn noch nicht benutzt:
                    # jedenfalls aus den Anfragedaten entfernen!
                    key = 'as_system_user'
                    if key in query:  # "if" derzeit wg. Warnung; muß ggf. entfernt werden!
                        dic[key] = asu = query.pop(key, AS_SYSTEM_USER)
                        logger.warning(asu_msg, locals())
                    override = query.pop('override_excludeFromSearch', False)
                    if not override:
                        query['getExcludeFromSearch'] = False
                    override = query.pop('override_excludeFromNav', False)
                    if not override:
                        query['getExcludeFromNav'] = False
                    override = query.pop('override_workflow', False)
                    key = 'review_state'
                    if override:
                        if key in query:
                            del query[key]
                    elif key not in query:
                        query['review_state'] = ['inherit',
                                                 'published',
                                                 'visible',
                                                 'restricted',
                                                 ]

                    qkwargs = dict(query)
                    # root wird gleich wieder entfernt:
                    qkwargs['root'] = o.getPath()
                    self._resolve_path_args(query, **qkwargs)

                    dic.update({'query': query,
                                })
                    if queries_nonthumbnail_types_only(query):
                        dic['with_thumbnails'] = False
                    if execute:
                        # pp(query=query, maxcount=maxcount)
                        dic['brains'] = pc(**query)[:maxcount]
                        if not dic['brains']:
                            logger.warning('Nichts gefunden! query=\n%s', pformat(query))
                    else:
                        logger.warning('uid=%(uid)r, execute=%(execute)r', locals())
                res['children'].append(dic)

        finally:
            sm.setOld()

        res.update({'maxcount': maxcount,
                    'execute': execute,
                    'uids': uids,
                    })
        return res

    def getReviewStates(self, **kwargs):
        """
        Generiere die Arbeitsablauf-Statuus

        (eine dict-Liste mit den Schlüsseln 'id' und 'title';
        nach @@reviewstates.getFCKList, ../reviewstates/browser.py)
        """
        return self._dictifyReviewStates(['published',
                                          'inherit',
                                          'visible',
                                          'restricted',
                                          'accepted',
                                          'submitted',
                                          'private',
                                          ], **kwargs)

    def _dictifyReviewStates(self, keys, **kwargs):
        label_key = kwargs.pop('label_key', 'title')
        context = self.context
        getAdapter = context.getAdapter
        pw = getAdapter('pw')()
        _ = getAdapter('translate')
        states_dict = pw['dayta_workflow'].states
        for review_state in keys:
            label = _(states_dict[review_state].title)
            if label != review_state:  # immer, nehme ich an!
                label = '%(label)s (%(review_state)s)' % locals()
            yield {'id': review_state,
                   label_key: label,
                   }

    @log_or_trace(**lot_kwargs)
    # @log_or_trace(**updated(lot_kwargs, trace=1))
    def getActionURL(self, **kwargs):
        """
        Gib die URL zurück, die für das action-Attribut des <form>-Elements
        verwendet werden soll.
        """
        if 'layout' in kwargs:
            layout = kwargs.pop('layout')
        else:
            if 'context' in kwargs:
                context = kwargs.pop('context')
            else:
                context = self.context
            layout = context.getLayout()
        if 'folder_url' in kwargs:
            folder_url = kwargs.pop('folder_url')
        else:
            if 'context' in kwargs:
                context = kwargs.pop('context')
            else:
                context = self.context
            folder_url = context.getAdapter('parentfolder')().absolute_url()
        suffix = layout_to_action_suffix[layout]
        if suffix is None:
            return folder_url
        return '/'.join((folder_url, suffix))

    def refreshBrain(self):
        """
        Aktualisiere das Katalogobjekt des Kontexts
        """
        self.authRefreshBrains()
        context = self.context
        # request = context.REQUEST
        # form = request.form
        reindex = make_reindexer(logger=logger,
                                 context=context,
                                 update_metadata=True)
        ok = self._refreshBrain(reindex=reindex,
                                verbose=True)
        return back_to_referer(context)

    def _refreshBrain(self, reindex, **kwargs):
        """
        Arbeitspferd für --> refreshBrain
        """
        context = self.context
        brain = context.getHereAsBrain()
        verbose = kwargs.pop('verbose', False)
        if verbose:
            message = context.getAdapter('message')
        if brain is None:
            uid = context.UID()
            if uid is None:
                raise ValueError('Context %(context)r lacks a UID!' % locals())
            catalog = context.getAdapter('pc')
            total = catalog.catalogObject(context, uid)
            logger.info('%(context)r (%(uid)r) added to catalog, %(total)r indexes',
                        locals())
            if verbose:
                message('Object added to portal catalog.')
            return True
        if reindex(brain):
            if verbose:
                message('Catalog entry was refreshed.')
            return True
        else:
            logger.error('Reindexing for %(context)r failed!', locals())
            if verbose:
                message('Error refreshing the catalog entry!',
                        'error')
            return False


RE_TITLEANDYEAR = compile_re('^(?P<title>.*)'
                             ' *\('
                             '(?P<year>[0-9]{2,4})' # 2 oder 4 Ziffern
                             '\) *$'                # schl. Klammer, opt. Leerzeichen
                             )
def custom_rowdict1(brain, verbose=False):
    """
    Gib ein dict zurück, das aus dem übergebenen Brain die speziell benötigten Informationen extrahiert
    """
    dic = {'brain': brain}
    try:
        more = {'getURL': brain.getURL}
        dic.update(more)
        title = brain.pretty_title_or_id()
        more = {'pretty_title_or_id': title}
        dic.update(more)
        mo = RE_TITLEANDYEAR.match(title)
        if mo:
            dic.update(mo.groupdict())
        else:
            dic.update({'title': title,
                        'year': None,
                        })
        more = {'Description': brain.Description}
        dic.update(more)
        o = brain.getObject()
        i = o.getImage()
        more = {'image_path': i and i.getPath() or None}
        dic.update(more)
    except AttributeError as e:
        print asciibox(e.__class__.__name__, str(e))
        pp(dic=dic)
    except Exception as e:
        print asciibox(e.__class__.__name__, str(e))
        pp(dic=dic)
    finally:
        return dic


def custom_rowdict0(brain, verbose=False):
    """
    Wie custom_rowdict1, aber ohne Extraktion des Jahres aus dem Titel;
    der Wert für 'year' ist immer None.
    """
    dic = {'brain': brain}
    try:
        more = {'getURL': brain.getURL}
        dic.update(more)
        title = brain.pretty_title_or_id()
        more = {'pretty_title_or_id': title}
        dic.update(more)
        dic.update({'title': title,
                    'year': None,
                    })
        more = {'Description': brain.Description}
        dic.update(more)
        o = brain.getObject()
        i = o.getImage()
        more = {'image_path': i and i.getPath() or None}
        dic.update(more)
    except AttributeError as e:
        print asciibox(e.__class__.__name__, str(e))
        pp(dic=dic)
    except Exception as e:
        print asciibox(e.__class__.__name__, str(e))
        pp(dic=dic)
    finally:
        return dic
