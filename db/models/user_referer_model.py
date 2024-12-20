from sqlalchemy import Column, BigInteger, String, sql, ForeignKey

from config.config import REFERER_ID_LEN
from db.db import TimedBaseModel
from db.enums.association_type import AssociationType


class UserRefererModel(TimedBaseModel):
    __tablename__ = "user-referer"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    referer_id = Column(String(REFERER_ID_LEN), ForeignKey("referers.id"), nullable=False)
    type = Column(String(16), nullable=False)
    query: sql.select

    @staticmethod
    async def get_user_referal(user_id):
        return await UserRefererModel.query.where(
            (UserRefererModel.user_id == user_id) & (
                    UserRefererModel.type == str(AssociationType.REFERAL))).gino.first()

    @staticmethod
    async def get_user_referer(user_id):
        return await UserRefererModel.query.where((UserRefererModel.user_id == user_id) & (
                UserRefererModel.type == str(AssociationType.REFERER))).gino.first()

    @staticmethod
    async def get_referer_user(referer_id):
        return await UserRefererModel.query.where(
            (UserRefererModel.referer_id == referer_id) & (
                    UserRefererModel.type == str(AssociationType.REFERER))).gino.first()
