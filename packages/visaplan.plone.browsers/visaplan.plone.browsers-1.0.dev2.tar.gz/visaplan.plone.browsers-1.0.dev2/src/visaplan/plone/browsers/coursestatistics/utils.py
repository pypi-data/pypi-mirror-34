# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""
utils-Modul für Browser coursestatistics
"""

def get_uid_and_info__factory(context):
    # evtl. reicht auch das Brain ... 
    author = context.getBrowser('author')
    getByUserId = author.getByUserId

    def get_uid_and_info(row):
        user_id = row['id']
        user = getByUserId(user_id)
        if user is None:
            return None, None
        uid = user.UID()
        return uid, {'member_id': user_id,
                     'member_title': row['title'],
                     }
    return get_uid_and_info

def void_uid_info(uid):
    return {'member_id': uid,
            'member_title': 'dangling profile %(uid)s' % locals(),
            }

if __name__ == '__main__':
    import doctest
    doctest.testmod()

