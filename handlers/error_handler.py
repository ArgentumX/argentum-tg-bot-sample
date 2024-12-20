from aiogram import Router, F
from aiogram.types import ErrorEvent, Message, CallbackQuery
from loguru import logger

from bot import bot
from errors.api_error import ApiError

router = Router()


async def handle_error(error: ErrorEvent, event: CallbackQuery | Message):
    if isinstance(error.exception, ApiError):
        text = error.exception.message
        if error.exception.secret_message:
            logger.error(error.exception.secret_message)
        if bot.id != event.from_user.id:
            await bot.send_message(event.from_user.id, text)
    else:
        text = "Что-то пошло не так"
        logger.error(f"user {event.from_user.id} occurred error: {error.exception}")
        if bot.id != event.from_user.id:
            await bot.send_message(event.from_user.id, text)
        raise error.exception


@router.errors(F.update.message.as_("message"))
async def error_handler(event: ErrorEvent, message: Message):
    await handle_error(event, message)


@router.errors(F.update.callback_query.as_("callback"))
async def error_handler(event: ErrorEvent, callback: CallbackQuery):
    await handle_error(event, callback)
    await callback.answer()
