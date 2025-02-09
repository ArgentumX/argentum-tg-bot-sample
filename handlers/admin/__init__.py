from aiogram import Router

from config import config
from handlers.admin import dev, user_info, blacklist, referer, roles_manage
from middlewares.check_admin_middleware import CheckAdminMiddleware
from utils.aiogram import include_global_middleware

router = Router()
include_global_middleware(router, CheckAdminMiddleware())
router.include_routers(
    user_info.router,
    blacklist.router,
    referer.router,
    roles_manage.router,
)
if config.ENABLE_DEVELOP_TOOLS:
    router.include_router(dev.router)
