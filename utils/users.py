from loguru import logger

from db.enums.association_type import AssociationType
from db.models.user_model import UserModel
from db.models.user_referer_model import UserRefererModel
from errors.api_error import ApiError
from events import event_manager
from events.user.user_registration_event import UserRegistrationEvent
from objects.referer.referer import Referer
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

async def get_referals(user: User) -> list[User]:
    result = []
    referer = await user.get_referer()
    associations = await UserRefererModel.query.where((UserRefererModel.referer_id == referer.get_id()) & (
        UserRefererModel.type == str(AssociationType.REFERAL))).gino.all()
    for association in associations:
        user = await get_user_by_id(association.user_id)
        result.append(user)
    return result

async def get_all_users() -> list[User]:
    users = list(map(UserImpl, await UserModel.query.gino.all()))
    return users