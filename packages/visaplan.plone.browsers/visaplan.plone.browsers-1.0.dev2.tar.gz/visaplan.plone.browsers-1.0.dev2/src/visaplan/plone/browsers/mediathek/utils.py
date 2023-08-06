# -*- coding: utf-8 # äöü
"""
unitracc@@mediathek.utils
"""

# Unitracc-Tools
from visaplan.tools.lands0 import groupstring


def get_code(o):
    """
    Für Mediathek-Objekte: lies den Fachbereich aus und gib ihn als Liste zurück
    """
    code = o.getCode()
    if (not code
        or code in ('**',
                    'NODOMAIN',
                    )
        ):
        return ['NODOMAIN']
    return groupstring(code, 2)
