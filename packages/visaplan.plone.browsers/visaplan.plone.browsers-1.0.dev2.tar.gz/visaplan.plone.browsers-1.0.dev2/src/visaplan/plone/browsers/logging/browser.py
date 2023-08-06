# -*- coding: utf-8 -*- äöü
from dayta.browser.public import BrowserView, implements, Interface

import logging
logger = logging.getLogger('unitracc@@logging')


class ILogging(Interface):

    def log(self, txt=None, **kwargs):
        """
        log-Methode, gestrickt nach den Aufrufen aus dem mail-Browser
        (tomcom.mail 4.3.0.3)
        """


class Browser(BrowserView):

    implements(ILogging)

    def log(self, txt=None, *args, **kwargs):
        """
        log-Methode, gestrickt nach den Aufrufen aus dem mail-Browser
        (tomcom.mail 4.3.0.3)
        """

        if txt is None:
            # angetroffene Aufrufe: genau ein Schlüsselwortargument
            txt = ', '.join(['%s=%r' % tup
                             for tup in kwargs.items()
                             ])
            logger.info(txt)
        elif kwargs:
            logger.info(txt, kwargs)
        elif args:
            logger.info(txt, *args)
