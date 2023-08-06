from tomcom.browser.public import *
from collective.ckeditor.browser.ckeditorfinder import *

class IUnitraccCKFinder(Interface):

    pass

class Browser(CKFinder):

    implements(IUnitraccCKFinder)

    def __call__(self):

        context=self.context

        return context.restrictedTraverse('unitraccckfinder_search')()