from loguru import logger

from config import config
from db.enums.association_type import AssociationType
from db.enums.referer_rang import RefererRang
from db.models.referer_model import RefererModel
from db.models.user_referer_model import UserRefererModel
from errors.api_error import ApiError
from events import event_manager
from events.referer.referer_add_referal_event import RefererAddReferalEvent
from events.referer.referer_set_user_event import RefererSetUserEvent
from utils.aop.logger.decorator import AsyncLoggable
from .referer import Referer

class RefererImpl(Referer):
    __referer_model: RefererModel

    def __init__(self, referer_model: RefererModel):
        self.__referer_model = referer_model
        super().__init__()

    def get_id(self) -> int:
        return self.__referer_model.id

    def get_rang(self) -> RefererRang:
        return RefererRang.get_by_name(self.__referer_model.rang)

    @AsyncLoggable()
    async def set_rang(self, rang: RefererRang) -> None:
        await self.__referer_model.update(rang=str(rang)).apply()
        logger.info(f"Referer {self.get_id()} rang was set to {rang}")

    @AsyncLoggable()
    async def add_referal(self, user_id: int) -> None:
        association = await UserRefererModel.query.where((UserRefererModel.user_id == user_id) & (
                UserRefererModel.type == str(AssociationType.REFERAL))).gino.first()
        if association:
            raise ApiError.bad_request("Пользователь уже ввёл реферальный код")
        new_association = UserRefererModel(user_id=user_id, referer_id=self.get_id(),
                                           type=str(AssociationType.REFERAL))
        await new_association.create()
        await event_manager.call(RefererAddReferalEvent(self))

    @AsyncLoggable()
    async def set_user(self, user_id: int) -> None:
        association = await UserRefererModel.query.where(UserRefererModel.referer_id == self.get_id(),
                                                         type=str(AssociationType.REFERER)).gino.first()
        if association:
            await association.delete()
            logger.info(f"Old referer {self.get_id()} - user {association.user_id}  association was deleted")
        new_association = UserRefererModel(user_id=user_id, referer_id=self.get_id(),
                                           type=str(AssociationType.REFERER))
        await new_association.create()
        await event_manager.call(RefererSetUserEvent(self))

    async def get_user_id(self) -> int:
        association = await UserRefererModel.get_referer_user(self.get_id())
        return association.user_id

    def get_referal_link(self):
        return config.BOT_LINK + f"?start={self.get_id()}"

    def __str__(self):
        return f"REFERER:{self.get_id()}"