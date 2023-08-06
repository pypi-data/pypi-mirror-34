# -*- coding: UTF-8 -*- äöü
from dayta.browser.public import BrowserView, implements, Interface
from plone.memoize import ram
from time import time

from .utils import brain_dict, flattened

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport(defaultFromDevMode=0)
# from Products.unitracc.tools.debug import print_call_and_result, trace_this
from visaplan.tools.debug import log_or_trace
# from pprint import pprint

lot_kwargs = {'debug_level': debug_active,
              'logger': logger,
              }


class ITree(Interface):

    def getRelObject(self):
        """ """

    def getRelBrain(self):
        """ """

    def getNextBrain(self):
        """ """

    def getPreviousBrain(self):
        """ """

    def getLastAsBrain(self, brain):
        """ """

    def getNavigationWithoutBrains(self, brain=None):
        """"""

    def getFlatNavigationWithoutBrains(self, brain=None):
        """"""

    def getNavigationWithBrains(self, brain=None):
        """"""

    def getFlatNavigationWithBrains(self, brain=None):
        """ """

    def getRelUid(self):
        """ """


def cache_key(method, self, brain=None, excludeFromNav=True,
              assertGivenBrain=True):

    context = self.context
    getAdapter = context.getAdapter
    langCode = getAdapter('langcode')()
    portalUrl = getAdapter('portal')().absolute_url()
    if not brain:
        brain = context.getHereAsBrain()

    return (portalUrl,
            brain.UID,
            self.pc.getCounter(),
            langCode,
            excludeFromNav,
            assertGivenBrain)


class Browser(BrowserView):

    implements(ITree)

    content_types = ['Document', 'UnitraccAnimation']
    folder_types = ['Folder']

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.pc = context.getAdapter('pc')()
        self.query = {}
        self.query['portal_type'] = self.folder_types + self.content_types
        self.query['sort_on'] = 'getObjPositionInParent'
        self.query['Language'] = 'all'

    def getTreeTypes(self):
        """ """
        return self.content_types + self.folder_types

    @log_or_trace(**lot_kwargs)
    def getLevel(self, current, excludeFromNav=True):
        """
        Gib die unmittelbaren Kindelemente des übergebenen Brains zurück
        """
        query = dict(self.query)

        query['path'] = {'query': current.getPath(),
                         'depth': 1}
        if excludeFromNav:
            query['getExcludeFromNav'] = False

        return self.pc(query)

    @log_or_trace(**lot_kwargs)
    @ram.cache(cache_key)
    def getCachedLevel(self, current, excludeFromNav=True):
        """
        Wie getLevel, aber anstelle der Brains wird eine Liste von
        dict.s zurückgegeben, und das Ergebnis wird gepuffert.
        """
        return [{'getURL': brain.getURL(),
                 'Title': brain.Title,
                 'UID': brain.UID,
                 'portal_type': brain.portal_type,
                 }
                for brain in self.getLevel(current, excludeFromNav)
                ]

        # Alten Code erstmal erhalten: 
        query = dict(self.query)

        query['path'] = {'query': current.getPath(),
                         'depth': 1}
        if excludeFromNav:
            query['getExcludeFromNav'] = False

        return [{'getURL': brain.getURL(),
                 'Title': brain.Title,
                 'UID': brain.UID,
                 'portal_type': brain.portal_type,
                 }
                 for brain in self.pc(query)]

    def recurse(self, current, results, level=1, currentAsBrain=True, excludeFromNav=True):
        """
        Erstelle eine Liste (Argument 'results'), die den Objektbaum abbildet,
        der im Objekt 'current' wurzelt.

        current - das Wurzelobjekt
        results - die zu füllende Liste
        level - zum Füllen der Rekursionslevel-Information
        currentAsBrain - wenn False, wird stattdessen die UID zurückgegeben
        excludeFromNav - wenn True, werden nur Elemente zurückgegeben, für die
                         getExcludeFromNav False ist (Auswertung durch getLevel)
        """
        brains = self.getLevel(current, excludeFromNav)
        current_uid = current.UID
        for brain in brains:
            dict_ = brain_dict(brain, current_uid, level, currentAsBrain)
            results.append(dict_)
            if brain.portal_type == 'Folder':
                self.recurse(brain, dict_['childs'],
                             level + 1,
                             currentAsBrain,
                             excludeFromNav=excludeFromNav)

        return results

    # @print_call_and_result
    # @trace_this
    @log_or_trace(**lot_kwargs)
    def getNextBrain(self, current=None, excludeFromNav=False):
        """ """
        context = self.context
        getbrain = context.getAdapter('getbrain')

        if not current:
            current = self.getRelBrain()
        if not current:
            return None

        list_ = self.getFlatNavigationWithoutBrains(context.getHereAsBrain(), excludeFromNav)

        current_uid = current.UID
        counter = 0
        for dict_ in list_:
            if 0:\
            pprint({'Index:': counter,
                    'Dict.:': dict_,
                    'UID': current_uid,
                    })
            if dict_['current'] == current_uid:
                if dict_['current'] != list_[-1]['current']:
                    dict_ = dict(list_[counter + 1])
                    dict_['current'] = getbrain(dict_['current'])
                    return dict_
                else:
                    return
            counter += 1

    # @print_call_and_result
    @log_or_trace(**lot_kwargs)
    def getPreviousBrain(self, current=None, excludeFromNav=False):
        """ """
        context = self.context
        getbrain = context.getAdapter('getbrain')
        if not current:
            current = self.getRelBrain()
        if not current:
            return None

        list_ = self.getFlatNavigationWithoutBrains(context.getHereAsBrain(), excludeFromNav)

        current_uid = current.UID
        counter = 0
        for dict_ in list_:
            if dict_['current'] == current_uid:
                if dict_['current'] != list_[0]['current']:
                    dict_ = dict(list_[counter - 1])
                    dict_['current'] = getbrain(dict_['current'])
                    return dict_
                else:
                    return
            counter += 1

    def getRelBrain(self):
        """ """
        uid = self.getRelUid()
        DEBUG('%r.getRelBrain(): uid=%r', self, uid)
        if uid:
            getbrain = self.context.getAdapter('getbrain')
            return getbrain(uid)

    def getRelObject(self):
        """ """
        brain = self.getRelBrain()
        if brain:
            return brain.getObject()

    @log_or_trace(**lot_kwargs)
    def getRelUid(self):
        """
        Gib die per Request-Variable angegebene UID zurück (ab Offset 4, wg.
        des Präfixes 'uid-') bzw. als Fallback die UID des Kontexts
        """
        context = self.context
        form = context.REQUEST.form
        if form.has_key('uid'):
            uid = form['uid']
            DEBUG('%r.getRelUid(): uid=%r (form), %r', self, uid, uid[4:])
            if uid and uid.startswith('uid-'):
                return uid[4:]
            return uid
        return context.UID()

    @ram.cache(cache_key)
    def getNavigationWithoutBrains(self, brain=None, excludeFromNav=True):
        """brain=root element"""
        if not brain:
            brain = self.context.getHereAsBrain()
        if not brain:
            return []
        return self.recurse(brain, [], currentAsBrain=False, excludeFromNav=excludeFromNav)

    @ram.cache(cache_key)
    def getFlatNavigationWithoutBrains(self, brain=None,
                                       excludeFromNav=True,
                                       assertGivenBrain=True):
        """brain=root element"""
        if not brain:
            brain = self.context.getHereAsBrain()
        if not brain:
            return []

        if debug_active and 0:\
        print(['getFlatNavigationWithoutBrains(%r):' % brain,
               brain,
               {'uid:': brain.UID,
                },
               ])
        tree = self.getNavigationWithoutBrains(brain, excludeFromNav)
        list_ = []
        self.flat(list_, tree)

        current_uid = brain.UID
        insert_current = (assertGivenBrain and
                          current_uid not in [dic['current']
                                              for dic in list_]
                          )
        if insert_current:
            list_.insert(0, brain_dict(brain, None, 1, currentAsBrain=False))
        delete_first = False
        if list_:
            first = list_[0]
            delete_first = (first['portal_type'] == 'Folder'
                            and first['uid_parent'] is None
                            )
        if delete_first:
            DEBUG('getFlatNavigationWithoutBrains'
                  '(%(current_uid)r):'
                  'loesche %(first)s',
                  locals())
            if first['current'] == current_uid:
                DEBUG('*** Loesche "aktuelles" Objekt,'
                      ' uid=%(current_uid)s'
                      ' (assertGivenBrain=%(assertGivenBrain)s)!',
                      locals())
            del list_[0]
        # Nummern injizieren:
        number = 1
        for dic in list_:
            dic['number'] = number
            number += 1
        return list_

    @ram.cache(cache_key)
    def getFlatNavigationNumbersMap(self, brain=None,
                                    excludeFromNav=True,
                                    assertGivenBrain=True):
        """
        Gib ein Tupel zweier Strukturen zurück:

        - uid2number: ein dict, das einer UID die 1-basierte Nummer
                      in der Sequenz zuordnet;
        - uid_sequence: ein Tupel der UIDs; durch ein vorn eingefügtes
                        None ebenfalls 1-basiert
        """
        dicts = self.getFlatNavigationWithoutBrains(brain,
                                    excludeFromNav=True,
                                    assertGivenBrain=True)
        uid2number = {}
        # Dieser Wert wird verwendet (@@presentation.goto)! 
        uid_sequence = [None]
        number = 1
        for dic in dicts:
            uid = dic['current']
            uid_sequence.append(uid)
            uid2number[uid] = number
            number += 1
        return uid2number, tuple(uid_sequence)

    # @print_call_and_result
    def getNavigationWithBrains(self, brain=None, excludeFromNav=True):
        """brain=root element"""
        if not brain:
            brain = self.context.getHereAsBrain()
        if not brain:
            return []
        return self._getNavigationWithBrains(brain,
                            excludeFromNav=excludeFromNav)

    def _getNavigationWithBrains(self, brain, excludeFromNav=True):
        return self.recurse(brain, [], currentAsBrain=True,
                            excludeFromNav=excludeFromNav)

    def getFlatNavigationWithBrains(self, brain=None):
        """brain=root element"""
        if not brain:
            brain = self.context.getHereAsBrain()
        if not brain:
            return []

        ## für die Vortragsnavigation werden die "childs" leider noch verwendet
        ## (die von "flattened" konsequenterweise entfernt werden):
        # return list(flattened(self._getNavigationWithBrains(brain)[0], 'childs'))

        tree = self._getNavigationWithBrains(brain)
        list_ = []
        self.flat(list_, tree)

        return list_

    def flat(self, list_, childs):
        """
        list_ - eine (leere) Liste zur Aufnahme der Elemente
        childs - eine Liste von Wurzelelementen (dict.s),
                 typischerweise mit der Länge 1

        Hänge die enthaltenen dict.s an die übergebene Liste an.

        ACHTUNG - die "childs"-Schlüssel (mit den Verweisen auf die
        Kindelemente) bleiben dabei erhalten! Die Liste ist also nicht
        wirklich flach, und es gibt keine Sicherheit, daß Elemente nicht
        doppelt verwendet würden!
        """
        for dict_ in childs:
            list_.append(dict_)
            if dict_['childs']:
                self.flat(list_, dict_['childs'])

    def getFirstAsBrain(self, brain):
        """ """
        context = self.context
        getbrain = context.getAdapter('getbrain')
        list_ = self.getFlatNavigationWithoutBrains(brain, False)
        if list_:
            dict_ = dict(list_[0])
            return getbrain(dict_['current'])

    def getLastAsBrain(self, brain):
        """ """
        context = self.context
        getbrain = context.getAdapter('getbrain')
        list_ = self.getFlatNavigationWithoutBrains(brain, False)
        if list_:
            dict_ = dict(list_[-1])
            return getbrain(dict_['current'])
