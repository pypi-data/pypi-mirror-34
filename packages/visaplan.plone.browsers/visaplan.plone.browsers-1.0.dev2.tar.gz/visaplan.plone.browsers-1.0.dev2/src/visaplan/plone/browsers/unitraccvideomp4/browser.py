from tomcom.browser.public import *
from tomcom.tcconvert.browser import *
from tomcom.tcconvert.browser import Browser as BrowserView
import xml.etree.cElementTree  as cET

class IUnitraccVideoMP4(Interface):

    def update_field(self):
        """ """

class Browser(BrowserView):

    implements(IUnitraccVideoMP4)

    def update_field(self):
        """ """
        context=self.context

        context.getBrowser('tpcheck').auth_modify_portal_content()

        _=context.getAdapter('message')

        if context.getSource():
            context.setFile(None)
            context.setWidth(0)
            context.setHeight(0)

            self.send()

            _('Changes saved.')

        else:
            _('Source format does not exist.','error')

        return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])


    def _set_custom(self):
        """ """
        context=self.context
        root=self._get_root()

        element=cET.Element('target_field')
        element.text='file'
        root.append(element)

        element=cET.Element('source_field')
        element.text='source'
        root.append(element)

        element=cET.Element('new_format')
        element.text='mp4'
        root.append(element)

        element=cET.Element('type')
        element.text='video'
        root.append(element)

        element=cET.Element('file_name')
        element.text=context.getField('source').getFilename(context)
        root.append(element)