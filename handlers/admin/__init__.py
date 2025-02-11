from aiogram import Router

from config import config
from enums.role import Role
from handlers.admin import dev, user_info, blacklist, referer, roles_manage
from middlewares.check_role_middleware import CheckRoleMiddleware
from utils.aiogram import include_global_middleware
from utils.roles import Roles

router = Router()
include_global_middleware(router, CheckRoleMiddleware([Role.ADMIN, Role.MODERATOR]))
router.include_routers(
    user_info.router,
    blacklist.router,
    referer.router,
    roles_manage.router,
)
if config.ENABLE_DEVELOP_TOOLS:
    router.include_router(dev.router)
