# -*- coding: utf-8 -*- äöü
# @@mogrify.visaplan.reindexobject: Katalogobjekte aktualisieren

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


logger = logging.getLogger('visaplan.transmogrifier.reindexobject')


class ReindexObject(BaseSection):
    """
    Zugeordnete Katalogobjekte aktualisieren
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        # aus plone.app.transmogrifier.reindexobject:
        self.portal_catalog = transmogrifier.context.portal_catalog
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')
        self.counter = 0
        self.indexes = getOption(options, 'indexes',
                                 factory=makeListOfStrings)
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):

        catalog = self.portal_catalog
        count = self.count
        firsterror = True
        # Debugging/Entwicklung: Logging jedes katalogisierten Objekts
        verbose = self.verbose
        # Debugging/Entwicklung: Einzelschrittausführung bei erstem Objekt
        trace1st = self.trace1st
        if trace1st or self.debug_ids:
            from pdb import set_trace
        prefix = self.context.getPhysicalPath()
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

            # Debugging/Entwicklung: Logging jedes katalogisierten Objekts
            if verbose:  # add a log to display reindexation progess
                self.counter += 1
                logger.info("Reindex object %s (%s)", path, self.counter)

            try:
                if trace1st:
                    print self.name +': Erste Katalogisierung!'
                    trace1st = False
                    set_trace()
                # update catalog
                if self.indexes:
                    self.portal_catalog.reindexObject(ob, idxs=self.indexes)
                else:
                    self.portal_catalog.reindexObject(ob)
                count('reindexed')
            except CatalogError as e:
                if firsterror:
                    logger.error('error adding %(path)s to catalog', locals())
                    logger.exception(e)
                    firsterror = False
                    if self.trace1st:
                        set_trace()
                count('errors')

            yield item
