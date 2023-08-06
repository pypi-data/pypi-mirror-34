# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79
"""
@@unitraccfeature - Informationen über grundlegende Eigenschaften der Instanz

Die Eigenschaften werden üblicherweise während der Laufzeit nur einmal
ermittelt;  da die Verwendung von zope.component.hooks.getSite() ohne Request
fehlschlägt (siehe utils-Modul), muß dies verzögert erfolgen.
"""

from dayta.browser.public import BrowserView, implements, Interface

# Systemmodule:
from .utils import (FeaturesInfo, MYUNITRACC_UID, THE_KEYS, LOGGER,
        sitecustomize_info,
        )

# Unitracc-Tools:
from visaplan.plone.tools.cfg import get_debug_active
debug_active = get_debug_active('unitraccfeature')

FEATURESINFO = FeaturesInfo()

if debug_active:
    LOGGER.info('*'*79 + '\n'+__file__)

    LOGGER.info('FEATURESINFO: %s', FEATURESINFO)


# sitecustomize_info()


class IUnitraccFeatureBrowser(Interface):
    """
    Informationen über grundlegende Eigenschaften der Instanz
    """

    def all():
        """
        Gib ein dict aller vorhandenen Informationen zurück
        """

    def rootfolder():
        """
        Das Wurzelverzeichnis (unitracc oder vdz)
        """

    def reset():
        """
        Vergiß alle vorhandenen Informationen
        """

    def has_articles():
        """
        Gibt es im "Aktuelles"-Bereich Artikelseiten?
        """


class Browser(BrowserView):
    """
    Informationen über grundlegende Eigenschaften der Instanz
    """
    implements(IUnitraccFeatureBrowser)

    def __init__(self, *args, **kwargs):
        BrowserView.__init__(self, *args, **kwargs)

    def all(self):
        """
        Gib ein dict aller vorhandenen Informationen zurück
        """
        FEATURESINFO["rootfolder"]
        return FEATURESINFO

    def _reset(self):
        """
        Vergiß alle vorhandenen Informationen
        """
        # ungetestet
        FEATURESINFO.clear()

    def reset(self):
        """
        Vergiß alle vorhandenen Informationen
        """
        context = self.context
        context.getAdapter('authorized')('Manage portal')
        message = context.getAdapter('message')
        FEATURESINFO.clear()
        message('Features information reset')
        request = context.REQUEST
        response = request.RESPONSE
        return response.redirect(request['HTTP_REFERER'])

    def asList(self):
        """
        Gib das Dictionary als sortierte Liste
        von {'key': ..., 'value': ...}-Dictionarys aus
        """
        FEATURESINFO[THE_KEYS[0]]
        keys = sorted(FEATURESINFO.keys())
        keys.reverse()
        liz = []
        for key in keys:
            liz.append({'key': key,
                        'value': FEATURESINFO[key],
                        })
        return liz

    def rootfolder(self):
        """
        Das Wurzelverzeichnis (unitracc oder vdz)
        """
        return FEATURESINFO["rootfolder"]

    def has_articles(self):
        """
        Gibt es im "Aktuelles"-Bereich Artikelseiten?
        """
        return FEATURESINFO["has_articles"]

    def has_booking(self):
        """
        Ist hier das Buchungssystem aktiv?
        """
        return FEATURESINFO["has_booking"]

    def has_advertising(self):
        """
        Gibt es hier Kurse?
        (keine w3l-Anbindung, sondern Unitracc-Kurse)
        """
        return FEATURESINFO["has_advertising"]

    def has_courses(self):
        """
        Gibt es hier Kurse?
        (keine w3l-Anbindung, sondern Unitracc-Kurse)
        """
        return FEATURESINFO["has_courses"]

    def courses_uid(self):
        """
        UID des Kursordners, wenn has_courses
        """
        return FEATURESINFO["courses_uid"]

    def has_flexpaper(self):
        """
        Gibt es hier Flexpaper-Dokumente?
        (spezielle aus PDF-Dokumenten erzeugte Flash-Dateien zur
        Online-Ansicht)
        """
        return FEATURESINFO["has_flexpaper"]

    def desktop_id(self):
        """
        ID des Schreibtischobjekts ('myunitracc' oder 'schreibtisch')
        """
        return FEATURESINFO["desktop_id"]

    def desktop_path(self):
        """
        Pfad des Schreibtisches
        """
        return FEATURESINFO["desktop_path"]

    def ejournal_columns(self):
        """
        Wieviele Einträge pro Spalte für News und Artikel?
        """
        return FEATURESINFO["ejournal_columns"]

    def board_guidelines(self):
        """
        Forenrichtlinien UID je nach Plattform (WNZKB, Unitracc)
        """
        return FEATURESINFO["board_guidelines"]
