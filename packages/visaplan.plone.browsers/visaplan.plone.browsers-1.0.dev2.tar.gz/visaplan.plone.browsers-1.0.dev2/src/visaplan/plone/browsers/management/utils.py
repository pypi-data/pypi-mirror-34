# -*- coding: utf-8 -*- äöü
# Standardmodule:
from json import dumps as json_dumps

# Plone:
from Products.CMFCore.utils import getToolByName

# Unitracc-Tools:
from ...tools.context import make_timeFormatter

def jsonify(context, brains, varname=None):
    """
    Gib die übergebene Sequenz im JSON-Format zurück;
    ermittle zu diesem Zweck Informationen, die ansonsten beim Rendern durch
    TAL beschafft würden (was aber - bei langen Listen - sehr (!) lang dauert)
    """
    res = []
    member = context.getBrowser('member')
    totime = context.getAdapter('totime')
    _ = context.getAdapter('translate')
    pm = getToolByName(context, 'portal_membership')
    ft = make_timeFormatter(context, True)

    getMember = pm.getMemberById
    for brain in brains:
        creator_id = brain.Creator
        creator_o = getMember(creator_id)
        creator_exists = creator_o is not None
        if creator_exists:
            creator_name = creator_o.getProperty('fullname', creator_id)
        else:
            creator_name = creator_id + ' (not found)'
        url = brain.getURL()
        dic = {'title': brain.Title,
               'view_url': url and (url+'/view'),
               'edit_url': url and (url+'/edit'),
               # 'creator_id': creator_id,
               'creator_name': creator_name,
               'modification_time': ft(brain.modified),
               'portal_type': _(brain.portal_type),
               }
        res.append(dic)
    if varname:
        return '\n%s = %s;' % (varname, json_dumps(res))
    return json_dumps(res)
