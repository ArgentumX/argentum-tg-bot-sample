from loguru import logger

from db.models.user_model import UserModel
from errors.api_error import ApiError
from events import event_manager
from events.user.user_registration_event import UserRegistrationEvent
from objects.user.user import User
from objects.user.user_impl import UserImpl
from utils import referers


async def get_user_by_id(user_id: int) -> User:
    user_model = await UserModel.query.where(UserModel.id == user_id).gino.first()
    if not user_model:
        raise ApiError.bad_request("Пользователь не найден")
    return UserImpl(user_model)


async def get_user_by_id_or_null(user_id: int) -> User | None:
    user_model = await UserModel.query.where(UserModel.id == user_id).gino.first()
    return UserImpl(user_model) if user_model else None


async def is_registered(user_id: int) -> bool:
    return (await get_user_by_id_or_null(user_id)) is not None


async def is_username_taken(username: str) -> bool:
    user = await UserModel.query.where(UserModel.username == username).gino.first()
    return user is not None


async def create_user(user_id: int, username: str, tag: str, referer_id: str = None):
    user_model = UserModel(id=user_id, username=username, tag=tag)
    await user_model.create()
    logger.info(f"user {user_id} created reg request")
    user = UserImpl(user_model)
    if referer_id:
        referer = await referers.get_referer_by_id(referer_id)
        await referer.add_referal(user.get_id())
    await event_manager.call(UserRegistrationEvent(user))
    return user
