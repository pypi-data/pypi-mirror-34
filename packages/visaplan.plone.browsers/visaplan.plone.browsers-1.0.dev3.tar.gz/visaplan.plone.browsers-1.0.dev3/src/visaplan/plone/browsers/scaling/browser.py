# -*- coding: utf-8 -*- äöü
from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
from os.path import exists, getsize, getmtime
from os import sep, unlink
from time import gmtime
from traceback import format_stack
from collections import defaultdict

# Plone-Module:
import PIL.Image
from DateTime import DateTime
from App.Common import rfc1123_date
from ZPublisher.Iterators import filestream_iterator
from App.config import getConfiguration

# Unitracc-Tools:
from visaplan.plone.tools.log import getLogSupport

# Logging und Debugging:
LOGGER, debug_active, DEBUG = getLogSupport('scaling')
# from pdb import set_trace

SCALING_STORAGE_KEY = 'CUSTOM_SCALINGS'
# vorläufig hartcodiert:
SCALING_WHITELIST = frozenset([
                     '%dx%d' % (n, n)
                     for n in (60, 90, 120, 180, 240, 560, 720)
                     ] + [  # alte Inhalte aus Unitracc 1:
                     '60x80',
                     '180x120',
                     '180x135',
                     '180x240',
                     '360x240',
                     '90x120',
                     ])
DEFAULT_SCALING = defaultdict(lambda: '120x120')


class IScaling(Interface):

    def get():
        """get a needed scaling"""

    def getAvaliable(self):
        """ """

    def set():
        """ """

    def getSize(scaling):
        """ """

    def createScalings():
        """ """

    def setImageConfig():
        """
        Speichere die Bilder-Settings (erlaubte Skalierungen)
        """

    def getScalingFormat():
        """ """


class Browser(BrowserView):

    implements(IScaling)

    cache_duration = 3600
    storageKey = 'scaling'

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)

    def _storage_path(self):
        """ """
        return getConfiguration().product_config.get('scaling', {})['scaling_dir'] + sep

    def getAvaliable(self):  # Elefant in Kairo: getAvailable
        """ """
        context = self.context.getAdapter('portal')()
        ann = context.getBrowser('annotation')
        return ann.get(SCALING_STORAGE_KEY, [])

    def getSize(self, scaling):
        """
        Gib die realen Abmessungen des Bildes zurueck,
        sofern <scaling> in der Positivliste ist

        scaling -- ein String, z.B. '180x180'
        """
        context = self.context
        portal = context.getAdapter('portal')()
        ann = portal.getBrowser('annotation')
        scalings = ann.get(SCALING_STORAGE_KEY, [])
        DEBUG('getSize(%(scaling)r): scalings = %(scalings)s', locals())

        if scaling not in scalings:
            return {'width': 0,
                    'height': 0}

        pickle = context.getBrowser('pickle')
        dict_ = pickle.get('scaling_info', {})

        uid = context.UID()
        if not dict_.has_key(uid):
            self._scale(scaling)

        dict_ = pickle.get('scaling_info', {})

        return dict_[uid]

    def get(self):
        """
        HTTP-GET-Antwort für die Bild-Datei zur UID des Kontexts

        Wenn die Skalierung noch nicht vorhanden und auf Platte gespeichert
        ist, wird sie erzeugt.
        """
        context = self.context
        portal = context.getAdapter('portal')()
        request = context.REQUEST
        scaling = request.form.get('scaling')
        if not scaling:
            referer = request.get('HTTP_REFERER')
            LOGGER.error('%(context)r: kein Scaling angegeben (Referer: %(referer)r)', locals())
            pt = context.portal_type
            scaling = DEFAULT_SCALING[pt]
            if not scaling:
                return

        uid = context.UID()
        if not scaling or not uid:
            LOGGER.error('%(context)r.get(): uid (%(uid)r) und/oder scaling %(scaling)r leer!', locals())
            liz = format_stack()  # Fehler gefunden; Traceback ermitteln
            liz.insert(0, '[ @@scaling.get TraceBack ... [\n')
            liz.append('] ... @@scaling.get TraceBack ]')
            LOGGER.error(''.join(liz))
        filename_stem = self._storage_path() + uid + '_'
        # XXX Fehler, wenn scaling is None; Vorgehen? (Fehler, etc.)
        fullScalingPath = filename_stem + scaling
        if not exists(fullScalingPath):
            DEBUG('get(uid=%(uid)r, scaling=%(scaling)r):', locals())
            DEBUG('/resolveuid/%(uid)s/@@scaling/get?scaling=%(scaling)s', locals())
            fullOrigPath = filename_stem + 'image'
            if exists(fullOrigPath):
                DEBUG('--> _scale(...)')
                self._scale(scaling)
            else:
                if scaling not in SCALING_WHITELIST:
                    LOGGER.error('%(context)r: Unzulaessige Skalierung (%(scaling)r)', locals())
                    return
                width, height = map(int, scaling.split('x'))

                field = context.getField('image')
                if not field:
                    DEBUG('Keine <image>-Daten fuer %(context)r (1)', locals())
                    return ''
                data = str(field.get(context))

                if not data:
                    DEBUG('<image>-Daten fuer %(context)r sind leer (2)', locals())
                    return ''

                try:
                    io = field.scale(data=data, w=width, h=height)[0]
                except IOError as e:
                    LOGGER.error('%(context)r: konnte %(field)r nicht skalieren (%(scaling)r)', locals())
                    LOGGER.exception(e)
                    return
                else:
                    data = io.read()
                    with open(fullScalingPath, 'wb') as nif:
                        nif.write(data)
                        DEBUG('%(fullScalingPath)s geschrieben', locals())

        response = context.REQUEST.RESPONSE
        setHeader = response.setHeader
        modified = DateTime('%s/%s/%s/ %s:%s'
                            % gmtime(getmtime(fullScalingPath))[:5])
        setHeader('Last-Modified', (modified).toZone('GMT').rfc822().split('+')[0] + 'GMT')
        setHeader('Expires', rfc1123_date((DateTime() + self.cache_duration).timeTime()))
        setHeader('Cache-Control', 'max-age=%d' % int(self.cache_duration * 24))
        setHeader('Accept-Ranges', 'bytes')
        setHeader('Content-Type', 'image/jpeg')
        setHeader('Content-Length', getsize(fullScalingPath))
        setHeader('Content-Disposition',
                  'inline; filename="%s.jpg"' % context.getId())
        return filestream_iterator(fullScalingPath, mode='rb')

    def set(self):
        """ """
        context = self.context

        context.getBrowser('tpcheck').auth_manage_portal()

        form = context.REQUEST.form
        portal = context.getAdapter('portal')()
        ann = portal.getBrowser('annotation')
        scalings = form.get('scalings')
        scalings = scalings.split('\n')
        scalings = [scaling.strip()
                    for scaling in scalings
                    if scaling.strip()
                    ]

        ann.set(SCALING_STORAGE_KEY, scalings)
        message = context.getAdapter('message')
        message('Changes saved.')
        context.REQUEST.RESPONSE.redirect(context.absolute_url() + '/manage_scalings')

    def _scale(self, scaling):
        """
        Erzeuge und speichere ein Thumbnail-Bild
        """
        context = self.context

        splittedScaling = scaling.split('x')
        w = int(splittedScaling[0])
        h = int(splittedScaling[1])

        storagepath = self._storage_path()
        uid = context.UID()
        fullScalingPath = storagepath + uid + '_' + scaling
        fullOrigPath = storagepath + uid + '_image'
        # set_trace()

        field = context.getField('image')
        # FIXME: Daten werden per plone.app.blob verwaltet;
        #        über entsprechende Funktionalität beschaffen!
        data = open(fullOrigPath, 'rb').read()
        io = field.scale(data=data, w=w, h=h, instance=context)[0]
        scaledData = io.read()
        io.seek(0)
        image = PIL.Image.open(io)
        width, height = image.size[:2]
        pickle = context.getBrowser('pickle')
        dict_ = pickle.get('scaling_info', {})
        dict_[uid] = {'width': width,
                      'height': height,
                      }
        # dict_[context.UID()] = {'width': image.size[0],
        #                         'height': image.size[1]}
        pickle.set('scaling_info', dict_)

        open(fullScalingPath, 'wb').write(scaledData)

    def createScalings(self):
        """ """
        context = self.context
        context.getAdapter('authorized')('Manage portal')
        pc = context.getAdapter('pc')()._catalog

        form = context.REQUEST.form

        scalings = self.getAvaliable()

        query = {}
        query['portal_type'] = 'Image'
        query['path'] = context.getPath()

        for brain in pc(query):
            object_ = brain.getObject()
            for scaling in scalings:
                form.update({'scaling': scaling})
                object_.getBrowser('scaling').get()

    def setImageConfig(self):
        """
        Speichere die Bilder-Settings (erlaubte Skalierungen)
        """
        context = self.context

        context.getBrowser('authorized').managePortal()

        form = dict(context.REQUEST.form)
        message = context.getAdapter('message')
        pickle = context.getBrowser('pickle')
        dict_ = pickle.get(self.storageKey, {})

        dict_[context.UID()] = form

        pickle.set(self.storageKey, dict_)

        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])

    def getScalingFormat(self):
        """ """
        context = self.context

        pickle = context.getBrowser('pickle')
        dict_ = pickle.get(self.storageKey, {})

        return dict_.get(context.UID(), {}).get('format', 'JPEG')
