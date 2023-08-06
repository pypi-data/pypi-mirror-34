# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
Utils-Modul des Browsers tree
"""

def flattened(dic, key):
    """
    dic -- Ein dict, das eine Struktur mit einer Hierarchie von Kindelementen
           repräsentiert
    key -- Der Schlüssel, der für das übergebene dict und seine "Kinder"
           auf die Liste der Kindelemente verweist

    Es wird eine "flache Version" generiert; eine Überprüfung auf Duplikate
    findet nicht statt.
    Die ausgelesenen Schlüssel werden entfernt!

    >>> d = {'a': 1,
    ...      'subs': [{'a': 2,
    ...                'subs': None,
    ...                },
    ...               {'a': 3,
    ...                'subs': [{'a': 4},
    ...                         {'a': 5,
    ...                          'subs': [{'a': 6},
    ...                                   {'a': 7},
    ...                                   ]},
    ...                         ]},
    ...               ]}
    >>> list(flattened(d, 'subs'))
    [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}, {'a': 7}]
    >>> d = {'a': 1,
    ...      'subs': [{'a': 2,
    ...                'subs': [{'a': 3},
    ...                         ]},
    ...               {'a': 4},
    ...               ]}
    >>> list(flattened(d, 'subs'))
    [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
    """
    yield dic
    try:
        subs = dic.pop(key)
        if subs:
            for sub in subs:
                for val in flattened(sub, key):
                    yield val
    except KeyError:
        pass


def brain_dict(brain, parent_uid, level, currentAsBrain=True):
    """
    Gib für das übergebene Katalogobjekt ein dict zurück
    zum Aufbau einer Navigationsstruktur
    """
    if parent_uid is not None:
        assert isinstance(parent_uid, basestring)
    assert isinstance(level, int)
    dic = {'current': currentAsBrain and brain or brain.UID,
           'uid_object': brain.UID,
           'uid_parent': parent_uid,
           'portal_type': brain.portal_type,
           'level': level,
           'Title': brain.Title,
           'childs': list(),
           }
    return dic


if __name__ == '__main__':
    import doctest
    doctest.testmod()
