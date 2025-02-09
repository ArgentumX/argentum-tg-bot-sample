from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from loguru import logger

from enums.role import Role
from utils import users
from utils.roles import roles


class CheckAdminMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not roles.roles.has_any_role(event.from_user.id, [Role.ADMIN, Role.MODERATOR]):
            logger.warning(f"user {event.from_user.id} attempted to execute admin actions")
            return
        return await handler(event, data)
