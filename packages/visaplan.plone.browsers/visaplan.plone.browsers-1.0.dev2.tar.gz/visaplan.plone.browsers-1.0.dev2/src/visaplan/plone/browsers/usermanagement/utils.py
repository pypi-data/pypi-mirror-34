# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
unitracc@@usermanagement.utils
"""


from ...tools.attools import getter_tuple

NAME_FIELDS = ('academicTitle',
               'firstname', 'lastname',
               )

def profileInfoDict(o):
    """
    Gib ein Dict zurück
    """
    res = {'userId': o.getUserId(),
           }
    for (aname, getter_name) in map(getter_tuple,
            ('academicTitle', 'firstname', 'lastname', 'email',
                )):
        getter = getattr(o, getter_name)
        val = getter()
        if val:
            val = val.strip()
        res[aname] = val or None
    return res


def oneliner(dic):
    res = [dic['userId']]
    names = []
    for a in NAME_FIELDS:
        val = dic[a]
        if val:
            names.append(val)
    Name = ' '.join(names)
    EMail = dic['email']
    if Name or EMail:
        res.append(' (')
        if Name:
            res.append(Name)
            if EMail:
                res.append(', ')
        if EMail:
            res.extend(['Mail: ', EMail])
        res.append(')')
    return ''.join(res)


def make_condensed(**kwargs):
    if 'admin_id' not in kwargs:
        if 'auth' not in kwargs:
            if 'getBrowser' not in kwargs:
                if 'context' not in kwargs:
                    raise TypeError('Information missing!')
                context = kwargs.pop('context')
                getBrowser = context.getBrowser
            else:
                getBrowser = kwargs.pop('getBrowser')
            auth = getBrowser('auth')
        else:
            auth = kwargs.pop('auth')
        admin_id, admin_name = (auth.getId(), auth.getFullname())
        if admin_name:
            admin_info = '%s (%s)' % (admin_id, admin_name)
        else:
            admin_info = admin_id
    else:
        admin_info = kwargs.pop('admin_id')

    def condensed(dic, **kwargs):
        """
        Dict für die Protokollierung:
        Fasse die Namensinformationen zusammen
        und ergänze Informationen über den Administrator
        """
        res = {'by': admin_info,
               }
        names = []
        # academicTitle < firstname < lastname ;-) 
        for key in sorted(dic.keys()):
            val = dic[key]
            if val is None:
                continue
            if key in NAME_FIELDS:
                names.append(val)
                continue
            res[key] = val
        if names:
            res['Name'] = ' '.join(names)
        res.update(kwargs)
        return res

    return condensed


def profileInfo(o):
    """
    Gib die Benutzer-ID und die Namensinformationen zum übergebenen
    Profilobjekt zurück
    """
    theid = o.getUserId()
    names = []
    for aname in ('academicTitle', 'firstname', 'lastname',
            ):
        getter_name = 'get'+(aname[0].upper())+aname[1:]
        val = getattr(o, getter_name)()
        if val:
            names.append(val)
    if names:
        return '%s (%s)' % (
                theid,
                ' '.join(names),
                )
    else:
        return theid


def profileBrainInfo(b):
    """
    Gib die Profil-ID und die Namensinformationen zum übergebenen
    Benutzerkatalogobjekt zurück
    """
    theid = b.getId
    names = []
    for aname in ('academicTitle', 'firstname', 'lastname',
            ):
        getter_name = 'get'+(aname[0].upper())+aname[1:]
        val = getattr(b, getter_name)
        if val:
            names.append(val)
    if names:
        return '%s (%s)' % (
                theid,
                ' '.join(names),
                )
    else:
        return theid
