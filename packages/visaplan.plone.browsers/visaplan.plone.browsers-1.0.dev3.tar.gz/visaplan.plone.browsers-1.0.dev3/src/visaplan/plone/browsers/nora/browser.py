# -*- coding: utf-8 -*- äöü
# Plone/Zope/Dayta:
from dayta.browser.public import Interface, implements, BrowserView
from DateTime import DateTime
from zExceptions import NotFound

# Unitracc-Tools:
from ...tools.misc import columns as to_columns
from ...tools.forms import tryagain_url, merge_qvars
from visaplan.plone.tools.log import getLogSupport

# Andere Browser und Adapter:
from ...browser.article.utils import extract_1st_image_src

# Logging und Debugging:
LOGGER, debug_active, DEBUG = getLogSupport(fn=__file__)
from pprint import pformat
import pdb
from visaplan.tools.debug import pp


class INewsOrArticlesBrowser(Interface):

    def search():
        """
        Suche nach News und Artikeln (per Vorgabe: max. 12)
        """

    def search_all():
        """
        Suche alle News und Artikel
        """

    def search_a():
        """
        Für Entwicklungszwecke:
        Suche *nur* nach Artikeln (von denen es weniger gibt)
        """

    def getImageUrl(brain, scaling):
        """
        Gib die URL des Vorschaubilds für die Listenansicht zurück

        Prioritätenliste:
        1. das explizite Vorschaubild (wie -> getImage)
        2. die erste im Seitentext gefundene Bild-URL
        3. das Standard-Piktogramm für News (die Zeitung; wie -> getImage)
        """

    def getImage():
        """ """


class Browser(BrowserView):

    implements(INewsOrArticlesBrowser)

    def getImage(self, uid=''):
        """
        Gib Bilddaten zurück;
        zur Verwendung in URLs, auch für die Listenansicht, die
        üblicherweise durch getImageUrl erzeugt werden.

        Wenn kein explizites Vorschaubild vorhanden ist, aber Bilder im
        Seitentext verwendet werden (sehr häufiger Fall), muß
        stattdessen eine andere URL verwendet werden, die von der
        Methode getImageUrl erzeugt wird.

        """
        context = self.context
        if 0 and context.portal_type != 'UnitraccNews':
            return
        portal = context.getAdapter('portal')()
        rc = context.getAdapter('rc')()
        form = context.REQUEST.form
        DEBUG('Formulardaten:\n%s', pformat(form))

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
        try:
            DEBUG('getImage(%(self)r, %(uid)r', locals())
            if not uid:
                uid = form.get('uid')
                DEBUG('uid ist %r', uid)

            context = rc.lookupObject(uid)
            DEBUG('context ist jetzt %(context)r', locals())
            data = self._getPreviewImageData(context)
            if data is not None:
                return data

            # letzte Möglichkeit: Standard-Piktogramm
            data = context.restrictedTraverse('news_default_%(scaling)s.jpg'
                                              % form
                                              )._data
            return data
        except Exception as e:
            LOGGER.error('%(context)r->getImage(%(uid)r):', locals())
            LOGGER.exception(e)
        finally:
            sm.setOld()

    def getImageUrl(self, brain, scaling):
        """
        Gib die URL des Vorschaubilds für die Listenansicht zurück

        Prioritätenliste:
        1. das explizite Vorschaubild (wie -> getImage)
        2. die erste im Seitentext gefundene Bild-URL
        3. das Standard-Piktogramm für News (die Zeitung; wie -> getImage)
        """
        DEBUG('getImageUrl(%(brain)r, %(scaling)r)', locals())
        context = self.context
        context.REQUEST.form['scaling'] = scaling  # TH: warum in Formulardaten?
        portal = context.getAdapter('portal')()
        rc = context.getAdapter('rc')()
        uid = brain.UID
        pp(portal_type=brain.portal_type, hasImage=brain.hasImage)
        if brain.portal_type == 'UnitraccArticle':
            pdb.set_trace()

        # explizites Vorschaubild vorhanden?
        if brain.hasImage:
            return merge_qvars('@@news/getImage',
                               [('scaling', scaling),
                                ('uid', uid),
                                ])
        text = str(brain.getRawText)
        url = extract_1st_image_src(text, scaling)
        if url:
            return url

        # kein Bild im Text gefunden; verwende Standard-Piktogramm:
        image = context.restrictedTraverse('news_default_' + scaling + '.jpg', None)
        if image:
            return image.absolute_url()

    def _getPreviewImageData(self, o):
        """
        Gib die Bilddaten des konfigurierten Vorschaubilds zurück,
        aber *nicht* die des als letzte Möglichkeit zu verwendenden
        Standard-Piktogramms
        """
        scaling = o.getBrowser('scaling')
        data = scaling.get()
        if data:
            DEBUG('Ok: explizites Vorschaubild gefunden')
            # explizites Vorschaubild gefunden
            return data or None

    def _query(self, context, **kwargs):
        """
        Erzeuge die Suchargumente für --> search
        """
        query = {}
        form = context.REQUEST.form

        queryString = form.get('SearchableText', '')
        if queryString:
            DEBUG('search: queryString (1) = %(queryString)r', locals())
            txng = context.getBrowser('txng')
            queryString = txng.processWords(queryString).strip()
            DEBUG('search: queryString (2.txng) = %(queryString)r', locals())

        if queryString:
            queryString = '*' + queryString + '*'
            query['SearchableText'] = queryString

        query['portal_type'] = ['UnitraccNews', 'UnitraccArticle']
        query['getExcludeFromSearch'] = False

        query['sort_on'] = 'effective'
        query['sort_order'] = 'reverse'
        query['effective'] = {'query': DateTime(),
                              'range': 'max'}

        if form.has_key('getCustomSearch'):
            query['getCustomSearch'] = form['getCustomSearch']

        query['review_state'] = ['visible', 'inherit',
                                 'published', 'restricted']
        # Noch keine Behandlung etwaiger Doppelangaben:
        if kwargs:
            query.update(kwargs)
        return query

    def search_all(self):
        """
        @@nora.search_all: Suche alle News und Artikel
        """
        return self.search(search_limit=None)

    def search(self, **kwargs):
        """
        @@nora.search: Suche News und Artikel

        Die Suche ergibt üblicherweise zu wenige Artikel (bzw. gar
        keine, wegen der häufigeren und i.d.R. neueren News);
        daher wird gleich eine zweite Suche ausgeführt und die
        gefundenen Artikel dem Suchergebnis hinzugefügt.
        """
        context = self.context
        portal = context.getAdapter('portal')()

        sm = portal.getAdapter('securitymanager')
        sm(userId='system')
        sm.setNew()
	try:
            return self._search(context, **kwargs)
	finally:
            sm.setOld()

    def _search(self, context, **kwargs):

        if 'search_limit' in kwargs:
            limit = kwargs['search_limit']
            if limit is None:
                del kwargs['search_limit']
            else:
                kwargs['search_limit'] = limit = int(kwargs['search_limit'])
        else:
            kwargs['search_limit'] = limit = 12
        skip_uid = kwargs.pop('skip_uid', None)
        if skip_uid is not None and limit is not None:
            kwargs['search_limit'] += 1
        # balanced_list/minimum nicht mehr verwendet:
        if 'minimum' in kwargs:
            LOGGER.error('_search: "minimum" argument ignored (%(kwargs)s)', locals())
            del kwargs['minimum']

        pc = context.getAdapter('pc')()
        query = self._query(context, **kwargs)
        tutti = pc(query)
        if skip_uid is None:
            if limit is None:
                return tutti
            return tutti[:limit]
        elif limit is None:
            return [brain
                    for brain in tutti
                    if brain.UID != skip_uid
                    ]
        else:
            return [brain
                    for brain in tutti
                    if brain.UID != skip_uid
                    ][:limit]
        # nunmehr toter Code: 
        query['portal_type'] = 'UnitraccArticle'
        articles = pc(query)

        return balanced_list(tutti[:limit],
                             articles[:limit],
                             idfunc=lambda x: x.UID,
                             limit=limit,
                             minimum=minimum)

    def search_a(self):
        """
        Für Entwicklungszwecke:
        Suche *nur* nach Artikeln (von denen es weniger gibt)
        """
        return self.search(portal_type='UnitraccArticle')

# vim: ts=8 sts=4 sw=4 si et hls
