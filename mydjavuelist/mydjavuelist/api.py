from ninja import NinjaAPI
from ninja.security import django_auth

from ..core.views_api import router as core_router

api = NinjaAPI(csrf=True)

api.add_router("/core/", core_router, auth=django_auth, tags=["core"])
