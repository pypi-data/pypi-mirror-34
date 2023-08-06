from os import unlink
import os
import glob

def delete(self,event):
    """ """
    context=event.object
    storagepath=context.getBrowser('scaling')._storage_path()

    if hasattr(context,'UID') and context.UID():
        for path in glob.glob(storagepath+context.UID()+'*'):
            if os.path.exists(path):
                unlink(path)