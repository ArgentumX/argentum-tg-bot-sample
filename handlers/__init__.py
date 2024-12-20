from aiogram import Router

from config import config
from handlers import admin, unexpected_handler, user
from handlers.error_handler import router as error_handler_router
from middlewares.banned_middleware import BannedMiddleware
from middlewares.log_input_middleware import LogInputMiddleware
from middlewares.throttling_middleware import ThrottlingMiddleware
from utils.aiogram import include_global_middleware
from utils.blacklist import blacklist

router = Router()
router.include_router(error_handler_router)
include_global_middleware(router, BannedMiddleware(blacklist))
include_global_middleware(router, LogInputMiddleware())
include_global_middleware(router, ThrottlingMiddleware(config.DEFAULT_RATE_LIMIT, config.DEFAULT_RATE_TIME_CYCLE))
# include_global_middleware(router, BannedMiddleware())
router.include_routers(
    user.router,
    admin.router,
    unexpected_handler.router
)
