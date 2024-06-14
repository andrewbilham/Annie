from fastapi import APIRouter

from app.api.routes import items, login, users, utils, sources,suppliers,circs_groups,claims,referrals_allocations,referrals,source_rates,supplier_rates,veh_groups,authorities

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(sources.router, prefix="/sources", tags=["sources"])
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(circs_groups.router, prefix="/circs_groups", tags=["circs_groups"])
api_router.include_router(claims.router, prefix="/claims", tags=["claims"])
api_router.include_router(referrals_allocations.router, prefix="/referrals_allocations", tags=["referrals_allocations"])
api_router.include_router(referrals.router, prefix="/referrals", tags=["referrals"])
api_router.include_router(source_rates.router, prefix="/source_rates", tags=["source_rates"])
api_router.include_router(supplier_rates.router, prefix="/supplier_rates", tags=["supplier_rates"])
api_router.include_router(veh_groups.router, prefix="/veh_groups", tags=["veh_groups"])
api_router.include_router(authorities.router, prefix="/authorities", tags=["authorities"])