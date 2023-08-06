# -*- coding: utf-8 -*- äöü
# @@mogrify.visaplan.setsubportals: Subportal-Zuordnung korrigieren

# Plone/Zope:
from zope.interface import classProvides, implements
try:
    from Products.CMFCore.CMFCatalogAware import CatalogAware  # Plone 4
except ImportError:
    from Products.CMFCore.CMFCatalogAware import CMFCatalogAware as CatalogAware  # noqa
from Products.ZCatalog.Catalog import CatalogError

# Installierte Module:
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.utils import defaultMatcher, traverse

# Unitracc-Tools:
from ....tools.misc import getOption
from visaplan.tools.lands0 import makeListOfStrings
from visaplan.tools.minifuncs import makeBool

# Dieser Browser:
from ._base import BaseSection

# Logging:
import logging


logger = logging.getLogger('visaplan.transmogrifier.setsubportals')


class SetSubportals(BaseSection):
    """
    Subportal(e) setzen

    Setzt für die übergebenen Objekte den subPortals-Wert auf das aktuelle Subportal
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')
        self.counter = 0
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):

        count = self.count
        firsterror = True
        # Debugging/Entwicklung: Einzelschrittausführung bei erstem Objekt
        trace1st = self.trace1st
        # Debugging/Entwicklung: Logging jedes katalogisierten Objekts
        verbose = self.verbose
        if trace1st:
            from pdb import set_trace
        current_subportal = self.context.getBrowser('subportal').get_current_id()
        newval = [current_subportal]
        newval_set = set(newval)
        logger.info('[%s]: setting subPortals to %s', self.name, newval)
        for item in self.previous:
            pathkey = self.pathkey(*item.keys())[0]
            if not pathkey:  # not enough info
                count('skipped-nopath')
                yield item
                continue
            path = item[pathkey]

            ob = traverse(self.context, str(path).lstrip('/'), None)
            if ob is None:
                count('skipped-notfound')
                yield item
                continue  # object not found

            if not isinstance(ob, CatalogAware):
                count('skipped-invalid')
                yield item
                continue  # can't notify portal_catalog

            try:
                self.counter += 1

                ok = False
                try:
                    oldval_set = set(ob.subPortals)
                    if oldval_set == newval_set:
                        ok = True
                    else:
                        if trace1st:
                            trace1st = False
                            print self.name + ': Erste Subportal-Korrektur!'
                            set_trace()

                        key = 'changed'
                except AttributeError:
                    ok = False
                    key = 'set'
                if ok:
                    key = 'unchanged'
                    if verbose >= 2:
                        logger.info("Subportals of %s %s (%s)", path, key, self.counter)
                    count(key)
                    yield item
                    continue
                ob.subPortals = newval
                if verbose:
                    logger.info("Subportals of %s %s (%s)", path, key, self.counter)
                count(key)
            except CatalogError as e:
                if firsterror:
                    firsterror = False
                    logger.error('error adjusting subportal for %(path)s', locals())
                    logger.exception(e)
                    if self.trace1st:  # bei Fehler vormaliges trace1st ignorieren
                        set_trace()  # Subportal-Korrektur: Fehler untersuchen!
                count('errors')

            yield item
