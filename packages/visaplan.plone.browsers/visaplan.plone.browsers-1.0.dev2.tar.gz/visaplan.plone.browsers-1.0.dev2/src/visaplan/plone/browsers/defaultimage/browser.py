# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=72 cc=+8
from dayta.browser.public import BrowserView, implements, Interface

# ------------------------------------------- [ Daten ... [
SCALING = '120x120'
DEFAULT_IMG_NAME = 'article_default_%(SCALING)s.jpg' % globals()
# ------------------------------------------- ] ... Daten ]


class IDefaultImage(Interface):

    def get(self):
        """ """


class Browser(BrowserView):

    implements(IDefaultImage)

    def get(self):
        """ """
        context = self.context

        # getAdapter: für aufrufenden Kontext
        getAdapter = context.getAdapter
        portal = getAdapter('portal')()

        data = ''
        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            form = context.REQUEST.form
            uid = form.get('uid')

            #Because we set the security to a master user we only allow one scaling to be delivered
            form.update({'scaling': SCALING})

            rc = getAdapter('rc')()
            context = rc.lookupObject(uid)
            # getBrowser: für aus übergebener UID ermittelten Kontext
            getBrowser = context.getBrowser
            portal_type = context.portal_type

            if portal_type == 'UnitraccNews':
                browser = getBrowser('news')
                data = browser.getImage(context.UID())
            elif portal_type == 'UnitraccArticle':
                browser = getBrowser('article')
                #returns an url
                url = browser.getFirstImage(context.getHereAsBrain(), SCALING)

                #is it an url we can use
                split_url = url.split('/')
                if split_url[2:]:
                    uid = split_url[2]
                    object_ = rc.lookupObject(uid)
                    if object_:
                        browser = object_.getBrowser('scaling')
                        data = browser.get()
                    else:
                        data = str(context.restrictedTraverse(DEFAULT_IMG_NAME)._data)
            elif portal_type in ('UnitraccImage',
                                 'UnitraccAnimation',
                                 ):
                browser = getBrowser('scaling')
                data = browser.get()
            elif portal_type == 'Document':
                brain = getBrowser('book').getBookFolderAsBrain()
                if brain:
                    brains = getBrowser('stage').getAsBrains('illustration', brain.UID)
                    if brains:
                        form.update({'scaling': SCALING})
                        data = brains[0].getObject().getBrowser('scaling').get()
        finally:
            sm.setOld()
            return data
