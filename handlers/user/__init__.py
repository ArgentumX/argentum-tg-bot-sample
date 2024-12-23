from aiogram import Router

from handlers.user import general

router = Router()
router.include_routers(
    general.router,
)
