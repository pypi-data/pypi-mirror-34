# -*- coding: utf-8 -*-

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import RootedCrumb
from ...adapters.breadcrumbs.base import register, registered

from ..unitraccsettings.crumbs import OK


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    settings_crumb = registered('manage_settings')
    _page_id = 'configure_registration'
    subportal_crumb = RootedCrumb(_page_id,
                                  _('Configure registration'),
                                  [settings_crumb])
    register(subportal_crumb, _page_id)

register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
