# -*- coding: utf-8 # äöü
from dayta.browser.public import BrowserView, implements, Interface
import transaction

# Andere Browser
from ..unitraccfeature.utils import (MEDIATHEK_UID, ARTICLESFOLDER_UID,
        EVENTSFOLDER_UID, COURSESFOLDER_UID,
        )

# Dieser Browser
from .data import MEDIATHEK_TYPES, DESTINATION_MAP
from .utils import get_code

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)

# -------------------------------------------- [ Daten ... [
NO_TRANSACTION, USE_TRANSACTION, OWN_TRANSACTION = tuple(range(3))
# -------------------------------------------- ] ... Daten ]


# Akademie Kanalbau (GKZ): c5c80b6365a64a268f2f55cb39c39aa8
class IMediathek(Interface):

    def move(self, object_):
        """
        Verschiebe das übergebene Objekt; *alte Version!*

        Wenn der Aufrufkontext eine Transaktion erzeugt, kann diese Version
        Probleme verursachen.  Es ist daher zu empfehlen, auf die neuere Methode
        _move umzustellen (die allerdings eine abweichende Aufrufsignatur hat)!
        """

    def _move(self, **kwargs):
        """
        Verschiebe das übergebene Objekt; alle Argumente sind benannt anzugeben
        """

    def getStructureFolder(self):
        """ """

    def getDestinationMap(self):
        """
        Gib eine Liste der verwendeten Verschiebungsziele aus
        """


class Browser(BrowserView):

    implements(IMediathek)

    def getMediathekPath(self):
        """
        get Mediathek Path
        """
        context = self.context
        getbrain = context.getAdapter('getbrain')
        return getbrain(MEDIATHEK_UID).getPath()

    def getStructureFolder(self):
        """
        Der Ordner "structure" in der Mediathek
        """

        if MEDIATHEK_UID is None:
            logger.warning('Keine Mediathek konfiguriert!')
            return

        context = self.context
        rc = context.getAdapter('rc')()
        media = rc.lookupObject(MEDIATHEK_UID)
        if media is None:
            logger.error('Mediathek (unter UID %r) nicht gefunden!',
                         MEDIATHEK_UID)
            return

        return media.restrictedTraverse('structure', None)

    def _get_destination(self, o, rc=None, **kwargs):
        """
        Objekt <o> verschieben; ein evtl. fehlender Unterordner in der
        Mediathek wird ggf. erstellt
        """
        logger.info('_get_destination(%(o)r) ...', locals())
        ok = False
        destination = None
        try:
            ptype = o.portal_type
            destination_uid = DESTINATION_MAP[ptype]
        except AttributeError as e:
            logger.exception(e)
        except KeyError as e:
            if ptype not in MEDIATHEK_TYPES:
                logger.info('kein Ziel fuer Typ %(ptype)r', locals())
                ok = True
                return

            values = [chunk.lower()
                      for chunk in get_code(o)
                      ]
            folder = self.getStructureFolder()
            if folder is None:
                return

            use_transaction = kwargs.get('use_transaction',
                                         USE_TRANSACTION)
            for item in values:
                if folder.restrictedTraverse(item.lower(), None):
                    folder = folder.restrictedTraverse(item.lower())
                else:
                    createobject = folder.getAdapter('createobject')
                    newFolder = createobject('Folder', item)
                    newFolder.processForm()
                    folder = newFolder
                    if use_transaction:
                        transaction.savepoint()
            destination = folder
            return destination

        else:
            if destination_uid is None:
                logger.info('kein Ziel fuer Typ %(ptype)r', locals())
                return
            if rc is None:
                rc = self.context.getAdapter('rc')()
            destination = rc.lookupObject(destination_uid)
            if destination is None:
                logger.error('Ziel %(destination_uid)r fuer Typ %(ptype)r'
                             ' nicht gefunden!',
                             locals())
                return None  # pep 20.2
            return destination
        finally:
            logger.info('... fertig')

    def _move(self, **kwargs):
        """
        Verschiebe das übergebene Objekt; alle Argumente sind benannt anzugeben:

        o -- das zu verschiebende Objekt
        uid -- die UID des zu verschiebenden Objekts

        use_transaction -- soll eine Transaktion verwendet werden?
                           Werte:
                           NO_TRANSACTION
                           USE_TRANSACTION (Vorgabe)
                           OWN_TRANSACTION
        force -- Wahrheitswert: soll auch aus anderen Verzeichnissen als /temp verschoben werden?
        unlock -- Wahrheitswert (entsperren?) -- Vorgabe: True
        rc -- der resource_catalog, ggf. ermittelt mit context.getAdapter('rc')()
        """
        logger.info('_move(%(kwargs)s) ...', locals())
        uid = kwargs.get('uid', None)
        o = kwargs.get('o', None)
        check_conflict = False
        if uid is None:
            if o is None:
                raise TypeError('Either <uid> or <o> is needed!')
            uid = o.UID()
        elif o is not None:
            logger.warn('_move: both uid (%(uid)r) and o(bject) (%(o)r) given', locals())
            check_conflict = True
        o.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)

        rc = kwargs.get('rc', None)
        if rc is None:
            getAdapter = kwargs.get('getAdapter', None)
            if getAdapter is None:
                context = kwargs.get('context', None)
                if context is None:
                    context = self.context
                getAdapter = context.getAdapter
            rc = getAdapter('rc')()

        if o is None:
            o = rc.lookupObject(uid)
            if o is None:
                logger.error('No object found with UID %(uid)r!', locals())
                return False
        elif check_conflict:
            uid2 = o.UID()
            if uid2 != uid:
                logger.error('object %(o)r has an unexpected UID!'
                             '\nexpected: %(uid)r'
                             '\nfound:    %(uid2)r',
                             locals())
                return False

        parent = o.aq_parent
        if parent.getId() != 'temp':
            force = kwargs.get('force', False)
            if not force:
                # Strenggenommen verschiebt diese Methode aus jedem Ordner,
                # der 'temp' heißt ...
                logger.info('Verschiebe nur aus dem temp. Verzeichnis!')
                return

        use_transaction = kwargs.get('use_transaction', USE_TRANSACTION)
        if use_transaction >= OWN_TRANSACTION:
            transaction.begin()
        dest = self._get_destination(o, rc,
                                     use_transaction=use_transaction and USE_TRANSACTION)
        if dest is None:
            logger.warning('_move(%(o)r): no destination configured', locals())
            if use_transaction >= OWN_TRANSACTION:
                transaction.abort()
            return
        elif parent is dest:
            logger.info('Quelle %(parent)r und Ziel %(dest)r sind identisch!',
                        locals())
            if use_transaction >= OWN_TRANSACTION:
                transaction.abort()
            return

        logger.info('_move(%(o)r): dest=%(dest)r', locals())

        oid = o.getId()
        cp = parent.manage_cutObjects(ids=[oid])
        dest.manage_pasteObjects(cp)

        # verschobenes Objekt:
        moved_o = rc.lookupObject(uid)
        moved_o.reindexObject()

        if use_transaction >= OWN_TRANSACTION:
            transaction.commit()
        elif use_transaction:
            transaction.savepoint()
        return moved_o

    def move(self, object_, force=False):
        """
        Verschiebe das übergebene Objekt
        """
        logger.info('move(%(object_)r) ...', locals())
        object_.restrictedTraverse('@@plone_lock_operations').force_unlock(redirect=False)

        context = self.context
        uid = object_.UID()
        rc = context.getAdapter('rc')()
        transaction.begin()
        dest = self._get_destination(object_, rc)
        if dest is None:
            logger.warning('move(%(object_)r): no destination configured', locals())
            return

        logger.info('move(%(object_)r): dest=%(dest)r', locals())

        parent = object_.aq_parent
        if parent.getId() != 'temp' and not force:
            logger.info('Verschiebe nur aus dem temp. Verzeichnis!')
            return

        oid = object_.getId()
        cp = parent.manage_cutObjects(ids=[oid])
        dest.manage_pasteObjects(cp)

        # verschobenes Objekt:
        movedo = rc.lookupObject(uid)
        movedo.reindexObject()

        transaction.commit()

    def getDestinationMap(self):
        """
        Gib eine Liste der verwendeten Verschiebungsziele aus
        """
        known_types = set(MEDIATHEK_TYPES)
        known_keys = set(DESTINATION_MAP.keys())
        missing_keys = known_types.difference(known_keys)
        if missing_keys:
            logger.error('getDestinationMap: missing_keys = %s', sorted(missing_keys))
        not_listed = known_keys.difference(known_types)
        if not_listed:
            logger.error('getDestinationMap: not_listed = %s', sorted(not_listed))
        all_types = set(known_types)
        all_types.update(known_keys)
        for key in sorted(all_types):
            yield {'key': key,
                   'uid': DESTINATION_MAP.get(key),
                   }

