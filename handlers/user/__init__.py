from aiogram import Router

from handlers.user import reg, general

router = Router()
router.include_routers(
    general.router,
    reg.router
)
