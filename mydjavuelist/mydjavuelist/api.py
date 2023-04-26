from ninja import NinjaAPI
from ninja.security import django_auth

from ..core.views_api import router as core_router
from ..accounts.views_api import router as accounts_router
from ..base.views_api import router as base_router

api = NinjaAPI(csrf=True)

api.add_router("/", base_router, tags=["base"])
api.add_router("/accounts/", accounts_router, tags=["accounts"])
api.add_router("/core/", core_router, auth=django_auth, tags=["core"])
