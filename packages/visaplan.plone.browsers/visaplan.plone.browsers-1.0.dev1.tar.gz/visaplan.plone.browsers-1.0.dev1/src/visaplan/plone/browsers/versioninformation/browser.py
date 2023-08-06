# -*- coding: utf-8 -*- äöü
# Plone/Zope/Dayta:
from dayta.browser.public import BrowserView, implements, Interface
from plone.memoize import ram
from Globals import DevelopmentMode

# Standardmodule:
import sys
from os.path import exists, join, basename, dirname
from os import popen
import re
from hashlib import md5
from time import time

# Unitracc-Tools:
from ...config import PRODUCT_HOME
from visaplan.tools.minifuncs import makeBool
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
logger, debug_active, DEBUG = getLogSupport(fn=__file__)

VERSION = '.'.join(map(str, [
                       2,   # Plone
                       3,   # visaplan.{UnitraccCustom,AQWA}
                       2,   # Überarbeitung des Buchungssystems
                       5,   # Fehlerbehebungen für Suche
                       ]))
# gf: ../../version.txt


def maintain_version_file():
    global PRODUCT_HOME, VERSION
    vfname = join(PRODUCT_HOME, 'version.txt')
    vf = None
    rewrite = 1
    try:
        if exists(vfname):
            vf = open(vfname, 'r')
            found_version = vf.read().rstrip()
            vf.close()
            if found_version == VERSION:
                logger.debug('%s contains correct version %s'
                             % (vfname, VERSION))
                rewrite = 0
            else:
                logger.info('found old version %s in %s'
                            % (found_version, vfname))
        if rewrite:
            vf = open(vfname, 'w')
            vf.write(VERSION + '\n')
            vf.close()
            logger.info('%s updated' % vfname)
    except Exception, e:
        logger.exception(e)
        logger.error('error maintaining %s' % vfname)

maintain_version_file()

static_info = {
        # Slicing:
        # 3 für '$: '; 11 für 'LastChanged'; letzter Summand für das Wort
        'LastChangedRevision': '$LastChangedRevision: 22300 $'[3+11+8:-2],
        'Revision':            '$Revision: 22300 $'[3+0+8:-2],
        'LastChangedDate':     '$LastChangedDate: 2018-08-10 16:06:41 +0200 (Fr, 10. Aug 2018) $'[3+11+4:-2],
        'LastChangedBy':       '$LastChangedBy: tobias $'[3+11+2:-2],
        'HeadURL':             '$HeadURL: svn+ssh://svn.visaplan.com/unitracc/products/visaplan.plone.browsers/branches/v1_0/src/visaplan/plone/browsers/versioninformation/browser.py $'[3+4+3:-2],
    }


def branch_or_tag(url, cut=0):
    u"""
    extrahiere den Namen von Zweig (Branch) oder Tag aus einer URL

    url -- die vollständige URL
    cut -- Anzahl zu entfernender Pfadelemente, abhängig von der (fixen)
           relativen Position im Verzeichnisbaum  (und *nur* zu ändern,
           wenn diese Datei im Projekt verschoben oder kopiert wird)
    """
    _spliturl = url.split('/')
    namepos = -(cut + 1)
    botpos = namepos - 1
    bot = _spliturl[botpos]
    dic = {'svn_branch': None,
           'svn_tag':    None,
           }
    try:
        if bot == 'branches':
            dic['svn_branch'] = _spliturl[namepos]
        elif bot == 'tags':
            dic['svn_tag'] = _spliturl[namepos]
        else:
            assert _spliturl[namepos] == 'trunk', \
                    'Element %d of URL %s expected to be "trunk" (is %r)' % (
                            namepos, url, _spliturl[namepos],
                            )
    finally:
        return dic

static_info.update(branch_or_tag(static_info['HeadURL'],
                                 5))


# Wenn das Modul neu geladen wird (nur möglich im Entwicklungsmodus),
# wird die Datei neu eingelesen, und der Hash wird neu berechnet;
# dann werden auch die Informationen neu ermittelt
def new_hash():
    val = md5(open(__file__, 'r').read())
    val.update(str(time()))
    return val.hexdigest()

MYHASH = new_hash()
def cache_key(self, method):
    return MYHASH


class IVersionInformation(Interface):

    def get(self):
        """
        Ermittle die Versionsinformationen und gib ein dict zurueck.
        Request-Variablen (jeweils 0 [default] oder 1):

        svn-info -- rufe "svn info" auf. Schlaegt manchmal fehl; liefert dafuer
                    aber Informationen ueber das Produkt, nicht diese Datei
        all -- vom Seitentemplate ausgewertet: gib mehr Informationen aus,
               z. B. ueber einen nicht aktiven Entwicklungsmodus
               (wenn aktiv, wird darueber *immer* informiert)
               oder den Python-Interpreter
        """

    def get_unitracc_version(self):
        """
        gib die Unitracc-Version zurueck wie in diesem Modul definiert
        """


class Browser(BrowserView):

    implements(IVersionInformation)

    def get(self):

        context = self.context
        context.getBrowser('authorized').managePortal()
        request = context.REQUEST
        meta = {'svn-info': False,
                'show_all': False,  # bool(DevelopmentMode),
                }
        for key in ('svn-info', 'show_all'):
            val = request.get(key, '')
            if val:
                try:
                    meta[key] = makeBool(val)
                except ValueError as e:
                    DEBUG('%(key)s = %(val)r --> %(e)r', locals())
        call_info = meta['svn-info']
        res = {'meta': meta,
               'info': (call_info
                        and self._get
                        or  self._miniget
                        )(),
               }
        return res

    @ram.cache(cache_key)
    def _get(self):
        """
        Subversion-Informationen werden durch Aufruf von 'svn info' beschafft.
        """
        global PRODUCT_HOME
        context = self.context

        pmu = context.portal_migration
        cp = context.Control_Panel

        dict_ = dict(static_info)

        fp = popen('svn info ' + PRODUCT_HOME)
        string_ = fp.read()
        fp.close()
        string_ = string_.replace('\n', '')

        dict_['zope'] = cp.version_txt()
        dict_['python'] = cp.sys_version()
        dict_['platform'] = cp.sys_platform()
        dict_['python_executable'] = sys.executable

        dict_['svn_url'] = re.findall('URL: (.+?)Basis', string_)[0]
        dict_['svn_version_number'] = re.findall('Revision: (.+?)Knotentyp', string_)[0]
        dict_['svn_modification_date'] = re.findall('erungsdatum: (.+?) \(', string_)[0]

        dict_['instance_version'] = pmu.getInstanceVersion()
        dict_['unitracc_version'] = pmu.getFileSystemVersion()
        dict_['unitracc_rootdir'] = PRODUCT_HOME
        dict_['debug_mode'] = bool(DevelopmentMode)
        dict_['portal_url'] = context.portal_url()

        return dict_

    svn_info = _get

    @ram.cache(cache_key)
    def _miniget(self):
        """
        Informationen ohne Aufruf von svn info, und moe. direkt von Python
        """
        global PRODUCT_HOME, VERSION
        context = self.context

        pmu = context.portal_migration
        cp = context.Control_Panel

        dict_ = dict(static_info)

        dict_['zope'] = cp.version_txt()
        dict_['python'] = sys.version
        dict_['platform'] = sys.platform
        dict_['python_executable'] = sys.executable

        dict_['instance_version'] = pmu.getInstanceVersion()
        dict_['unitracc_version'] = VERSION
        dict_['unitracc_rootdir'] = PRODUCT_HOME
        dict_['debug_mode'] = bool(DevelopmentMode)
        dict_['portal_url'] = context.portal_url()

        return dict_

    def get_unitracc_version(self):
        """
        gib die Unitracc-Version zurueck wie in diesem Modul definiert
        """
        global VERSION
        return VERSION

if 0:  # um die Versionsinformation "anzufassen", ein Bit kippen;
    # --> LastChangedRevision (Vim: * oder #):
    {'trunk': 1,
     # [ nur wnzkb ... [
     'wnzkb-trunk': 0,
     # ... prod:
     'wnzkb-prod': 1,
     # ] ... nur wnzkb ]
     'unitracc-prod': 1,
     'therp': 1,
     # [ nur gkz ... [
     'gkz-trunk': 1,
     # ... prod:
     'gkz-prod': 1,
     # ] ... nur gkz ]
     # [ staging ... [
     'staging': 0,
     # ] ... staging ]
     }

# $LastChangedRevision: 22300 $ vim: ts=8 sts=4 sw=4 si et
