from config import config
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

def get_all_user_info(user: User) -> str:
    text = (f'Пользователь\n\n'
            f'id: {user.get_id()}\n'
            f'tag: @{user.get_tag()}\n'
            f'balance: {user.get_balance()}\n')
    return text


def get_user_info(user: User) -> str:
    text = (f'Пользователь\n\n'
            f'id: {user.get_id()}\n'
            f'balance: {user.get_balance()}\n')
    return text
