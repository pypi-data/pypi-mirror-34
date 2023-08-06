from dayta.browser.public import BrowserView, implements, Interface


class IReviewStates(Interface):

    def get(self):
        """ """


class Browser(BrowserView):

    implements(IReviewStates)

    def get(self):
        """ """
        context = self.context
        pw = context.getAdapter('pw')()
        list_ = []
        for review_state in ['published',
                             'inherit',
                             'visible',
                             'restricted',
                             'private']:
            dict_ = {}

            dict_['title'] = pw['dayta_workflow'].states[review_state].title
            dict_['id'] = review_state

            list_.append(dict_)
        return list_

    def getFCKList(self):
        """ """
        # siehe (gf) ../unitraccsearch/browser.py, getReviewStates 
        context = self.context
        pw = context.getAdapter('pw')()
        list_ = []
        for review_state in ['published',
                             'inherit',
                             'visible',
                             'accepted',
                             'submitted',
                             'private']:
            dict_ = {}

            dict_['title'] = pw['dayta_workflow'].states[review_state].title
            dict_['id'] = review_state

            list_.append(dict_)
        return list_
