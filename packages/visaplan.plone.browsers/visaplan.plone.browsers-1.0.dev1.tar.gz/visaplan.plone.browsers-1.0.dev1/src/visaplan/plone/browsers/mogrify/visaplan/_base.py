# -*- coding: utf-8 -*- äöü
# @@mogrify.visaplan._base

# Unitracc-Tools:
from ....tools.misc import getOption
from visaplan.tools.lands0 import makeListOfStrings
from visaplan.tools.minifuncs import makeBool

class BaseSection(object):
    """
    Basisklasse für Transmogrifier-Sektionen

    classProvides und implements müssen mutmaßlich in jeder abgeleiteten Klasse
    direkt aufgerufen werden. Direkt in der Klasse:

    classProvides(ISectionBlueprint)
    implements(ISection)
    """

    def __init__(self, transmogrifier,
                 name,    # Sektionsname
                 options, # Optionen aus Sektion oder transmogrifier-kwargs
                 previous):
        self._store_initial_args(self, transmogrifier, name, options, previous)

    def _store_initial_args(self,
                 transmogrifier,
                 name,    # Sektionsname
                 options, # Optionen aus Sektion oder transmogrifier-kwargs
                 previous):
        self.previous = previous
        self.name = name
        self.context = transmogrifier.context
        self.count = transmogrifier.create_itemcounter(name)
        self._set_debugging_options(options)

    def _set_debugging_options(self, options):
        """
        Allgemeine Debugging-Optionen auswerten;
        die konkrete Verwendung dieser Optionen wird vollständig durch den Code
        der jeweiligen Sektion realisiert.
        Es ist also durchaus möglich, daß einzelne Sektionen nur eine
        Untermenge der hier zugewiesenen Optionen verwenden!

        Debugging dieser Sektion wird erwogen:
        - wenn kein Schlüssel 'debug-sections' vorhanden,
          oder
        - wenn er vorhanden und der Sektionsname enthalten ist

        Ein leerer Schlüssel 'debug-sections' schaltet das Debugging also für
        alle Sektionen ab.
        """
        if 'debug-sections' in options:
            sections = getOption(options, 'debug-sections',
                                 None, makeListOfStrings)
            if sections is not None:
                consider_debugging = self.name in sections
            else:
                consider_debugging = False
        else:
            consider_debugging = True

        # keine Debugging-Option im engeren Sinne:
        self.verbose = getOption(options, 'verbose', 'no', makeBool)

        if not consider_debugging:
            self.debug_ids = None
            self.trace1st = False
            return
        # IDs, die Debugging auslösen: 
        self.debug_ids = getOption(options, 'debug-ids', None,
                                   makeListOfStrings)
        # set_trace bei erstem (oder erstem interessanten) Objekt:
        self.trace1st = getOption(options, 'trace-first', 'no', makeBool)
