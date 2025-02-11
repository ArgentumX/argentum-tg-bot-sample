from config import config
from objects.referer.referer import Referer
from objects.user.user import User


START_MESSAGE = (f'Привет, это ArgentumBot. С моей помощью вы можете сделать что-нибудь интересное\n'
                 f'\n'
                 f'/abstract_command - какая-нибудь команда')

UNEXPECTED_ACTION_MESSAGE = START_MESSAGE

HELP_MESSAGE = START_MESSAGE

async def get_ref_link_message(user: User) -> str:
    referer = await user.get_referer()
    ref_link = referer.get_referal_link()
    return f"Ваша реферальная ссылка: {ref_link}"

def get_all_user_info(user: User, referer: Referer) -> str:
    text = (f'telegram id: {user.get_id()}\n'
            f'tag: @{user.get_tag()}\n\n'
            f'balance: {user.get_balance()}\n\n'
            f'реферальная ссылка: {referer.get_referal_link()}\n')
    return text


def get_user_info(user: User, referer: Referer) -> str:
    text = (f'telegram id: {user.get_id()}\n\n'
            f'balance: {user.get_balance()}\n\n'
            f'реферальная ссылка: {referer.get_referal_link()}\n\n')
    return text

def get_referals_list(referals: list[User]) -> str:
    res = "["
    for user in referals:
        res += str(user.get_id()) + ", "
    res = res[:-2] if referals else res
    res += "]"
    return f'Рефералы пользователя: {res}'

def get_users_list(users: list[User]) -> str:
    res = "\n"
    for user in users:
        res += f"{str(user.get_id())}:@{user.get_tag()} ,\n"
    res = res[:-3] if users else res
    res += "\n"
    return f'{res}'