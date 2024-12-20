from sqlalchemy import Column, String, FLOAT, sql, BigInteger

from db.db import TimedBaseModel
from db.enums.association_type import AssociationType
from db.enums.referer_rang import RefererRang
from db.models.referer_model import RefererModel
from db.models.user_referer_model import UserRefererModel
from utils import referers


class UserModel(TimedBaseModel):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    tag = Column(String(64))
    balance = Column(FLOAT, default=0)
    query: sql.select

    async def delete_instance(self, *args, **kwargs):
        await self._delete_referal_association()
        await self._delete_referer_association()
        await self.delete(*args, **kwargs)

    async def _delete_referal_association(self):
        association = await UserRefererModel.get_user_referal(self.id)
        await association.delete()

    async def _delete_referer_association(self):
        user_ref = await UserRefererModel.get_user_referer(self.id)
        ref = await RefererModel.query.where(RefererModel.id == user_ref.referer_id).gino.first()
        await user_ref.delete()
        await ref.delete_instance()

    async def create(self, *args, **kwargs):
        await super().create(*args, **kwargs)
        referer = await referers.create_referer(self.id, RefererRang.DEFAULT)
        await UserRefererModel(user_id=self.id, referer_id=referer.get_id(),
                               type=str(AssociationType.REFERER)).create()
