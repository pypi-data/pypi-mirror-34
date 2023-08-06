# -*- coding: utf-8 -*- äöü vim: sts=4 sw=4 si et
from tomcom.tcconvert.browser import *
from tomcom.tcconvert.browser import Browser as BrowserView
from dayta.browser.public import implements, Interface

from os.path import exists
from os import sep
from os.path import getmtime
from time import gmtime
from App.Common import rfc1123_date
from ZPublisher.Iterators import filestream_iterator
from os.path import getsize


class IUnitraccAudio(Interface):

    def get_streaming_info():
        """ """

    def stream():
        """ """

    def get_script_content(absurl, uid):
        """
        Gib Javascript-Code zurück
        """


class Browser(BrowserView):

    implements(IUnitraccAudio)

    cache_duration = 3600

    def _set_custom(self):
        """ """
        context = self.context
        root = self._get_root()

        field = context.getField('file')
        type_, subtype = field.getContentType(context).split('/')

        element = cET.Element('target_field')
        element.text = 'ogg'
        root.append(element)

        element = cET.Element('source_field')
        element.text = 'file'
        root.append(element)

        element = cET.Element('new_format')
        element.text = 'ogg'
        root.append(element)

        element = cET.Element('type')
        element.text = type_
        root.append(element)

        element = cET.Element('file_name')
        element.text = field.getFilename(context)
        root.append(element)

    def get_streaming_info(self):

        context = self.context
        list_ = []

        field = context.getField('file')
        dict_ = {}
        dict_['field_name'] = 'file'
        dict_['content_type'] = field.getContentType(context)
        list_.append(dict_)

        dict_ = {}
        dict_['field_name'] = 'ogg'
        dict_['content_type'] = 'application/ogg'
        list_.append(dict_)

        return list_

    def stream(self):
        """ """
        context = self.context
        form = context.REQUEST.form
        field_name = form.get('field_name')
        field = context.getField(field_name)
        file = field.get(context)
        return file.index_html(context.REQUEST, context.REQUEST.RESPONSE)

    def get_script_content(self, absurl, uid):
        """
        Gib Javascript-Code zurück
        """
        return """\
    if (document.createElement('audio').canPlayType) {
        if (!document.createElement('audio').canPlayType('audio/mpeg') &&
            !document.createElement('audio').canPlayType('audio/ogg')) {
                swfobject.embedSWF("player_mp3_mini.swf",
                     "player_fallback-%(uid)s", "200", "20", "9.0.0", "",
                     {"mp3":"%(absurl)s/@@unitraccaudio/stream?field_name=file"},
                     {"bgcolor":"#5C595A"}
                );
                swfobject.embedSWF("/player_mp3_mini.swf",
                     "custom_player_fallback-%(uid)s", "200", "20", "9.0.0", "",
                     {"mp3":"%(absurl)s/@@unitraccaudio/stream?field_name=file"},
                     {"bgcolor":"#5C595A"}
                );
        document.getElementById('audio_with_controls-%(uid)s').style.display = 'none';
        } else {
                // HTML5 audio + mp3 support
                //document.getElementById('player').style.display = 'block';
        }
    }
    """ % locals()
