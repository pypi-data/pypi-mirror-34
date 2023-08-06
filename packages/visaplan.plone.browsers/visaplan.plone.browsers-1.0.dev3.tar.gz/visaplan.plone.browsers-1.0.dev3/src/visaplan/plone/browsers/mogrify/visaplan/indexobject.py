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
from visaplan.tools.lands0 import makeListOfStrings
from visaplan.tools.minifuncs import makeBool

# Dieser Browser:
from ._base import BaseSection

# Logging:
import logging


logger = logging.getLogger('visaplan.transmogrifier.indexobject')


class IndexObject(BaseSection):
    """
    Objekte dem Katalog hinzufügen
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
        if trace1st:
            from pdb import set_trace
        prefix = self.context.getPhysicalPath()
        idxs = ('Creator',
                'Date',
                'Description',
                'Language',
                'SearchableText',
                'Subject',
                'Title',
                'Type',
                'UID',
                'allowedRolesAndUsers',
                'cmf_uid',
                'commentators',
                'created',
                'effective',
                'effectiveRange',
                'end',
                'expires',
                'getCode',
                'getCodeIndex',
                'getCustomSearch',
                'getEffectiveIndex',
                'getExcludeFromNav',
                'getExcludeFromSearch',
                'getId',
                'getObjPositionInParent',
                'getRawRelatedItems',
                'getTitleIndex',
                'getUsedLanguages',
                'get_sub_portal',
                'id',
                'in_reply_to',
                'is_default_page',
                'is_folderish',
                'meta_type',
                'modified',
                'object_provides',
                'path',
                'portal_type',
                'review_state',
                'sortable_title',
                'start',
                'total_comments',
                ) and self.indexes
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
                logger.info("Index object %s (%s)", path, self.counter)

            try:
                if trace1st:
                    print self.name +': Erste Katalogisierung!'
                    trace1st = False
                    set_trace()
                catalog.catalog_object(ob, idxs=idxs)
                count('indexed')
            except CatalogError as e:
                if firsterror:
                    logger.error('error adding %(path)s to catalog', locals())
                    logger.exception(e)
                    firsterror = False
                    if self.trace1st:
                        set_trace()
                count('errors')

            yield item
