# -*- coding: utf-8 -*-

# Andere Browser und Adapter:
from ...adapters.breadcrumbs.base import (
        NoCrumbs,
        register,
        )


# -------------------------------------------- [ Initialisierung ... [
def register_crumbs():
    for template_id in ('kss-presentation-page',
                        ):
        register(NoCrumbs(template_id))


register_crumbs()
# -------------------------------------------- ] ... Initialisierung ]

OK = True
