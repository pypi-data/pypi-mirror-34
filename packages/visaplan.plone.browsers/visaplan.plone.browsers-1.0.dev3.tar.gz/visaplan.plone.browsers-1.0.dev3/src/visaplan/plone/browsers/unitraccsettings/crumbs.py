# -*- coding: utf-8 -*-

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import RootedCrumbWithChild
from ...adapters.breadcrumbs.base import register, registered

from ..management.crumbs import imported

# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    management_base_crumb = registered('management_view')
    _page_id = 'manage_settings'
    settings_crumb = RootedCrumbWithChild(_page_id,
                                          _('Miscellaneous Settings'),
                                          'key',
                                          [management_base_crumb])
    register(settings_crumb, _page_id)

register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
