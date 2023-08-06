# Standardmodule:
from DateTime import DateTime

# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface

class IServiceNews(Interface):

    pass


class Browser(BrowserView):

    implements(IServiceNews)

    def __call__(self):
        """ """
        context=self.context

        portal=context.getAdapter('portal')()
        sm=portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()

        try:
            pc=context.getAdapter('pc')()._catalog
            browser=context.getBrowser('news')
            queryDate=DateTime()-browser.days

            query={}
            query['portal_type']='UnitraccNews'
            query['created']={'query':queryDate,
                              'range':'max'}
            query['effective']={'query':queryDate,
                                'range':'max'}
            query['review_state']=['published','inherit']

            for brain in pc(query):
                object_=brain.getObject()
                object_.getBrowser('workflow').change('make_visible')

        finally:
            sm.setOld()

        return True
