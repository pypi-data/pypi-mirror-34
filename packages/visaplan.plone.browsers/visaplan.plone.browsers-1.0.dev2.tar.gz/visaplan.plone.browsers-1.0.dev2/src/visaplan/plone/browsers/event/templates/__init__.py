# -*- coding: utf-8 -*- äöü
from os.path import join, isdir
from os import listdir

BASE = """<configure
    xmlns="http://namespaces.zope.org/zope"
    xmlns:browser="http://namespaces.zope.org/browser">
    %s
</configure>
"""

PAGE = """
    <browser:page
             for="*"
             name="%(name)s"
             template="%(template)s"
             permission="zope2.View"
             />
"""

DENIED = ['__init__.py', 'configure.zcml', '.svn']
BASE_PATH = __path__[0]


def skip(fn):
    global DENIED, BASE_PATH
    if fn in DENIED:
        return 1
    elif fn.startswith('.'):
        return 1
    elif fn.endswith('.pyc'):
        return 1
    elif fn.endswith('~'):
        return 1
    elif isdir(join(BASE_PATH, fn)):
        return 1
    else:
        return 0

BASE_PATH = __path__[0]


def generate(basedir):
    for fn in sorted(listdir(basedir)):
        if skip(fn):
            continue
        dic = {'template': fn}
        if fn.endswith('.xml.pt'):
            dic['name'] = fn[:-7]
        elif fn.endswith('.pt'):
            dic['name'] = fn[:-3]
        else:
            print 'SKIPPING: %s' % join(basedir, fn)
            continue
        yield dic


def aliasdict(name):
    return {'name': 'my-%(name)s' % locals(),
            'template': 'our-%(name)s.pt' % locals(),
            }

ZCML_NAME = join(BASE_PATH, 'configure.zcml')
# Nicht routinemäßig generieren, da kleine manuelle Änderungen;
# bei Bedarf neu generieren und Änderungen sichten (tsvn diff)!
if 1:
    tmpls = []
    for dict_ in generate(BASE_PATH):
        tmpls.append(PAGE % dict_)
    for addi in ('calendar',
                 ):
        tmpls.append(PAGE % aliasdict(addi))

    fp = open(ZCML_NAME, 'w')
    fp.write(BASE % ''.join(tmpls))
    fp.close()
else:
    print 'SKIPPED generation of', ZCML_NAME
