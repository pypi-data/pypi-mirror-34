# -*- coding: utf-8 -*-

# Unitracc-Tools:
from ...tools.misc import translate_dummy as _

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import RootedCrumb
from ...adapters.breadcrumbs.base import register, registered

from ..groupdesktop.crumbs import OK
from ..management.crumbs import imported


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    management_base_crumb = registered('management_view')
    _page_id = 'order_management'
    order_management_crumb = RootedCrumb(_page_id,
                                  'Buchungsverwaltung',
                                  [management_base_crumb])
    register(order_management_crumb, _page_id)
    for tid, label in [
            ('order_add',
             _('Buchung hinzufügen'),
             ),
            ('order_edit',
             _('Buchung bearbeiten'),
             ),
            ('order_view',
             _('Buchung Detailansicht'),
             ),
            ]:
        register(RootedCrumb(tid, label,
                             [order_management_crumb]))


register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]
