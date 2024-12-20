from sqlalchemy import Column, String, sql, Integer, Boolean

from config.config import REFERER_ID_LEN
from db.db import TimedBaseModel
from db.enums.association_type import AssociationType
from db.enums.referer_rang import RefererRang
from db.models.user_referer_model import UserRefererModel


class RefererModel(TimedBaseModel):
    __tablename__ = "referers"
    id = Column(String(REFERER_ID_LEN), primary_key=True)
    rang = Column(String(16), default=str(RefererRang.DEFAULT))
    quota = Column(Integer, default=0)
    is_new = Column(Boolean, default=True)
    query: sql.select

    async def delete_instance(self, *args, **kwargs):
        await self._delete_referal_associations()
        await self.delete(*args, **kwargs)

    async def _delete_referal_associations(self):
        referal_associations = await UserRefererModel.query.where(
            (UserRefererModel.referer_id == self.id) & (
                    UserRefererModel.type == str(AssociationType.REFERAL))).gino.all()
        for referal in referal_associations:
            await referal.delete()
