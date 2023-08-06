# -*- coding: utf-8 -*- äöü
from os import popen,rename,sep,unlink
from App.config import getConfiguration

from os import unlink
import os
import glob

def convert(self,event):
    """ """
    context=event.object

    # FIXME: Default-Wert {} hat keinen Schlüssel 'active' ...
    if getConfiguration().product_config.get('flv', {})['active']=='True':
        if context.getContentType().startswith('video/') and not context.getContentType().endswith('flv'):
            context.getBrowser('flashfile')._convert()

def delete(self,event):
    """ """
    context=event.object
    storagepath=context.getBrowser('scaling')._storage_path()

    if hasattr(context,'UID'):
        for path in glob.glob(storagepath+context.UID()+'*'):
            if os.path.exists(path):
                unlink(path)
