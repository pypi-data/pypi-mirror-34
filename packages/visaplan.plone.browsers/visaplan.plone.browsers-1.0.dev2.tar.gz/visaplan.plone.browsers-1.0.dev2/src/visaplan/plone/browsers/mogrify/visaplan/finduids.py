# -*- coding: utf-8 -*- äöü

from zope.interface import classProvides, implements
from zope.annotation.interfaces import IAnnotations

from collective.transmogrifier.interfaces import ISection, ISectionBlueprint
from collective.transmogrifier.utils import Condition

from Products.CMFCore.utils import getToolByName

from visaplan.tools.lands0 import makeListOfStrings

# Dieser Browser:
from ._base import BaseSection
from ..utils import make_countdown_function

# Logging:
import logging
from pdb import set_trace


logger = logging.getLogger('visaplan.transmogrifier.finduids')

class FindUIDs(BaseSection):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self._store_initial_args(transmogrifier, name, options, previous)
        self.uidkey = options.get('uid-key', '_uid').strip()
        self.pathkey = options.get('path-key', '_path').strip()
        self.typekey = options.get('type-key', '_type').strip()
        self.uids = getOption(options, 'uids', factory=makeListOfStrings)
        # weitere Optionen aus BaseSection._set_debugging_options

    def __iter__(self):
        count = self.count
        firsterror = True
        # Debugging/Entwicklung: Einzelschrittausführung bei erstem Objekt 
        trace1st = self.trace1st
        uidkey = self.uidkey
        pathkey = self.pathkey
        typekey = self.typekey
        # Debugging/Entwicklung: Logging jedes katalogisierten Objekts
        verbose = self.verbose

        # vorerst fix: für nicht gefundene UIDs keine Items erzeugen 
        skip_notfound = True
        # vorerst fix: für abweichende Pfade zus. Items erzeugen
        skip_mismatch = False

        log_found = verbose >= 1
        log_notfound = verbose >= 2

        found_uids = set()
        for item in self.previous:
            count('got')
            uid = item.get(uidkey, None)
            if uid and item.get(pathkey, None):
                count('got-with-uids')
                found_uids.add(uid)
            elif uid:
                count('got-without-paths')
            else:
                count('got-without-uids')
            count('forwarded')
            yield item

        if not self.uids:
            logger.info('no UIDs specified')
            return

        rc = getToolByName(self.context, 'reference_catalog')
        lookup = rc.lookupObject

        urltool = getToolByName(self.context, 'portal_url')
        getpath = urltool.getRelativeContentURL

        spec_uids = set()
        for uid in self.uids:
            if uid in spec_uids:
                count('duplicate-uids')
                continue
            else:
                spec_uids.add(uid)
            if uid in found_uids:
                count('found-in-input')
                found_path = item.get(pathkey, None)
            else:
                found_path = None

            item = {uidkey: uid}
            obj = lookup(uid)
            if obj is None:
                count('not-found')
                if log_notfound:
                    logger.info('not found: %(uid)s', locals())
                if skip_notfound:
                    continue
            else:
                count('found')
                item.update({
                    pathkey: getpath(obj),
                    typekey: obj.getPortalTypeName(),
                    })
                rc_path = item[pathkey]
                if (found_path is not None
                    and found_path != item[pathkey]
                    ):
                    logger.warn('uid %(uid)s:'
                                '\ngot path  %(found_path)s,'
                                '\nrc yields %(rc_path)s',
                                locals())
                    if skip_mismatch:
                        count('skipped-path-mismatch')
                        continue
                    else:
                        count('found-path-mismatch')
                else:
                    count('found-ok')
                if log_found:
                    logger.info('uid %(uid)s --> %(rc_path)s', locals())
            count('created')
            yield item
