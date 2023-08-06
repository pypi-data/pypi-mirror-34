# -*- coding: utf-8 -*- äöü
# @@mogrify.visaplan.indexobject: Objekte dem Katalog hinzufügen

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
from visaplan.tools.minifuncs import makeBool

# Dieser Browser:
from ._base import BaseSection

# Logging:
import logging


logger = logging.getLogger('visaplan.transmogrifier.injectuid')


class InjectUID(BaseSection):
    """
    UIDs der vorhandenen Objekte dem Item hinzufügen
    """

    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        # aus plone.app.transmogrifier.reindexobject:
        self.portal_catalog = transmogrifier.context.portal_catalog
        self.pathkey = defaultMatcher(options, 'path-key', name, 'path')
        # self.uidkey = defaultMatcher(options, 'uid-key', name, 'uid')
        self.counter = 0
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):

        count = self.count
        firsterror = True
        # Debugging/Entwicklung: Einzelschrittausführung bei erstem Objekt
        trace1st = self.trace1st
        if trace1st:
            from pdb import set_trace
        # Debugging/Entwicklung: Logging jedes katalogisierten Objekts
        verbose = self.verbose
        prefix = self.context.getPhysicalPath()
        for item in self.previous:
            pathkey = self.pathkey(*item.keys())[0]
            # uidkey = self.uidkey(*item.keys())[0]
            if not pathkey:  # not enough info
                yield item
                continue
            path = item[pathkey]

            ob = traverse(self.context, str(path).lstrip('/'), None)
            if ob is None:
                yield item
                continue  # object not found

            if not isinstance(ob, CatalogAware):
                yield item
                continue  # can't notify portal_catalog

            if verbose:  # add a log to display reindexation progess
                self.counter += 1
                logger.info("Index object %s (%s)", path, self.counter)

            try:
                if trace1st:
                    trace1st = False
                    print self.name + ': Erste Ermittlung einer UID (%(path)s)!' % locals()
                    set_trace()
                item['_uid'] = ob.UID
                count('changed')
            except CatalogError as e:
                if firsterror:
                    logger.error('error injecting UID for %(path)s', locals())
                    logger.exception(e)
                    firsterror = False
                    if self.trace1st:
                        set_trace()
                count('errors')

            yield item
