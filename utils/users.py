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


async def create_user(user_id: int, tag: str, referer_id: str = None):
    user_model = UserModel(id=user_id, tag=tag)
    await user_model.create()
    logger.info(f"Registered user {user_id}")
    user = UserImpl(user_model)
    await event_manager.call(UserRegistrationEvent(user))
    try:
        if referer_id:
            referer = await referers.get_referer_by_id(referer_id)
            await referer.add_referal(user.get_id())
    except ApiError as e:
        logger.info(f"Failed add referal: {e.message}")
    return user
