# -*- coding: utf-8 -*-
"""\
Modul für verschiedene Suchutilities
"""

__author__ = "Enrico Ziese"
__date__  = "$22.01.2014$"


# Unitracc-Tools:
from visaplan.tools.coding import safe_decode
from visaplan.tools.debug import pp


def normalizeQueryString(string):
    r"""
    Gib eine Liste von Unicode-Strings zurück.
    Wenn keinerlei Asteriske enthalten sind, wird jedes enthaltene
    leerzeichengetrennte Wort vorn und hinten durch Asterisk ergänzt.
    (wer selbst Asteriske setzt, weiß, daß er sie explizit auch
    woanders setzen könnte)

    string -- ein UTF-8-codierter String

    >>> normalizeQueryString('abc')
    [u'*abc*']
    >>> normalizeQueryString(u'abc')
    [u'*abc*']
    >>> normalizeQueryString('ab*c')
    [u'ab*c']
    >>> normalizeQueryString('   abc\t  def  ')
    [u'*abc*', u'*def*']
    >>> normalizeQueryString('entkoppelte Förderschnecke ')
    [u'*entkoppelte*', u'*F\xf6rderschnecke*']
    >>> normalizeQueryString('rohr* leitung  ')
    [u'rohr*', u'leitung']
    >>> normalizeQueryString('rohr * leitung  ')
    [u'rohr', u'leitung']

    Durch die Verwendung von safe_decode darf auch Unicode übergeben werden;
    sogar bei latin-1 tritt kein Fehler auf:

    >>> normalizeQueryString(u'Förderschnecke')
    [u'*F\xc3\xb6rderschnecke*']
    """
    # searchstring is None or empty
    if not string:
        return []

    strings = safe_decode(string).split()
    if u'*' in strings:
        # ein alleinstehendes Asterisk würde *immer* passen;
        # also nur zur Unterdrückung der Automatik nutzen:
        return [s for s in strings
                if s != u'*'
                ]
    else:
        return [s.join((u'*', u'*'))
                for s in strings
                ]


def lsfactory_portal(o, distance=0, data=None): 
    """
    Gib die localsearch-Daten für das übergebene Portal zurück
    """
    return {'root': {'o': o,
                     'uid': None,
                     'path': o.getPath(),
                     }, 
            'distance': 0,
            'data': None,
            }

def create_lsfactory(getobject=False, get_okey=False):
    """
    Gib eine lsfactory zurück
    
    getobject -- beschaffe das Objekt, wenn nicht als o übergeben
                 (Vorgabe: False)
    get_okey -- stelle sicher, daß das 'root'-Dict. einen Schlüssel 'o'
                enthält (und sei er None; Vorgabe: False)
                Wenn das Objekt als o übergeben wird (und nicht None
                ist), ist das stets der Fall.
    """

    def lsfactory(brain, uid, data, distance, o=None):
        """
        Gib die localsearch-Daten für das übergebene Katalogobjekt zurück

        (zu übergeben an unitraccsettings._getInherited als
        factory-Argument)
        """
        root = {'brain': brain,  # sic!
                'uid': uid,
                'path': brain.getPath(),
                }
        if o is None and getobject:
            o = brain.getObject()
        if o is not None or get_okey:
            root['o'] = o
        return {'root': root,
                'distance': distance,
                'data': data,
                }
    return lsfactory


def create_flatlsfactory(func):
    """
    Gib eine Funktion zurück, die für das übergebene "Brain" ein Python-Dict zurückgibt,
    das alle übergebenen Schlüssel enthält.  Eine Sequenz entsprechender
    Rückgabewerte kann dann nach JSON konvertiert werden.

    Zusätzlich zu den angegebenen Metadatenfeldern wird ein Schlüssel "href" erzeugt
    (die brain-Methode getPath sollte die performanteste Lösung sein, oder?)

    names - die Feldnamen des Dict (ohne 'href', das generell erzeugt wird)
    func - eine Funktion, die unzulässige Namen beanstandet oder entfernt
           (siehe tools.misc.make_names_tupelizer)
    """

    def intermediate(names):
        names = func(names)

        fields_simple = []
        fields_conv = []
        for name in names:
            if '/' in name:
                src, method = name.split('/', 1)
                fields_conv.append((name, src, method))
            else:
                fields_simple.append(name)

        def _basiclist(brain, names):
            liz = []
            for key in names:
                a = getattr(brain, key, None)
                if not a:
                    if a is None:
                        pass
                    elif isinstance(a, int):
                        pass
                    elif isinstance(a, basestring):
                        a = a.strip()
                    else:
                        # TODO: was tun mit Value.Missing? 
                        a = None
                liz.append((key, a))
            url_list = brain.getPath().split('/')
            del url_list[1]
            liz.append(('href', '/'.join(url_list)))
            return liz

        def flatdict(brain):
            return dict(_basiclist(brain, names))

        def smartdict(brain):
            """
            Wie flatdict, aber mit Berücksichtigung zu konvertierender Felder
            """
            liz = _basiclist(brain, fields_simple)
            for name, src, method in fields_conv:
                a = getattr(brain, src)
                if a is not None:
                    v = getattr(a, method)()
                    liz.append((name, v))
            return dict(liz)

        if fields_conv:
            return smartdict
        else:
            return flatdict

    return intermediate


if __name__ == "__main__":
    import doctest
    doctest.testmod()

