# -*- coding: utf-8 -*-
# Plone/Zope/Dayta:
from dayta.browser.public import Interface, BrowserView, implements

# Standardmodule:
from datetime import date
from time import localtime

# Unitracc:
from ...permissions import ManageCourses

# Andere Browser:
from ..unitraccgroups.utils import LEARNER_SUFFIX, \
        learner_group_id

# Dieser Browser:
from .crumbs import register_crumbs
register_crumbs()


class IUnitraccCourseManager(Interface):

    def get_course_view_duration(self, group_id, course_id):
        """
        """

    def update_course_view_duration(self):
        """

        """

    def canManageCourses(self):
        """
        Darf der angemeldete Benutzer Kurse administrieren?
        """

    def authManageCourses(self):
        """
        Wirft Unauthorized, wenn der angemeldete Benutzer keine Kurse
        administrieren kann
        """

class Browser(BrowserView):

    def canManageCourses(self):
        """
        Darf der angemeldete Benutzer Kurse administrieren?
        """
        return self.context.getAdapter('checkperm')(ManageCourses)

    def authManageCourses(self):
        """
        Wirft Unauthorized, wenn der angemeldete Benutzer keine Kurse
        administrieren kann
        """
        self.context.getAdapter('authorized')(ManageCourses)

    def get_course_view_duration(self, group_id, course_id):
        context = self.context
        sql = context.getAdapter('sqlwrapper')
        fields = ['start', 'ends']
        table = "unitracc_groupmemberships"
        data = {'group_id_': course_id,
                'member_id_': group_id,
                }
        where = "WHERE group_id_=%(group_id_)s and member_id_=%(member_id_)s"
        result = sql.select(table=table,
                            where=where,
                            fields=fields,
                            query_data=data)
        res = {'start': '',
               'end': '',
               }
        if result:
            res['start'] = result[0]['start'].strftime("%d.%m.%Y")
            if result[0]['ends']:
                res['end'] = result[0]['ends'].strftime("%d.%m.%Y")

        return res

    def update_course_view_duration(self):
        """

        """
        context = self.context
        form = context.REQUEST.form
        sql = context.getAdapter('sqlwrapper')
        groups = context.getBrowser('groups')
        acl = context.getAdapter('acl')()
        TODAY = date.today()

        def makedate(s):
            if s:
                liz = map(int, s.split('.'))
                assert len(liz) == 3, '"d.m.yyyy" date value expected (%r)' % s
                liz.reverse()
                return date(*tuple(liz))
            return None

        start = form.get('start')
        if not start:
            # TODAY won't work for SQL:
            start = date(*localtime()[:3])
        else:
            start = makedate(start)
        course = groups.getById(form.get('course'))
        group = form.get('group')
        data = {'group_id_':  form['course'],
                'member_id_': form['group'],
                }
        table = "unitracc_groupmemberships"
        where = "WHERE group_id_=%(group_id_)s and member_id_=%(member_id_)s"
        end = makedate(form.get('end'))
        newdata = {'start': start,
                   'ends':  end,
                   }

        if sql.select(table, where=where,
                      query_data=data):
            sql.update(table, newdata, where, query_data=data)
        else:
            data.update(newdata)
            sql.insert(table, data)

        members = acl.source_groups._group_principal_map[form.get('course')]
        if start <= TODAY and not group in members:
            course.addMember(form.get('group'))

        if start > TODAY and group in members:
            course.removeMember(form.get('group'))
        return True

    def getCourse(self, gid):
        """
        Hole alle Kurse;
        falls Manager, auch unveröffentlichte.
        """
        context = self.context
        groups = context.getBrowser('groupsharing')
        acl = context.getAdapter('acl')()
        pc = context.getAdapter('pc')()
        rc = context.getAdapter('rc')()
        courses = []
        if gid:
            #Hole alle Kurse auf die die Gruppe Zugriff hat.
            if gid.split("_")[-1] == LEARNER_SUFFIX:
                coursegroups=[gid]
            else:
                coursegroups = groups._get_filtered_groups(gid)
        else:
            #Hole alle Kurse aus Portal Catalog.
            coursegroups = groups.search_groups(LEARNER_SUFFIX)
            coursegroups = [x['id'] for x in coursegroups]
        for member in coursegroups:
            if member.split("_")[-1] == LEARNER_SUFFIX:
                group_id = member.split("_")[1]
                course = rc.lookupObject(group_id)
                if course:
                    courses.append(course)
        return courses


    def getClasses(self, cid):
        """
        Hole alle Klassen, falls eine CID( Kurs id) angegeben ist füge
        den Eintrag direkte Mitglieder hinzu.
        """
        context = self.context
        groups = context.getBrowser('groupsharing')
        rc = context.getAdapter('rc')()
        acl = context.getAdapter('acl')()
        classes = []
        memberships =[]
        if cid:
            """
                Hole alle Klasse die auf den Kurs Zugriff hat.
            """
            groupid = learner_group_id(cid)
            group = [{'type':'group', 'id': groupid, 'title': 'Direkte Mitglieder'}]
            memberships.append(group)
            memberships.append(groups.get_explicit_group_memberships(groupid))


        else:
            courses = groups.search_groups(LEARNER_SUFFIX)
            for course in courses:
                memberships.append(groups.get_explicit_group_memberships(course['id']))


        for members in memberships:
            for member in members:
                if member['type'] == "group":
                    classes.append(member)


        return classes

