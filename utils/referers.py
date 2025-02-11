from loguru import logger

from config import config
from db.enums.referer_rang import RefererRang
from db.models.referer_model import RefererModel
from errors.api_error import ApiError
from objects.referer.referer import Referer
from objects.referer.referer_impl import RefererImpl
from utils import generate


def generate_referer_id(user_id):
    fill_len = config.REFERER_ID_LEN - len(str(user_id))
    return generate.generate_random_str(fill_len) + str(user_id)


async def create_referer(user_id: int, rang: RefererRang) -> Referer:
    referer_model = RefererModel(id=generate_referer_id(user_id), rang=str(rang))
    await referer_model.create()
    referer = RefererImpl(referer_model)
    logger.info(f"Referer of user {user_id} was created. ref code: {referer_model.id}")
    return referer


async def get_referer_by_id(ref_id: str) -> Referer:
    referer_model = await RefererModel.query.where(RefererModel.id == ref_id).gino.first()
    if not referer_model:
        raise ApiError.bad_request("Указанный реферальный код не сушествует")
    referer = RefererImpl(referer_model)
    return referer