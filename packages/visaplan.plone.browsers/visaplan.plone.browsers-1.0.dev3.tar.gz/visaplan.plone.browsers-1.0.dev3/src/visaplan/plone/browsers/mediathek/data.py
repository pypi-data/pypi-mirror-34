# -*- coding: utf-8 # äöü
"""
unitracc@@mediathek.data
"""

# Andere Browser
from ..unitraccfeature.utils import (MEDIATHEK_UID, ARTICLESFOLDER_UID,
        EVENTSFOLDER_UID, COURSESFOLDER_UID, NEWSFOLDER_UID,
        )
# hier andere Namenskonvention:
from ..structuretype.browser import (
        UID_LITERATURE as LITERATURE_UID,
        )

# -------------------------------------------- [ Daten ... [
MEDIATHEK_TYPES = ['UnitraccFile',
                   'UnitraccImage',
                   'UnitraccTable',
                   'UnitraccFormula',
                   'UnitraccBinary',
                   'UnitraccAnimation',
                   'UnitraccAudio',
                   'UnitraccVideo',
                   ]
DESTINATION_MAP = {
        'UnitraccArticle':	ARTICLESFOLDER_UID,
        'UnitraccNews': 	NEWSFOLDER_UID,
        'UnitraccEvent':	EVENTSFOLDER_UID,
        'UnitraccGlossary':	'12995b34a21e093a3bc5841dc18759bc',
        'UnitraccLiterature':	LITERATURE_UID,
        'UnitraccStandard':	'6e919abf7cb110e23651a583ac5ea308',
        'UnitraccCourse':	COURSESFOLDER_UID,
        }
# -------------------------------------------- ] ... Daten ]
