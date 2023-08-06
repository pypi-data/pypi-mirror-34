from dayta.browser.public import implements, Interface
from tomcom.tcconvert.browser import cET
from tomcom.tcconvert.browser import Browser as BrowserView

from App.Common import rfc1123_date
from ZPublisher.Iterators import filestream_iterator
from OFS.Image import File

from visaplan.plone.tools.log import getLogSupport
logger, debug_active, DEBUG = getLogSupport(fn=__file__)


class IUnitraccVideo(Interface):

    def get_streaming_info(self):
        """ """

    def stream(self):
        """ """

    def update_ogg(self):
        """ """


class Browser(BrowserView):

    implements(IUnitraccVideo)

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
        request = context.REQUEST
        form = request.form
        field_name = form.get('field_name')
        logger.info('stream(%(context)r, field_name=%(field_name)r', locals())
        field = context.getField(field_name)
        file = field.get(context)
        return file.index_html(request, request.RESPONSE)

    def update_ogg(self):
        """ """
        context = self.context

        context.getBrowser('tpcheck').auth_modify_portal_content()

        context.setOgg(None)

        self.send()

        message = context.getAdapter('message')
        message('Changes saved.')

        return context.REQUEST.RESPONSE.redirect(context.absolute_url() + '/view')
