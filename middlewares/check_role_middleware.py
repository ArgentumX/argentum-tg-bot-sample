from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from loguru import logger

from enums.role import Role
from utils.roles import roles


class CheckRoleMiddleware(BaseMiddleware):
    def __init__(self, user_roles: list[Role]):
        self.user_roles = user_roles

    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        if not roles.has_any_role(event.from_user.id, self.user_roles):
            logger.warning(f"user {event.from_user.id} attempted to execute admin actions")
            return
        return await handler(event, data)
