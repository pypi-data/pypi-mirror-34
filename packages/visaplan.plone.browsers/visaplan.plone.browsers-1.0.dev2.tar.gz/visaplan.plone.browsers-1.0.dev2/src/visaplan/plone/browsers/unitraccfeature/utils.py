# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79
u"""
utils-Modul für unitracc@@unitraccfeature
"""

# Systemmodule:
import sys
from os.path import join, isfile, isdir
from os import uname, getlogin, \
         getuid, geteuid, getpgrp, getegid

# Zope, Plone etc.:
import zope.component.hooks

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
LOGGER, debug_active, DEBUG = getLogSupport(fn=__file__)


# ------------------------------------------------------ [ Daten ... [
# -------------- [ UIDs (ggf. nach Projekt unterschiedlich) ... [
# XXX UIDs wieder gleichziehen! (Update-Schritt)
MYUNITRACC_UID = '31b9ab69eb35f706785632ff84c58241'
DESKTOP_UID = MYUNITRACC_UID
TEMP_UID = '063f1a7473c1fbd7e9e6942761f0b593'
REGISTRATION_UID = 'c27542ed513d0e6094bc2795087d8335'
HELP_UID = '133a0293a6556474debd6fd051239e47'
ABOUT_UID = '4f4780201a510b0491c4a6be41f9f418'
CONTACT_UID = '512c8c63d3214f365d78719906ef2f7c'
# beim Erzeugen einer Plone-Instanz erzeugte Objekte:
NEWSFOLDER_UID = '94f9c255900052d01fbe49883da17b5f'
ARTICLESFOLDER_UID = 'c5391cc6b3e35e6a4f6e42a746e381a2'
EVENTSFOLDER_UID = '21c53f55fa1b49a2085e1d5b483ab294'
# Ordner der Mitgliederliste (unitracc: /management/autoren):
MEMBERSFOLDER_UID = '5fe2a19cff91d9ed9595bfdc76887a78'
# Kurse:
COURSESFOLDER_UID = 'd01deba3238957e6e021ff2ca2d4f140'  # Unitracc
# Mediathek:
# Unitracc: 'e8dfc4253bc0ad402d48dc862d20821c'
MEDIATHEK_UID = 'e8dfc4253bc0ad402d48dc862d20821c'
# Akademie Kanalbau (GKZ): c5c80b6365a64a268f2f55cb39c39aa8
# AGBs:
AGB_UID = '7b807279090ab4af3043c47792fdcd2d'  # Unitracc
# -------------- ] ... UIDs (ggf. nach Projekt unterschiedlich) ]

THE_KEYS = ('rootfolder',     # unitracc, vdz
            'has_articles',   # True, False
            'has_booking',    # True, False
            'has_advertising',# True, False
            'has_courses',    # True, False
            'courses_uid',    # Container der Kurse
            'has_flexpaper',  # True, False
            'desktop_id',     # myunitracc
            'desktop_path',   # /myunitracc
            'ejournal_columns', # {'news': (...), 'articles': (...)}
            'board_guidelines',
            'bracket_default',
            'text_fig_dot',   # "Fig." oder auch "Image"
            'default_encoding',
            'os_hostname',    # z. B. unitracc1.vcl1.vdz.kunden.csl.de
                              #  oder unitracc2 (.tcis.de)
                              #  oder vbox-therp (.sbs-sup.local)
            'on_live_server'  # nach -> os_hostname
            'os_login_name',  # z. B. www-data
            'os_uid',         # eine Zahl, z. B. 1000
            'os_uid_effective', # eine Zahl, z. B. 1000; Unterschied?
            'os_gid',         # eine Zahl, z. B. 1000
            'os_gid_effective',
            )
# Hostnamen von Maschinen, für die die "produktiven Hostnamen"
# ordentlich eingetragen wurden (global gültige Nameserver-Einträge):
KNOWN_LIVE_HOSTNAMES = set(['unitracc1.vcl1.vdz.kunden.csl.de',
                            'unitracc.vcl1.vplan.kunden.csl.de',
                            'gkz.vcl1.vplan.kunden.csl.de',
                            ])
# ------------------------------------------------------ ] ... Daten ]


class FeaturesInfo(dict):
    """
    Klasse zur Ermittlung und Speicherung der Instanzinformationen
    """
    def __init__(self):
        dict.__init__(self)

    def __detect(self):
        """
        Ermittle die Eigenschaften, basierend auf der ID des Wurzelordners
        """
        site = zope.component.hooks.getSite()
        try:
            rootfolder = site.getId()
        except Exception, e:
            LOGGER.exception(e)
            rootfolder = 'unitracc'
            LOGGER.warn('Verwende Default %(rootfolder)r fuer rootfolder', locals())
        if debug_active:
            LOGGER.info('rootfolder: %r', rootfolder)
        self['rootfolder'] = rootfolder

        desktop_id = None
        try:
            query = {'UID': MYUNITRACC_UID,
                     }
            res = site.portal_catalog(query)
            for brain in res:
                desktop_id = brain.getId # bei Brain ohne Aufruf!
                break
        finally:
            if desktop_id is None:
                desktop_id = (rootfolder in ('unitracc',
                                             )
                              and 'myunitracc'
                              or  'schreibtisch')
            self['desktop_id'] = desktop_id
            if debug_active:
                LOGGER.info('desktop_id: %r', desktop_id)
            self['desktop_path'] = '/' + self['desktop_id']
        # Epilog:
        self['has_articles'] = rootfolder in ('unitracc', 'gkz')
        self['has_booking'] = rootfolder in ('unitracc', 'gkz')
        self['has_advertising'] = rootfolder in ('unitracc', 'gkz')
        self['has_courses'] = rootfolder in ('unitracc',
                                             'gkz',
                                             )
        self['courses_uid'] = (self['has_courses']
                               and COURSESFOLDER_UID
                               or  None)
        self['has_flexpaper'] = rootfolder == 'vdz'
        self['default_encoding'] = sys.getdefaultencoding()
        self['os_hostname'] = uname()[1]
        self['on_live_server'] = self['os_hostname'] in KNOWN_LIVE_HOSTNAMES
        try:
            self['os_login_name'] = getlogin()
        except OSError as e:
            LOGGER.error('getlogin: %s', e)
            LOGGER.exception(e)
            self['os_login_name'] = 'ERROR'
        try:
            self['os_uid'] = getuid()
        except OSError as e:
            LOGGER.error('getuid: %s', e)
            LOGGER.exception(e)
            self['os_uid'] = 'ERROR'
        try:
            self['os_uid_effective'] = geteuid()
        except OSError as e:
            LOGGER.error('geteuid: %s', e)
            LOGGER.exception(e)
            self['os_uid_effective'] = 'ERROR'
        try:
            self['os_gid'] = getpgrp()
        except OSError as e:
            LOGGER.error('getpgrp: %s', e)
            LOGGER.exception(e)
            self['os_gid'] = 'ERROR'
        try:
            self['os_gid_effective'] = getegid()
        except OSError as e:
            LOGGER.error('getegid: %s', e)
            LOGGER.exception(e)
            self['os_gid_effective'] = 'ERROR'
        if debug_active:
            LOGGER.info('has_booking: %(has_booking)r', self)
        if rootfolder in ('unitracc',
                          'gkz',
                          ):
            self['ejournal_columns'] = {'news':     (1, 2),
                                        'articles': (1, 2),
                                        }
            self['board_guidelines'] = '14a1f00a25d34182a66e1a5759cc8815'
            self['bracket_default'] = 'unitracc-breaket'
            self['text_fig_dot'] = _('Image')
        else:
            self['ejournal_columns'] = {'news':     (2, 3),
                                        'articles': (1, 2),
                                        }
            self['board_guidelines'] = 'bffbb384217442a887497e12b11f6c3b'
            self['bracket_default'] = 'no-breaket'
            self['text_fig_dot'] = _('Fig.')
        if debug_active:
            from pprint import pprint
            pprint(dict(self))

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            if key in THE_KEYS:
                self.__detect()
                return dict.__getitem__(self, key)
            raise

    def get(self, key, default=None):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            if key in THE_KEYS:
                self.__detect()
            return dict.get(self, key, default)


def sitecustomize_info():
    plen = len(sys.path)
    print '-' * 79
    env = sys.getdefaultencoding()
    print 'sys.path has %(plen)d entries;' % locals()
    print 'default encoding is %(env)r' % locals()
    for tup in zip(range(1, plen+1), sys.path):
        nr, dname = tup
        if isdir(dname):
            for fname in ('site.py', 'sitecustomize.py'):
                if isfile(join(dname, fname)):
                    print '%(nr)4d. %(dname)s/%(fname)s' % locals()
            spname = join(dname, 'site-packages', 'sitecustomize.py')
            if isfile(spname):
                print '%(nr)4d. %(spname)s' % locals()
        else:
            print  '?     %(dname)s is not a directory' % locals()
    print '-' * 79

