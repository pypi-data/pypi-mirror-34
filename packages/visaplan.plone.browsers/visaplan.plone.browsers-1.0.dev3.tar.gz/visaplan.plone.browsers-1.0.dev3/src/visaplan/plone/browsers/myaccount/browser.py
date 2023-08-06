# -*- encoding: utf-8 -*- äöü
# Plone/Zope/dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport('myaccount')


class IMyAccount(Interface):

    def set(self):
        """
        Speichere Änderungen des Profils
        """

    def get(self):
        """
        Gib ein Formular zur Änderung des Profils aus
        """

    def editProfile(self):
        """
        Alias für get
        """


class Browser(BrowserView):

    implements(IMyAccount)

    def set(self):
        """ """
        context = self.context
        getBrowser = context.getBrowser
        getBrowser('authorized').raiseAnon()
        author = getBrowser('author').get()
        member = getBrowser('member')
        userId = member.getId()
        fullname = member.getFullname()

        getAdapter = context.getAdapter
        message = getAdapter('message')
        request = context.REQUEST
        form = request.form

        if not getAdapter('checkperm')('Portlets: Manage portlets'):
            form['suppress_portlet_management'] = True

        portal = getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:

            errors = {}
            errors = author.validate(REQUEST=request, errors=errors, data=1, metadata=0)

            if errors:
                form['user_fullname'] = fullname  # Ansonsten wird oben in der top.pt "system" angezeigt
                form = context.restrictedTraverse('my_account_edit_form')(errors=errors, userId=userId)
                return form

            author.processForm()

        finally:
            sm.setOld()

        message('Changes saved.')

        form['user_fullname'] = fullname
        desktop_path = getBrowser('unitraccfeature').desktop_path()
        return request.RESPONSE.redirect(portal.absolute_url() + desktop_path + '/@@myaccount/editProfile')

    def editProfile(self):
        """
        Gib ein Formular zur Bearbeitung des Profils des angemeldeten Benutzers aus
        """
        context = self.context

        if debug_active:
            def f(A):
                a = A.lower()
                for test in ('browser', 'portal', 'context',
                             ):
                    if test in a:
                        return True
                return False
        # Robuste Ermittlung des Kontexts:
        ok = False
        cnt = 0
        while True:
            cnt += 1
            try:
                getBrowser = context.getBrowser
                ok = True
            except AttributeError:
                context = context.getContext()
                getBrowser = context.getBrowser
                ok = True
            if debug_active:
                print repr(context)
                print filter(f, dir(context))
            if ok or cnt >= 2:
                break

        request = context.REQUEST
        getBrowser('authorized').raiseAnon()
        userId = getBrowser('member').getId()
        fullname = getBrowser('member').getFullname()
        management = getBrowser('management')
        if not management.canAccessSiteManagement():
            request.set('suppress_management_link', True)

        getAdapter = context.getAdapter
        if not getAdapter('checkperm')('Portlets: Manage portlets'):
            request.form['suppress_portlet_management'] = True

        portal = getAdapter('portal')()
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        try:
            request.form['user_fullname'] = fullname  # Ansonsten wird oben in der top.pt "system" angezeigt
            form = context.restrictedTraverse('my_account_edit_form')(userId=userId)
            return form
        finally:
            sm.setOld()

    get = editProfile
