# -*- coding: utf-8 -*- äöü
"""
mogrify@@utils
"""

# Standardmodule:
from posixpath import normpath as normpath_posix, split as split_posix
from os.path import normpath, join
from tempfile import mkstemp
import HTMLParser

# Plone/Zope:
from Products.GenericSetup.context import DirectoryImportContext

# Installierte Module:
from bs4 import BeautifulSoup

# Unitracc-Tools:
from visaplan.kitchen.spoons import extract_uids
from visaplan.plone.tools.functions import is_uid_shaped
from visaplan.tools.classes import Proxy


__all__ = ['bool2text',
           'prefix_paths',
           'make_prefixer',
           'make_childonly_filter',
           'rebased_sourcelist',  # /root entfernen
           'checked_sourcelist',  # /root ergänzen
           'wrapped_tarball',
           'all_uids',
           'make_dirProxy',
           'make_readableNameFactory',
           'make_pathFilter',
           'log_module',
           ]


def bool2text(b):
    """
    Die Sections von collective.transmogrifier
    wollen nur String-Argumente!
    """
    return b and 'true' or 'false'


def prefix_paths(seq, func):
    """
    Stelle sicher, daß alle Elemente der Sequenz Pfade unter der Portalwurzel (ID: root) enthalten

    >>> prefixer = make_prefixer('/Plone')
    >>> prefix_paths(('/Plone/schonok', 'relativ', '/absolut'), prefixer)
    ['/Plone/absolut', '/Plone/relativ', '/Plone/schonok']
    """
    res = set()
    for p in seq:
        p = func(p)
        if not p:
            continue
        res.add(p)
    return sorted(res)


def make_prefixer(root, add=True):
    """
    Erzeuge eine Funktion, die das übergebene Präfix hinzufügt (add=True)
    oder entfernt (add=False)

    >>> prefix = make_prefixer('root', True)
    >>> prefix('somewhere')
    '/root/somewhere'
    >>> prefix('/somewhere')
    '/root/somewhere'
    >>> prefix('/root/somewhere')
    '/root/somewhere'

    >>> unprefix = make_prefixer('root', False)
    >>> unprefix('somewhere')
    'somewhere'
    >>> unprefix('/root/elsewhere')
    'elsewhere'
    """
    tmp = root.strip('/')
    if not tmp:
        raise ValueError('root angeben, z. B. /unitracc')
    prefix0 = '/' + tmp
    prefix = prefix0 + '/'

    def add_prefix(s):
        if s.startswith(prefix):
            return s
        if s == prefix0:
            return s
        if s.startswith('/'):
            return prefix0 + s
        return prefix + s

    if add:
        return add_prefix

    offset = len(prefix)
    def del_prefix(s):
        return add_prefix(s)[offset:]

    return del_prefix


def make_childonly_filter(root,
                          normalize=normpath_posix,
                          sep='/',
                          current=''):
    """
    Erzeuge eine Funktion, die einen übergebenen absoluten Pfad
    als zur übergebenen <root> relativen Pfad zurückgibt

    >>> childpath = make_childonly_filter('/path/to/root')
    >>> childpath('/path/to/root/and/beyond')
    'and/beyond'
    >>> childpath('/path/to/root//and/beyond')
    'and/beyond'

    Wenn der übergebene Pfad nicht unter dem root-Pfad liegt,
    gibt es einen ValueError:
    >>> childpath('/ganz/wo/anders')
    Traceback (most recent call last):
        ...
    ValueError: '/ganz/wo/anders' is not located below '/path/to/root'!

    Ist der Pfad mit <root> identisch, wird der spezielle Wert für <current>
    verwendet:
    >>> childpath('/path/to/root/')
    ''
    """
    root = normalize(root)
    if not root.startswith(sep):
        raise ValueError('Absolute path expected! '
                         '(starting with %(sep)r; '
                         'given: %(root)r)'
                         % locals())
    root2 = root + sep
    offset = len(root2)

    def childonly(p):
        pn = normalize(p)
        if pn.startswith(root2):
            return pn[offset:] or current
        elif pn == root:
            return current
        elif not pn.startswith(sep):
            return pn
        raise ValueError('%r is not located below %r!'
                         % (pn, root))
    return childonly


def rebased_sourcelist(raw, root, allow_empty=False,
                       as_string=None, as_list=None):
    r"""
    >>> roots_list = ['/root/eins', '/root/zwei']
    >>> rebased_sourcelist(roots_list, '/root')
    ['eins', 'zwei']

    Wenn ein String übergeben wird, kommt das Ergebnis als String zurück:

    >>> rebased_sourcelist('\n'.join(roots_list), '/root')
    'eins\nzwei'

    Die Rückgabe als String ("Zeilen", ohne abschließendes '\n')
    kann auch unabhängig vom Eingabetyp erzwungen werden:

    >>> rebased_sourcelist(roots_list, '/root', as_string=True)
    'eins\nzwei'

    Wenn die Wurzel direkt enthalten ist, wird diese Angabe mit
    allow_empty=False (Vorgabe) ausgefiltert:

    >>> roots_list.append('/root')
    >>> roots_list
    ['/root/eins', '/root/zwei', '/root']
    >>> rebased_sourcelist(roots_list, '/root')
    ['eins', 'zwei']

    Die Eingabeliste wird dabei nicht verändert:

    >>> roots_list
    ['/root/eins', '/root/zwei', '/root']

    Doppelte Werte werden ausgefiltert:

    >>> roots_list.append('/root/eins/')
    >>> roots_list
    ['/root/eins', '/root/zwei', '/root', '/root/eins/']
    >>> rebased_sourcelist(roots_list, '/root')
    ['eins', 'zwei']

    Wenn fremde Pfade enthalten sind, tritt ein Fehler auf:

    >>> roots_list.append('/anderswo')
    >>> rebased_sourcelist(roots_list, '/root')
    Traceback (most recent call last):
        ...
    ValueError: '/anderswo' is not located below '/root'!

    """
    assert not (as_string and as_list), \
            ('Only one result type of string (%r) or list (%r) '
             ' can be enforced!'
             ) % (as_string, as_list)
    if isinstance(raw, (list, tuple)):
        joiner = '\n' if as_string else None
    else:
        raw = raw and raw.splitlines() or []
        joiner = None if as_list else '\n'
    res = []
    func = make_childonly_filter(root,
                                 current='' if allow_empty
                                            else None)
    for p in raw:
        val = func(p)
        if val is None or val in res:
            continue
        if not val and not allow_empty:
            continue
        res.append(val)
    if not res and not allow_empty:
        raise ValueError('Empty list is not allowed!')
    if joiner is None:
        return res
    return joiner.join(res)


def checked_sourcelist(raw, root, allow_empty=False,
                       allow_root=False,
                       as_string=None, as_list=None):
    r"""
    Wie --> rebased_sourcelist(), aber unter Erhaltung der absoluten
    root-Angabe.

    >>> roots_list = ['eins', 'zwei']
    >>> checked_sourcelist(roots_list, '/root')
    ['/root/eins', '/root/zwei']

    Wenn ein String übergeben wird, kommt das Ergebnis als String zurück:

    >>> checked_sourcelist('\n'.join(roots_list), '/root')
    '/root/eins\n/root/zwei'

    Die Rückgabe als String ("Zeilen", ohne abschließendes '\n')
    kann auch unabhängig vom Eingabetyp erzwungen werden:

    >>> checked_sourcelist(roots_list, '/root', as_string=True)
    '/root/eins\n/root/zwei'

    Wenn die Wurzel direkt enthalten ist, wird diese Angabe mit
    allow_root=False (Vorgabe) ausgefiltert:

    >>> roots_list.append('/root')
    >>> roots_list
    ['eins', 'zwei', '/root']
    >>> checked_sourcelist(roots_list, '/root')
    ['/root/eins', '/root/zwei']

    Die Eingabeliste wird dabei nicht verändert:

    >>> roots_list
    ['eins', 'zwei', '/root']

    Doppelte Werte werden ausgefiltert:

    >>> roots_list.append('/root/eins')
    >>> roots_list
    ['eins', 'zwei', '/root', '/root/eins']
    >>> checked_sourcelist(roots_list, '/root')
    ['/root/eins', '/root/zwei']

    (Eine Normalisierung bzgl. angehängter /-Zeichen findet dabei derzeit nicht
    statt)

    Wenn fremde Pfade enthalten sind, werden diese als unter root liegend
    angenommen:

    >>> roots_list.append('/anderswo')
    >>> checked_sourcelist(roots_list, '/root')
    ['/root/eins', '/root/zwei', '/root/anderswo']

    Traceback (most recent call last):
        ...
    ValueError: '/anderswo' is not located below '/root'!

    """
    assert not (as_string and as_list), \
            ('Only one result type of string (%r) or list (%r) '
             ' can be enforced!'
             ) % (as_string, as_list)
    if isinstance(raw, (list, tuple)):
        joiner = '\n' if as_string else None
    else:
        raw = raw and raw.splitlines() or []
        joiner = None if as_list else '\n'
    res = []
    if not root.startswith('/') or not root.strip('/'):
        raise ValueError('Bogus root (%(root)r)' % locals())
    root = root.rstrip('/')
    func = make_prefixer(root)
    for p in raw:
        val = func(p)
        if val is None or val in res:
            continue
        if not val and not allow_empty:
            continue
        if val == root and not allow_root:
            continue
        res.append(val)
    if not res and not allow_empty:
        raise ValueError('Empty list is not allowed!')
    if joiner is None:
        return res
    return joiner.join(res)


def wrapped_tarball(export_context, context):
    """
    Gib ein Tarball als Ergebnis des transmogrifier-Aufrufs zurück
    """
    result = _export_result_dict(export_context)
    RESPONSE = context.REQUEST.RESPONSE
    RESPONSE.setHeader('Content-type', 'application/x-gzip')
    RESPONSE.setHeader('Content-disposition',
                       'attachment; filename=%s' % result['filename'])
    return result['tarball']


def _export_result_dict(context, steps=None, messages=None):
    """
    Wie von Products.GenericSetup.SetupTool._doRunExportSteps zurückgegeben

    context -- ein *Export-Kontext*!

    (Helferlein für --> wrapped_tarball
    """
    return {'steps': steps,
            'messages': messages,
            'tarball': context.getArchive(),
            'filename': context.getArchiveFilename()}


def all_uids(elem, unescape=None):
    """
    Generiere alle UIDs aus einem XML-Element, wie es vom Marshaller erzeugt
    wird.
    """
    s = elem.string
    if not s:
        return
    if elem['mimetype'] == 'text/html':
        if unescape is None:
            unescape = HTMLParser.HTMLParser().unescape
        html = unescape(s)
        soup = BeautifulSoup(html)
        for uid in extract_uids(soup):
            if not is_uid_shaped(uid):
                print 'Keine UID:', uid
            yield uid
    elif is_uid_shaped(s):
        yield uid


def make_dirProxy(context, foldertype='Folder'):
    """
    Gib ein Proxy-Dictionary zurück, das existierende Folder-Objekte verwaltet.
    Sofern ein Objekt noch nicht existiert, wird es angelegt.
    """

    dic = None
    def create_directory(relpath):
        relpath_n = normpath_posix(relpath)
        if relpath_n in ('', '.'):
            return context
        subdir, name = split_posix(relpath_n)
        o = getattr(dic[subdir], name, None)
        if o is None:
            dic[subdir].manage_addFolder(name)
            o = getattr(dic[subdir], name)
        return o

    dic = Proxy(create_directory)
    dic[''] = dic['.'] = context

    return dic


def make_readableNameFactory(context, passthrough=None, single=True):
    """
    Gib eine Factory-Funktion zurück, die einen Dateinamen zurückgibt, unter
    dem die übergebene Datei lesbar ist.

    context -- ein Importkontext

    passthrough -- logischer Wert: Wenn ein DirectoryImportContext übergeben
                   wurde, können die übergebenen Dateinamen jeweils direkt
                   verwendet werden; ansonsten (z. B. TarballImportContext)
                   muß jeweils eine temporäre Datei erzeugt werden, die z. B.
                   der Methode _importObjectFromFile übergeben werden kann

    single -- logischer Wert: Wenn True, wird dieselbe temporäre Datei immer
              wieder verwendet (sodaß am Ende nur eine Datei gelöscht werden
              muß)
    """

    if passthrough is None:
        passthrough = isinstance(context, DirectoryImportContext)

    if passthrough:
        base = context._profile_path

        def getfile_absname(path):
            return normpath(join(base, path))

        return getfile_absname

    vars_ = {'tmpname': None}

    def gettemp_single(path):
        data = context.readDataFile(path)
        if vars_['tmpname'] is None:
            tmpfile, tmpname = mkstemp()
            tmpfile.write(data)
            tmpfile.close()
            vars_['tmpname'] = tmpname
        else:
            tmpname = vars_['tmpname']
            with open(tmpname, 'wb') as tmpfile:
                tmpfile.write(data)
        return tmpname

    def gettemp_multi(path):
        data = context.readDataFile(path)
        tmpfile, tmpname = mkstemp()
        tmpfile.write(data)
        tmpfile.close()
        return tmpname

    if single:
        return gettemp_single
    return gettemp_multi


def make_pathFilter(seq, sep='/', np=normpath_posix,
                    skip_leading=None):
    """
    Erzeuge eine Filterfunktion für Pfadangaben

    >>> whitelist = ['knowhow/*/*', 'akademie/*/*']
    >>> f = make_pathFilter(whitelist)
    >>> f('knowhow/fachbuecher/')
    False
    >>> f('knowhow/fachbuecher/ein-fachbuch')
    True
    >>> f('knowhow/fachbuecher/ein-fachbuch/ein-kapitel')
    False
    >>> f2 = make_pathFilter(whitelist, skip_leading=('unitracc', 'gkz'))
    >>> f('unitracc/knowhow/fachbuecher/ein-fachbuch')
    False
    >>> f2('unitracc/knowhow/fachbuecher/ein-fachbuch')
    True
    >>> f2('knowhow/fachbuecher/ein-fachbuch')
    True
    """
    if not seq:
        return lambda x: False
    MAIN = []
    for entry in seq:
        MAIN.append(np(entry).split(sep))

    def path_matches(p):
        pa = np(p)
        pal = pa.split(sep)
        if skip_leading is not None:
            if pal[0] in skip_leading:
                del pal[0]

        for wle in MAIN:
            if _path_matches(pal, wle):
                return True
        return False

    def _path_matches(val, ref):
        i = 0
        has_val = True
        has_ref = True
        while True:
            try:
                val_token = val[i]
            except IndexError:
                has_val = False
            try:
                ref_token = ref[i]
            except IndexError:
                has_ref = False
            if not has_val:
                return not has_ref
            elif not has_ref:
                return False
            i += 1
            if ref_token == '*':
                continue
            elif ref_token != val_token:
                return False

    return path_matches


def make_countdown_function(initial, **kwargs):
    """
    Gib ein Funktionsobjekt zurück, das keinmal, einmal oder n-mal
    True und dann False zurückgibt

    >>> f = make_countdown_function(True)
    >>> f()
    True
    >>> f()
    False
    >>> f()
    False

    Wenn der Initialwert False ist, kommt immer False zurück:
    >>> f = make_countdown_function(False)
    >>> f()
    False
    >>> f()
    False

    >>> f = make_countdown_function(2)
    >>> f()
    True
    >>> f()
    True
    >>> f()
    False
    """
    assert isinstance(initial, int)
    allow_neg = kwargs.pop('allow_neg', False)
    if not allow_neg:
        assert initial >= 0
    def gimme_false():
        return False

    if not initial:
        return gimme_false

    liz = [initial]

    def countdown():
        val = liz[0]
        if val:
            liz[0] = val - 1
            return True
        return False

    return countdown


def log_module(logger, e):
    """
    Modulinformation für übergebenes Objekt (meist eine Exception) protokollieren
    """
    try:
        mod = e.__module__
    except AttributeError:
        pass
    else:
        logger.info('Modul: %(mod)s', locals())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
