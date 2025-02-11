from aiogram import Router

from handlers.user import general, profile

router = Router()
router.include_routers(
    general.router,
    profile.router
)
