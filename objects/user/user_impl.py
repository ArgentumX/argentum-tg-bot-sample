from decorator_logging import *

from bot import bot
from db.models.referer_model import RefererModel
from db.models.user_model import UserModel
from db.models.user_referer_model import UserRefererModel
from errors.api_error import ApiError
from objects.referer.referer import Referer
from objects.referer.referer_impl import RefererImpl
from objects.user.user import User


class UserImpl(User):
    __user_model: UserModel

    def __init__(self, user_model: UserModel):
        self.__user_model = user_model
        super().__init__()

    def get_id(self) -> int:
        return self.__user_model.id

    def get_tag(self) -> str:
        return self.__user_model.tag

    def get_balance(self) -> float:
        return self.__user_model.balance

    @AsyncLoggable()
    async def add_balance(self, value: float) -> None:
        await self.__user_model.update(balance=self.get_balance() + value).apply()
        await bot.send_message(self.get_id(), f"Вам поступило {value} RUB на личный счёт")

    @AsyncLoggable()
    async def remove_balance(self, value: float) -> None:
        balance = self.get_balance() - value
        if balance < 0:
            raise ApiError.internal_error(f"Attempt to remove balance of user {self.get_id()} when not enough")
        await self.__user_model.update(balance=balance).apply()

    @AsyncLoggable()
    async def set_balance(self, value: float) -> None:
        if value < 0:
            raise ApiError.internal_error(f"Attempt to set negative balance of user {self.get_id()}")
        await self.__user_model.update(balance=value).apply()

    @AsyncLoggable()
    async def delete(self) -> None:
        await self.__user_model.delete_instance()

    async def get_referer(self) -> Referer:
        user_ref_model = await UserRefererModel.get_user_referer(self.get_id())
        ref_model = await RefererModel.query.where(RefererModel.id == user_ref_model.referer_id).gino.first()
        return RefererImpl(ref_model)

    async def get_inviter(self) -> Referer | None:
        user_ref_model = await UserRefererModel.get_user_referal(self.get_id())
        if not user_ref_model:
            return None
        ref_model = await RefererModel.query.where(RefererModel.id == user_ref_model.referer_id).gino.first()
        if not ref_model:
            return None
        return RefererImpl(ref_model)

    def __str__(self):
        return f"USER:{self.get_id()}"
