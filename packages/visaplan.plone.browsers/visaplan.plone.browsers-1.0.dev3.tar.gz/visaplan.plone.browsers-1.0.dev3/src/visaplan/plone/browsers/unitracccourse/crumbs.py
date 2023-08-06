# -*- coding: utf-8 -*-

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import (
        BaseCrumb, ViewCrumb,
        NoCrumbs,
        register, registered,
        )
from ...adapters.breadcrumbs.utils import crumbdict

from ..groupdesktop.crumbs import OK

# ---------------------------------------------- [ Crumb-Klassen ... [
class CourseOverviewCrumb(BaseCrumb):

    def get_course_brain(self, hub, info):
        #Warum hat man angefangen 2 unterschiedliche parameter in der URL zu verwenden?
        #Muss gerade gezogen werden. Übergabe parameter für UID sollte nur uid sein.
        for varname in ('cuid', 'uid'):
            uid = info['request_var'].get(varname, None)
            if uid:
                brain = hub['getbrain'](uid)
                if brain:
                    return (varname, uid, brain)
        return (None, None, None)

    def tweak(self, crumbs, hub, info):
        varname, uid, brain = self.get_course_brain(hub, info)

        if brain is not None:
            # Wenn auf Schreibtisch ...  
            if info['personal_desktop_done']:
                url = ''  # ... allgemeinere URL verwenden (TODO: Speicherort)
            else:
                url = info['context_url']  # ... ansonsten Pfad erhalten.
            tid = self.id
            crumbs.append(crumbdict(brain.Title,
                                    '%(url)s/%(tid)s?%(varname)s=%(uid)s'
                                    % locals()))


class TitledCourseCrumb(CourseOverviewCrumb):
    def __init__(self, id, label, parents):
        self.label = label
        CourseOverviewCrumb.__init__(self, id, parents)

    def tweak(self, crumbs, hub, info):
        varname, uid, brain = self.get_course_brain(hub, info)

        if brain is not None:
            url = info['context_url']
            tid = self.id
            crumbs.append(crumbdict(hub['translate'](self.label),
                                    '%(url)s/%(tid)s?%(varname)s=%(uid)s'
                                    % locals()))

# ---------------------------------------------- ] ... Crumb-Klassen ]


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    group_admin_crumb = registered('group_administration_view')
    overview_crumb = CourseOverviewCrumb('course_overview',
                                         parents=[group_admin_crumb])
    register(overview_crumb)
    documents_crumb = TitledCourseCrumb('course-documents',
                                        'Course documents',
                                        parents=[overview_crumb])
    register(documents_crumb)
    register(ViewCrumb('course_view'))
    for template_id in ('js-presentation-page',
                        ):
        register(NoCrumbs(template_id))


register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
