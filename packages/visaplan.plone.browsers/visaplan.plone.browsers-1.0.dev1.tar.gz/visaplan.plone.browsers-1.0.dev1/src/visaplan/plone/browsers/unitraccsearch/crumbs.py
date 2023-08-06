# -*- coding: utf-8 -*-

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import (ContextCrumb, SkipCrumb,
        register,
        )
from ...adapters.breadcrumbs.utils import crumbdict


def register_crumbs():
    for (tid, label) in [
        ('configure_localsearch', 'Configure local search'),
        ('configure_localsearch_json', 'Choose local search display preset'),
        ('brain_maintenance_view', 'Brain maintenance'),
        ]:
        register(ContextCrumb(tid, label, []))
    for tid in [
        'localsearch_view',
        ]:
        register(SkipCrumb(tid))

# -------------------------------------------- [ Initialisierung ... [
register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
