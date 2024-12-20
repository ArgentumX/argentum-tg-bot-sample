from aiogram import Router, BaseMiddleware
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from multipledispatch import dispatch

from errors.api_error import ApiError


def get_args(message: Message, required_args: int = None) -> list[str]:
    splitted = message.text.split()
    if required_args and len(splitted) != required_args:
        raise ApiError.bad_request("Недостаточно параметров")
    return splitted


def include_global_middleware(router: Router, middleware: BaseMiddleware) -> None:
    router.message.middleware(middleware)
    router.callback_query.middleware(middleware)


@dispatch(Message)
def extract_data(message: Message) -> str:
    return message.text


@dispatch(CallbackQuery)
def extract_data(callback: CallbackQuery) -> str:
    return callback.data


def get_txt_file(filename: str, text: str) -> BufferedInputFile:
    return BufferedInputFile(text.encode('utf-8'), filename=filename)
