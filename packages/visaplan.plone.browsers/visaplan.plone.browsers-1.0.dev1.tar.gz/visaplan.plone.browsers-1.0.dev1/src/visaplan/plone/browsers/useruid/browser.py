from dayta.browser.public import BrowserView, implements, Interface
from hashlib import md5


class IUserUid(Interface):

    def set():
        """
        Erzeuge das Cookie 'useruid', falls noch nicht vorhanden
        """

    def get():
        """
        Lies das Cookie 'useruid' aus
        """


class Browser(BrowserView):

    implements(IUserUid)

    key = 'useruid'  # hier nicht mehr verwendet

    def set(self):
        """
        Erzeuge das Cookie 'useruid', falls noch nicht vorhanden
        """
        REQUEST = self.context.REQUEST
        cookies = REQUEST.cookies
        if not cookies.has_key('useruid'):
            get = REQUEST.get
            value = md5(get('HTTP_X_FORWARDED_FOR', '') +
                        get('HTTP_USER_AGENT', '') +
                        get('channel.creation_time', '')
                        ).hexdigest()
            REQUEST.RESPONSE.setCookie('useruid', value, path='/')

    def get(self):
        """
        Lies das Cookie 'useruid' aus
        """
        return self.context.REQUEST.cookies.get('useruid', '')
