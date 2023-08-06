# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
from dayta.browser.public import BrowserView, implements, Interface

from App.config import getConfiguration
conf = getConfiguration()
env = conf.environment
MINIMUM_PASSWORD_LENGTH = env.get('MINIMUM_PASSWORD_LENGTH', 5)
try:
    MINIMUM_PASSWORD_LENGTH = int(MINIMUM_PASSWORD_LENGTH)
except ValueError:
    MINIMUM_PASSWORD_LENGTH = 5

if 0 and 'Futter fuer den Parser':
    _('Empty password is not allowed.')
    _('Password is too short; at least %(minlength)r characters required.')
    _('The new password and the repetition are not the same.')


class InvalidPassword(ValueError):
    def mkmsg(self, translate, **kwargs):
        self.msg = translate(self.msgmask) % kwargs

    def __str__(self):
        return self.msg

    def __init__(self, translate):
        self.mkmsg(translate)


class EmptyPassword(InvalidPassword):
    msgmask = 'Empty password is not allowed.'


class PasswordTooShort(InvalidPassword):
    msgmask = 'Password is too short; at least %(minlength)r characters required.'

    def __init__(self, translate, minlength):
        self.minlength = minlength
        self.mkmsg(translate, minlength=minlength)


class IPassword(Interface):

    def change(self):
        """ """

    def validate(self, password, translate):
        """
        pruefe den uebergebenen Wert auf Zulaessigkeit als Passwort
        und wirf ggf. einen ValueError
        """


class Browser(BrowserView):

    implements(IPassword)

    def change(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        message = context.getAdapter('message')
        _ = self.context.getAdapter('translate')

        # check permission:
        context.getBrowser('tpcheck').auth_set_own_password()

        password = form.get('password', '')
        passwordValidation = form.get('passwordValidation', '')

        error = False
        try:
            self.validate(password, _)
        except InvalidPassword as e:
            error = True
            message(str(e), 'error')
        else:
            if password != passwordValidation:
                error = True
                message(_('The new password and the repetition are not the same.'),
                        'error')

        if not error:
            memberId = context.getBrowser('member').getId()
            acl = context.getAdapter('acl')()
            acl.userSetPassword(memberId, password)

            message(_('Changes saved.'))

        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def validate(self, password, translate):
        """
        pruefe den uebegebenen Wert auf Zulaessigkeit als Passwort
        und wirf ggf. einen ValueError
        """
        global MINIMUM_PASSWORD_LENGTH
        if not password:
            raise EmptyPassword(translate)
        length = len(password)
        if length < MINIMUM_PASSWORD_LENGTH:
            raise PasswordTooShort(translate, MINIMUM_PASSWORD_LENGTH)
