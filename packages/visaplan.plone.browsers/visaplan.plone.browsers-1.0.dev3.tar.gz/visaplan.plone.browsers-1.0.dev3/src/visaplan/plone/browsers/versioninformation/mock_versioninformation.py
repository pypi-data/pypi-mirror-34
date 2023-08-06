# -*- coding: utf-8 -*- äöü
"""
Abgespeckte Kopie von ./browser.py, nur für Testzwecke (Doctests)
"""
VERSION = '.'.join(map(str, [
                       2,   # Plone
                       2,   # Plone 4 / Buildout-Setup
                       27,  # PDF-Export: Sachindex (aus Glossarbegriffen)
                       ]))


static_info = {
        # Slicing:
        # 3 für '$: '; 11 für 'LastChanged'; letzter Summand für das Wort
        'LastChangedRevision': '$LastChangedRevision: 17260 $'[3+11+8:-2],
        'Revision':            '$Revision: 17260 $'[3+0+8:-2],
        'LastChangedDate':     '$LastChangedDate: 2016-11-10 18:28:00 +0100 (Do, 10. Nov 2016) $'[3+11+4:-2],
        'LastChangedBy':       '$LastChangedBy: tobias $'[3+11+2:-2],
        'HeadURL':             '$HeadURL: svn+ssh://svn.visaplan.com/unitracc/products/visaplan.plone.browsers/branches/v1_0/src/visaplan/plone/browsers/versioninformation/mock_versioninformation.py $'[3+4+3:-2],
    }


def branch_or_tag(url, cut=0):
    """
    extrahiere den Namen von Zweig (Branch) oder Tag aus einer URL

    url -- die vollständige URL
    cut -- Anzahl zu entfernender Pfadelemente, abhängig von der (fixen)
           relativen Position im Verzeichnisbaum  (und *nur* zu ändern,
           wenn diese Datei im Projekt verschoben oder kopiert wird)
    """
    _spliturl = url.split('/')
    namepos = -(cut + 1)
    botpos = namepos - 1
    bot = _spliturl[botpos]
    dic = {'svn_branch': None,
           'svn_tag':    None,
           }
    try:
        if bot == 'branches':
            dic['svn_branch'] = _spliturl[namepos]
        elif bot == 'tags':
            dic['svn_tag'] = _spliturl[namepos]
        else:
            assert _spliturl[namepos] == 'trunk', \
                    'Element %d of URL %s expected to be "trunk" (is %r)' % (
                            namepos, url, _spliturl[namepos],
                            )
    finally:
        return dic

static_info.update(branch_or_tag(static_info['HeadURL'],
                                 5))

if __name__ == '__main__':
    from pprint import pprint
    pprint(static_info)
# vim: ts=8 sts=4 sw=4 si et
