# -*- coding: utf-8 -*-
# Zope/Plone/dayta:
from dayta.browser.public import BrowserView, implements, Interface

# Standardmodule:
from datetime import datetime
from collections import defaultdict

# Dieser Browser:
from .utils import get_uid_and_info__factory, void_uid_info

# TODO: Refactoring
# - Verwendung der neuen SQL-Sicht course_statistics_overview
# - obsolete Methoden löschen

# Logging und Debugging:
import logging
logger = logging.getLogger('unitracc@@groupdesktop')
ERROR = logger.error
from visaplan.tools.debug import pp


class ICourseStatistics(Interface):
    """ Interface für die Klasse Statistics """

    def get(self, courseUid, sql=None):
        """ Gibt Kursstatistiken für einen User zurück. """

    def set(self, course_uid, page_uid, page_number,
                  page_count, view_type='course_view'):
        """ Speichert die Aktualisierte Statistik ab."""

    def get_statistic_overview(self, courseid=None, groupid=""):
        """
          Hole alle Statistiken einer Klasse zu einem Kurs
        """

    def delete_statistic(self, course_uid, user_uids):
        """
        Lösche Statistiken für Nutzer
        """


class Browser(BrowserView):
    """
        Dieser Browser sendet die Nutzerstatistiken an das StatistikObjekt,
        Welches dann die Daten verarbeitet.
    """

    implements(ICourseStatistics)

    def get(self, courseUID=None, user=None, sql=None, **kwargs):
        """
        Gib Kursstatistiken für einen User zurück.

        Die alte Aufrufsyntax mit den Argumente courseUID (als erstes
        übergeben, aber optional!), user und sql wird nicht mehr empfohlen;
        mittelfristig soll die Methode bereinigt und die Optionen courseUID und
        user zugunsten **kwargs entfernt werden.
        """
        context = self.context
        query_data = dict(kwargs)
        course_uid = query_data.get('course_uid')
        if courseUID is not None:
            if course_uid is None:
                query_data['course_uid'] = courseUID
            elif course_uid != courseUID:
                raise ValueError('%(courseUID)r != %(course_uid)r'
                                 % locals())
        if course_uid is None and 'course_uid' in query_data:
            del query_data['course_uid']
        user_uid = kwargs.pop('user_uid', None)
        if user is None:
            if user_uid is None:
                bauthor = context.getBrowser('author')
                user = bauthor.get()
                if user is None:
                    logger.error('get: No profile for user!')
                    return
                query_data['user_uid'] = user.UID()
        elif user_uid is not None:
            if user_uid != user:
                # altes Argument war schlecht benannt
                assert user_uid == user.UID()
        if sql is None:
            with context.getAdapter('sqlwrapper') as sql:
                return self._get(sql, **query_data)
        else:
            return self._get(sql, **query_data)

        # Alter Code - nur Tabelle unitracc_statistic_course: 
        context = self.context
        if sql is None:
            sql = context.getAdapter('sqlwrapper')
        if not user:
            bauthor = context.getBrowser('author')
            user = bauthor.get()
            if user is None:
                logger.error('get: No profile for user!')
                return
            user = user.UID()
        where = "WHERE user_uid=%(user_uid)s"
        values = {'user_uid': user}
        if courseUID:
            where += " AND course_uid=%(course_uid)s"
            values['course_uid'] = courseUID
        result = sql.select('unitracc_statistic_course',
                            where=where,
                            query_data=values)
        return result

    def _get(self, sql, **kwargs):
        """
        Gib die Kursstatistiken gemäß den übergebenen Filterkriterien zurück.

        Es wird die Sicht "course_statistics_overview" verwendet.
        Alle Felder aus der Tabelle unitracc_statistic_course sind unverändert
        enthalten (mit Ausnahme der nur datenbanktechnisch interessanten "id").
        """
        return sql.select('course_statistics_overview',
                          query_data=kwargs)

    def set(self, course_uid, page_uid, page_number,
                  page_count, view_type='course_view'):
        """
        Speichere die aktualisierte Statistik und gib sie zurück.
        """
        context = self.context
        if context.getAdapter('isanon')():
            return False
        bauthor = context.getBrowser('author')
        user = bauthor.get()
        if user is None:
            logger.error('set: No profile for user!')
            return
        with context.getAdapter('sqlwrapper') as sql:
            user_uid = user.UID()
            # bei Aktualisierung zu schreibende Werte: 
            page_data = {'page_view_date': datetime.now(),
                         'page_view_type': view_type,
                         }
            # Funktioniert nur für die Sicht c.s.p.: 
            page_query = {'user_uid': user_uid,
                          'course_uid': course_uid,
                          'page_uid': page_uid,
                          }
            # TODO: gleich sql.update verwenden, mit returning-Argument
            rows = sql.select('course_statistics_page',
                              query_data=page_query)
            if rows:
                # User hat diese Kursseite schon betrachtet 
                user_and_course_id = rows[0]['user_and_course_id']
                query_data = {'id': user_and_course_id,
                              'page_uid': page_uid,
                              }
                # update_page
                rows = list(sql.update('unitracc_page_statistic_course',
                           page_data,
                           query_data=query_data,
                           returning='id'))  # nur Kontrolle
            else:
                # Hat er wenigstens den Kurs schon besucht?
                rows = sql.select('course_statistics_overview',
                                  query_data={'user_uid': user_uid,
                                              'course_uid': course_uid,
                                              },
                                  fields=['user_and_course_id'])
                if rows:
                    user_and_course_id = rows[0]['user_and_course_id']
                else:
                    rows = list(sql.insert('unitracc_statistic_course',
                                      {'user_uid': user_uid,
                                       'course_uid': course_uid,
                                       'course_page_count': page_count,
                                       },
                                      returning='id'))
                    # returning='id AS ...' funzt leider nicht korrekt!
                    user_and_course_id = rows[0]['id']
                # set_page
                page_data.update({
                    'rid': user_and_course_id,
                    'page_uid': page_uid,
                    'page_number': page_number,
                    })

                sql.insert('unitracc_page_statistic_course',
                           page_data)
            return self._get_statistic(course_uid, user_uid, sql)
                           
    def _get_statistic(self, course_uid, user_uid, sql):
        # die Methode get_statistic wurde eliminiert!
        for row in sql.select('course_statistics_overview',
                              query_data={'user_uid': user_uid,
                                          'course_uid': course_uid,
                                          }):
            return row  # Es kann eigtl. nur eine geben
        return None  # pep 20.2

    def get_statistic_overview(self, course_uid=None, groupid=""):
        """
          Hole alle Statistiken einer Klasse zu einem Kurs
        """
        # TODO: Logikbastelei ersetzen durch SQL-View
        if not groupid or not course_uid:
            return []
        context = self.context
        # --------- [ Sicht course_statistics_overview verwenden ... [
        groupsharing = context.getBrowser('groupsharing')
        author = context.getBrowser('author')
        groupmembers = groupsharing.get_explicit_group_memberships(groupid)
        get_uid_and_info = get_uid_and_info__factory(context)
        uid2member = {}
        uids = []
        # derzeit ist immer eine Gruppe angegeben;
        # andernfalls müßte der umgekehrte Weg beschritten und zu jeder
        # user_uid die Benutzer-ID nebst Name herausgesucht werden
        for member in groupmembers:
            uid, infodict = get_uid_and_info(member)
            if uid is not None:
                uid2member[uid] = infodict
            uids.append(uid)

        query_data = {'course_uid': course_uid,
                      'user_uid': uids,
                      }
        with context.getAdapter('sqlwrapper') as sql:
            rows = sql.select('course_statistics_overview',
                              query_data=query_data)
            cnt = defaultdict(int)
            for row in rows:
                uid = row['user_uid']
                try:
                    cnt[uid] += 1
                    memberdict = uid2member.get(uid)
                    if memberdict is None:
                        logger.error('No member info for uid %(uid)r yet ...', locals())
                        # pp((('uid:', uid), ('row:', row),))
                        tmp = void_uid_info(uid)
                        for key in ('member_id', 'member_title'):
                            if not row.get(key):
                                logger.info('Default value for key %(key)s ...', locals())
                    else:
                        row.update(memberdict)
                except KeyError:
                    # pp((('uid:', uid), ('row:', row),))
                    tmp = void_uid_info(uid)
                    for key in ('member_id', 'member_title'):
                        if not row.get(key):
                            logger.info('Default value for key %(key)s ...', locals())

                try:
                    row['last_view_date'] = row['last_view_date'
                                                ].strftime("%d.%m.%Y %H:%M")
                except (ValueError, AttributeError) as e:
                    if row['last_view_date']:
                        logger.error("Can't convert last_view_date %(last_view_date)r"
                                     ' (%(user_id)r)',
                                     row)
                        logger.exception(e)
                    else:
                        logger.error("No last_view_date %(last_view_date)r"
                                     ' for user %(user_id)r',
                                     row)
                    row['last_view_date'] = None
            return rows
        # --------- ] ... Sicht course_statistics_overview verwenden ]

    def get_pages(self, rid, page_uid=None, fields=None, sql=None):
        """
        Hole einen oder mehrere Einträge aus der Tabelle
        """
        context = self.context
        if sql is None:
            sql = context.getAdapter('sqlwrapper')
        where = "WHERE rid=%(rid)s"
        where_dict = {'rid': rid}
        if page_uid:
            where += " AND page_uid=%(page_uid)s"
            where_dict['page_uid'] = page_uid
        if fields:
            fields = ', '.join(fields)
        else:
            fields = '*'
        query_l = ['SELECT', fields, 'FROM %(table)s', where]
        query = ' '.join(query_l) + ';'
        # hier direkt query-Methode aufrufen,
        # um die fields-Kontrolle zu umgehen:
        result = sql.query(query,
                           names={'table': 'unitracc_page_statistic_course'},
                           query_data=where_dict)
        return result

    def set_page(self, page_uid, page_number, view_type, rid, sql=None):
        """
        Schreibt eine neue Zeile in die Tabelle
        """
        context = self.context
        if sql is None:
            sql = self.context.getAdapter('sqlwrapper')
        now = datetime.now()
        values = {'rid': rid,
                  'page_uid': page_uid,
                  'page_number': page_number,
                  'page_view_date': now,
                  'page_view_type': view_type}
        table = "unitracc_page_statistic_course"
        sql.insert(table, values)

    def update_page(self, id, view_type, sql=None):
        """
        Setzt neue datetime und Pagecount für Seite
        """
        if sql is None:
            sql = self.context.getAdapter('sqlwrapper')

        values = {'page_view_date': datetime.now(),
                  'page_view_type': view_type}
        where = "WHERE id=%(id)s"
        where_dict = {'id': id}
        sql.update('unitracc_page_statistic_course', values, where, where_dict)

    def delete_statistic(self, course_uid, user_uids):
        """
        Lösche Statistiken für Nutzer
        """
        # ------ [ ON DELETE CASCADE ... [
        context = self.context
        message = context.getAdapter('message')
        if user_uids:
            with context.getAdapter('sqlwrapper') as sql:
                rows = sql.delete('unitracc_statistic_course',
                                  query_data={'course_uid': course_uid,
                                              'user_uid': user_uids,
                                              },
                                  returning='id')
                count = len(list(rows))
                message('${count} rows deleted.',
                        mapping=locals())
        else:
            message('Nothing to do!', 'error')
        request = context.REQUEST
        logger.info(request['HTTP_REFERER'])
        return request.RESPONSE.redirect(request['HTTP_REFERER'])
        # ------ ] ... ON DELETE CASCADE ]

if 0 and 'Futter fuer den Parser':
    _('never')  # Verwendung: templates/manage_statistic_course.pt,
                #             row/last_time_seen;
                # sollte durch ""'...'-Markierung eigentlich gefunden werden
