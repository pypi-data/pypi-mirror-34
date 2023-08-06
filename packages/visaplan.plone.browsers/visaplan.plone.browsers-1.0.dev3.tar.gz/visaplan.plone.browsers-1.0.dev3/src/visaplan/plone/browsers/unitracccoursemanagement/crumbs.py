# -*- coding: utf-8 -*-

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import RootedCrumb
from ...adapters.breadcrumbs.base import register, registered

# wg. management_base_crumb:
from ..management.crumbs import imported


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    management_base_crumb = registered('management_view')
    _page_id = 'manage_course_view'
    main_crumb = RootedCrumb(_page_id,
                             _('Courses'),  # Seitenüberschrift: Course Manager
                             [management_base_crumb])
    register(main_crumb, _page_id)

    for tid, label in [
            ('manage_statistic_course',
             _('Statistics'),  # Seitenüberschrift: 'Course statistics manager'
             ),
            ]:
        register(RootedCrumb(tid, label,
                             [main_crumb]))


register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]
