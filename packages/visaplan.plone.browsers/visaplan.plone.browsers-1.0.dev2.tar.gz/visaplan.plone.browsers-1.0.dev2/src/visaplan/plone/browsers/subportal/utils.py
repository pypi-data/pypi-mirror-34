# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et
"""
utils-Modul für den Browser unitracc@@subportal
"""

# Standardmodule:
from urlparse import urlsplit, urlunsplit


def get_hostname(s):
    """
    >>> get_hostname('http://unitracc.de')
    'unitracc.de'
    >>> get_hostname('vbox-therp')
    'vbox-therp'
    """
    ntup = urlsplit(s)
    if ntup.scheme:
        return ntup.netloc
    else:
        return ntup.path


def detect_project(hostnames, dic):
    """
    >>> b_list=['http://wissensnetzwerk-steine-erden.de',
    ...         'http://biruzem.wissensnetzwerk-steine-erden.de',
    ...         'http://biruzem.unitracc.de',
    ...         'http://wnzkb-plone4.unitracc.de']
    >>> detect_project(b_list, None)
    'biruzem'

    >>> w_list=['http://wissensnetzwerk-steine-erden.de',
    ...         'http://wnzkb-plone4.unitracc.de']
    >>> detect_project(w_list, {'rootfolder': 'vdz'})
    'wnzkb'
    >>> detect_project(w_list, {'rootfolder': 'unitracc'})
    'unitracc'
    >>>
    """
    for line in hostnames:
        name = get_hostname(line)
        liz = name.replace('.', ' ').replace('-', ' ').split()
        for seg in liz:
            if seg in ('aqwa', 'biruzem'):
                return seg
    # bis hierher nichts eindeutiges
    if dic['rootfolder'] == 'vdz':
        return 'wnzkb'
    return 'unitracc'


LINK_KEYS = tuple(reversed(['lang_code', 'image_id', 'url', 'alt']))
LINK_DICT = {}
for key in LINK_KEYS:
    LINK_DICT[key] = None
del key


def lang_from_hostname(hostname):
    """
    Extrahiere die erste "Sprache" aus dem Hostnamen,
    wobei das extrahierte Sprachkürzel auch 'com' oder 'net' sein kann:

    >>> lang_from_hostname('dev-com.unitracc.de')
    'com'
    """
    hostname_snippets = hostname.replace('.', ' ').replace('-', ' ').split()
    for snippet in hostname_snippets:
        if snippet in ('de', 'com', 'net', 'es'):
            return snippet
    return None  # pep 20.2


def img_link_dict(z):
    """
    Erzeuge ein dict für die Ausgabe der Partnerlinks im Seitentitel

    >>> sorted(img_link_dict('de;bildchen.jpg;http://unitracc.de;').items())
    [('alt', None), ('host_lang', 'de'), ('hostname', 'unitracc.de'), ('image_id', 'bildchen.jpg'), ('lang_code', 'de'), ('url', 'http://unitracc.de')]

    Aus dem (bislang i.d.R. als URL angegebenen) Hostnamen wird eine Sprachinformation extrahiert, die ggf. 'net' oder 'com' sein kann:
    >>> sorted(img_link_dict('de;bildchen.jpg;http://dev-com.unitracc.de;').items())
    [('alt', None), ('host_lang', 'com'), ('hostname', 'dev-com.unitracc.de'), ('image_id', 'bildchen.jpg'), ('lang_code', 'de'), ('url', 'http://dev-com.unitracc.de')]
    """
    keys = list(LINK_KEYS)
    dic = dict(LINK_DICT)
    values = z.split(';')
    while keys:
        try:
            val = values.pop(0) or None
        except IndexError:
            val = None
        key = keys.pop()
        dic[key] = val
    try:
        hostname = dic['hostname'] = get_hostname(dic['url'])
        hostname_snippets = hostname.replace('.', ' ').replace('-', ' ').split()
        for snippet in hostname_snippets:
            if snippet in ('de', 'com', 'net', 'es'):
                dic['host_lang'] = snippet
                break
    except (KeyError, ValueError, TypeError, AttributeError) as e:
        pass
    if values:
        logger.warning('%(z)r: surplus values (%(values)s)', locals())
    return dic
    if dic['alt'] is not None:
        return dic
    # TODO: Schlaue Defaults fuer alt


def make_prefixer(prefix='/'):
    """
    Erzeuge eine Funktion, die ein Präfix anwendet

    >>> prefixed=make_prefixer('/default-base')
    >>> prefixed('logo.png')
    '/default-base/logo.png'
    >>> prefixed('./logo.png')
    './logo.png'

    Ein '~' als letztes Zeichen unterdrückt die automatische Ergänzung des '/' am Ende:
    >>> prefixed=make_prefixer('sub/path/and/prefix~')
    >>> prefixed('logo.png')
    '/sub/path/and/prefixlogo.png'
    """
    if not prefix:
        prefix = '/'
    else:
        liz = []
        if prefix[0] not in './':
            liz.append('/')
        if prefix.endswith('~'):
            liz.append(prefix[:-1])
        else:
            liz.append(prefix)
            if not prefix.endswith('/'):
                liz.append('/')
        prefix = ''.join(liz)
            
    def prefixed(fn):
        if '/' in fn:
            return fn
        return prefix+fn

    return prefixed

def create_subportalId(frame, title):
    r"""
    Erzeuge eine (höchstwahrscheinlich eindeutige) ID für ein neues Subportal

    >>> create_subportalId('0123456789abcdef0123456789abcdef', 'BetonQuali')
    'betonquali-bcdef0123456789abcdef'
    >>> create_subportalId('0123456789abcdef0123456789abcdef', '\tBetonQuali\n')
    'betonquali-bcdef0123456789abcdef'
    >>> create_subportalId('0123456789abcdef0123456789abcdef', '')
    '0123456789abcdef0123456789abcdef'
    """
    if not title:
        return frame
    fromtitle = '-'.join(title.split()).lower()
    framelist = list(frame)
    titlelist = list(fromtitle) + ['-']
    framelength = len(framelist)
    ol_length = min(framelength, len(titlelist))
    framelist[0:ol_length] = titlelist[:ol_length]
    return ''.join(framelist)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
