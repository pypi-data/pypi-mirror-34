# -*- coding: utf-8 -*- äöü
# Plone-Module:
from AccessControl import Unauthorized

# Dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Unitracc:
from ...permissions import (ManageGroups,
        ManageUsers, ManageCourses,
        View_Development_Information,
        )

# Unitracc-Tools:
from visaplan.tools.profile import StopWatch
from ...tools.misc import getOption
from ...tools.context import make_permissionChecker

# Dieser Browser:
from .utils import jsonify

# Logging und Debugging:
from visaplan.plone.tools.log import getLogSupport
LOGGER, debug_active, DEBUG = getLogSupport(defaultFromDevMode=False)
sw_kwargs = {'enable': bool(debug_active),
             'logger': LOGGER,
             }


class IManagementBrowser(Interface):

    def getStructureElementFolders(self):
        """ """

    def getSubmittedContent(self):
        """
        Gib alle Objekte im Bearbeitungsstatus "eingereicht" zurück
        """

    def getAcceptedContent(self):
        """
        Gib alle Objekte im Bearbeitungsstatus "akzeptiert" zurück
        """

    def getManagedContent(self):
        """
        Gib die Objekte der Bearbeitungsliste zurück;
        entnimm den Bearbeitungsstatus den Formulardaten
        """

    def getManagedContent_ajax(self):
        """
        Gib die Objekte der Bearbeitungsliste im JSON-Format zurück
        """

    def canAccessSiteManagement(self):
        """
        Zugriff auf die Unitracc-Verwaltungsseiten (wenn auch nicht
        notwendigerweise alle) erlaubt?
        """

    def canAccessStage(self):
        """
        Zugriff auf die Buehne erlaubt?
        """

    def get_management_actions(self):
        """ """

    def isDeveloper(self):
        """
        Darf der angemeldete Benutzer Entwicklerinformationen sehen?

        Es wird eine Berechtigung geprüft, keine Rolle; der Name wurde im Sinne
        der Handlichkeit gewählt.
        """


class Browser(BrowserView):

    implements(IManagementBrowser)

    def getStructureElementFolders(self):
        """ """
        context = self.context
        storagefolder = context.getBrowser('storagefolder')

        list_ = []

        for aname in (
            'getVirtualConstructionFolder',
            'getTechnicalInformationFolder',
            'getInstructionsFolder',
            'getDocumentationFolder',
            'getPaperFolder',
            'getPresentationFolder',
            ):
            a = getattr(storagefolder, aname)
            try:
                list_.append(a())
            except Exception as e:
                LOGGER.exception(e)

        return list_

    def getSubmittedContent(self):
        """
        Gib alle Objekte im Bearbeitungsstatus "eingereicht" zurück
        """
        return self._getManagedContent('submitted')

    def _getManagedContent(self, review_state):
        # Ergebnis der Messung:
        # - die Suche geht sehr schnell;
        # - was lang dauert, ist also die Ausgabe von über 1600 Listeneinträgen
        with StopWatch('_getManagedContent(%r)',
                       mapping=review_state,
                       **sw_kwargs) as stopwatch:
            context = self.context
            getAdapter = context.getAdapter

            getAdapter('authorized')('unitracc: Manage submitted and accepted content')

            query = {}
            query['Language'] = 'all'

            if review_state:
                query['review_state'] = review_state
            query['sort_on'] = 'modified'
            query['sort_order'] = 'descending'
            query['NO_SUBPORTAL'] = 1

            stopwatch.lap('query = %s' % (query,))
            pc = getAdapter('pc')()
            return pc(**query)

    def getAcceptedContent(self):
        """
        Gib alle Objekte im Bearbeitungsstatus "akzeptiert" zurück
        """
        return self._getManagedContent('accepted')

    def getManagedContent(self):
        """
        Gib die Objekte der Bearbeitungsliste zurück;
        entnimm den Bearbeitungsstatus den Formulardaten
        """
        context = self.context
        form = context.REQUEST.form
        review_state = getOption(form, 'review_state')
        return self._getManagedContent(review_state)

    def getManagedContent_ajax(self):
        """
        Gib die Objekte der Bearbeitungsliste im JSON-Format zurück
        """
        return jsonify(context, self.getManagedContent())

    def _getManagedContent_json(self, review_state, varname=None):
        """
        Gib die Objekte der Bearbeitungsliste im JSON-Format zurück
        """
        return jsonify(self.context, self._getManagedContent(review_state), varname)

    def canAccessSiteManagement(self, raiseUnauthorized=False):
        """
        Checks if current user can access site administration.
        @param raiseUnauthorized Raises Unauthorized if parameter value is True user can not access site management
        """
        checkperm = make_permissionChecker(self.context, verbose=debug_active)
        canAccess = (checkperm('Manage portal') or
                     checkperm(ManageUsers) or
                     checkperm(ManageGroups) or
                     checkperm(ManageCourses) or
                     checkperm('unitracc: Manage Keywords') or
                     checkperm('unitracc: Manage submitted and accepted content') or
                     checkperm('unitracc: Add structure types') or
                     checkperm('unitracc: Copy structure types') or
                     checkperm('unitracc: Delete structure types') or
                     checkperm('unitracc: Publish structure types') or
                     checkperm('unitracc: Manage Orders') or
                     checkperm('unitracc: Manage Export Profiles') or
                     checkperm('unitracc: Manage TANs'))

        if not canAccess and raiseUnauthorized:
            raise Unauthorized

        return canAccess

    def canAccessStage(self, raiseUnauthorized=False):
        """
        Zugriff auf die Buehne erlaubt?
        @param raiseUnauthorized Wenn True, wird ggf. eine
                                 Unauthorized-Exception geworfen
        """
        checkperm = make_permissionChecker(self.context, verbose=debug_active)
        if (checkperm('stage: Manage stage') or
            checkperm('unitracc: Manage Ads')):
            return True
        elif raiseUnauthorized:
            raise Unauthorized
        else:
            return False

    def _zopesrv_url(self):
        """
        Gib die mitmaßliche URL des Zope-Servers zurück;
        die Kombination 'http://%(SERVER_NAME)s:%(SERVER_PORT)s/'
        hat sich (aufgrund suboptimaler DNS-Konfiguration?)
        als unzuverlässig erwiesen
        """
        context = self.context
        request = context.REQUEST
        get = request.get
        port = get('SERVER_PORT')
        name = get('SERVER_NAME')
        if name in ('local',  # z. B. visaplan-Netz
                    'test',   # Test-Instanzen
                    ):
            xhost = get('HTTP_X_FORWARDED_HOST')
            if xhost:
                hostl = xhost.split('.', 1)
                if hostl[1:]:
                    host = hostl[1]
                    return 'http://%(host)s:%(port)s' % locals()
        # Zope selbst verwendet stets http, nicht https: 
        return 'http://%(name)s:%(port)s' % locals()

    def get_management_actions(self):

        context = self.context

        context.getBrowser('tpcheck').auth_manage_portal()

        pa = context.getAdapter('pa')()

        navigation = context.getBrowser('navigation')

        list_ = []

        for id in pa.objectIds():
            if id.startswith('management_'):
                list_.extend(navigation.get_actions([id]))
        return list_

    def isDeveloper(self):
        """
        Darf der angemeldete Benutzer Entwicklerinformationen sehen?

        Es wird eine Berechtigung geprüft, keine Rolle; der Name wurde im Sinne
        der Handlichkeit gewählt.
        """
        checkperm = make_permissionChecker(self.context, verbose=debug_active)
        return checkperm(View_Development_Information)


# vim: ts=8 sts=4 sw=4 si et tw=79
