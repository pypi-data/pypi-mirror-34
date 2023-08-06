from dayta.browser.public import BrowserView, implements, Interface


class IPartner(Interface):

    def get(self, brain):
        """ """


class Browser(BrowserView):

    implements(IPartner)

    def get(self, brain):
        """ """
        context = self.context
        stage = context.getBrowser('stage')

        if brain.getPartOf:
            return stage.getAsBrains('unitracc-partner', brain.getPartOf)
        else:
            return stage.getAsBrains('unitracc-partner', brain.UID)
