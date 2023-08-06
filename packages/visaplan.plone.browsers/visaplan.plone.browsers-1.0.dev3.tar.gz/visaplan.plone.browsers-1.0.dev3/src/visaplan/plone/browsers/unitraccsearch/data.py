# -*- coding: utf-8 -*-
"""\
unitraccsearch.data
"""

# Standardmodule:
from collections import defaultdict
from os.path import dirname, join

def read_local_file(fn):
    """
    Gib den Inhalt der übergebenen Datei zurück;
    die Verwendung im Quellcode erlaubt den Zugriff per "gf"-Kommando (vim)
    """
    qfn = join(dirname(__file__), fn)
    with open(qfn, 'r') as f:
        return f.read()


BASENAMES = ('Title getURL author_name Creator portal_type getThumbnailPath '
             'Description review_state'
             ).split()
# --------------- [ zu ./templates/localsearch_view.pt ... [
localsearch_presets_default = {  # ls_preset
        'default': {
            # Beschriftung für die Auswahl in der Konfigurationssicht:
            'label': '"responsive table" with thumbnails column'
                     ' (two columns total);'
                     ' standard item information',
            # die aufzurufende Sicht:
            'list_view': 'localsearch_monotable',
            # von der Sicht <list_view> zu verwendende Makros:
            'list_macro': 'localsearch_macros/macros/monotable-list',
            # 'item_macro': None, # noch wird hier kein Makro verwendet
        },
        'nothumbnails': {
            # Beschriftung für die Auswahl in der Konfigurationssicht:
            'label': '"responsive table" without thumbnails column'
                     ' (one column only);'
                     ' standard item information',
            # 'list_view': 'listing_responsive',
            # die aufzurufende Sicht:
            'list_view': 'localsearch_monotable',
            # von der Sicht <list_view> zu verwendende Makros:
            'list_macro': 'localsearch_macros/macros/monotable-list1',
            # 'item_macro': None, # noch wird hier kein Makro verwendet
        },
    }
# Vorgabewerte vorerst einfach aus localsearch_presets_default übernommen:
PRESETS_DEFAULTS = {
    'list_view': 'localsearch_monotable',
    # von der Sicht <list_view> zu verwendende Makros:
    'list_macro': 'localsearch_macros/macros/monotable-list',
    }
# Makros zu serverseitigen Darstellung von Listeneinträgen:
DISPLAY_ITEM_MACROS = [
    'unitraccnora_macros/macros/item',  # News oder Artikel; auf Startseite
    # Veröffentlichungsdatum, Fachbereich, Überschrift, Beschreibung: 
    'unitraccmacros/macros/unitraccitem_generic',
    ]
THUMBNAIL_COLUMN = read_local_file('render_thumbnail_column.js')
localsearch_json_presets_default = {
        'default': {
            'label': 'media list, excluding date information',
            'names': ['getThumbnailPath', 'Title', 'Descriptíon', 'getCode',
                      ],
            # --------- [ Integration serverseitiger Generierung ... [
            'description': None,  # siehe localsearch_presets_default, label
            'list_view': PRESETS_DEFAULTS['list_view'],
            'list_macro': PRESETS_DEFAULTS['list_macro'],
            # möglicherweise das einzige variierende: 
            'item_macro': 'x/macros/y',
            # --------- ] ... Integration serverseitiger Generierung ]
            # wichtig: "columns", nicht "columnDefs" !
            # https://datatables.net/reference/option/columns.render:
            'columns': ("""
            [{"data": "getThumbnailPath",
              "render": %s
              },
             {"data": null,
              "render": %s
              }]
              """
            % (# linke Spalte: nur Vorschaubild
               THUMBNAIL_COLUMN,
               # rechte Spalte: alle Inhalte 
               read_local_file('render_catchall_media_column.js'),
               )).strip(),
        },
        'books': {
            'label': 'Setup for books (including date and author information)',
            'names': ['getThumbnailPath', 'Title', 'Descriptíon',
                      'getCode',
                      'Rights',  # Autoreninformation
                      'getDateForList/year',
                      ],
            'columns': ("""
            [{"data": "getThumbnailPath",
              "render": %s
              },
             {"data": null,
              "render": %s
              }]
              """
            % (# linke Spalte: nur Vorschaubild
               THUMBNAIL_COLUMN,
               # rechte Spalte: alle Inhalte 
               read_local_file('render_catchall_book_column.js'),
               )).strip(),
        },
        'courses': {
            'label': 'courses, with booking buttons and special hyperlinks',
            'names': ['getThumbnailPath', 'Title', 'Descriptíon',
                      'getDateForList/year',
                      # wichtig bei Kursen, wegen des Links: 
                      'UID',
                      # ... für die Buchung: 
                      'getPrice', 'getDuration',
                      ],
            'columns': ("""
            [{"data": "getThumbnailPath",
              "render": %s
              },
             {"data": null,
              "render": %s
              }]
              """
            % (# linke Spalte: nur Vorschaubild
               THUMBNAIL_COLUMN,
               # rechte Spalte: alle Inhalte 
               read_local_file('render_catchall_course_column.js'),
               )).strip(),
        },
    }
# Die Vorgabe für den Fall, daß im Ordner oder seinen Eltern
# noch nichts konfiguriert wurde:
localsearch_json_default = dict(localsearch_json_presets_default['default'])
# --------------- ] ... zu ./templates/localsearch_view.pt ]

# --------- [ zu ../../skins/unitracc_templates/top.pt ... [
layout_to_action_suffix = defaultdict(lambda: 'search_view')
layout_to_action_suffix.update({
    # die folgenden Seiten stellen ihre Suchergebnisse selbst dar: 
    'localsearch_view': None,
    'event_folder_view': None,
    })
# --------- ] ... zu ../../skins/unitracc_templates/top.pt ]

FORBIDDEN_BRAIN_ATTRIBUTES = [# wird stets berechnet:
                              'href',
                              # Methoden, und damit nicht serialisierbar;
                              # stattdessen 'href' verwenden: 
                              'getURL', 'getPath', 'getObject',
                              ]
DATATABLES_TEMPLATE = read_local_file('datatables.js')
