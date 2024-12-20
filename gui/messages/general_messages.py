from config import config
from objects.user.user import User

UNEXPECTED_ACTION_MESSAGE = (f"Воспользуйтесь кнопками из главного меню ⬇️. "
                             f"Если возникли проблемы при работе с ботом,"
                             f" обязательно сообщите об этом {config.MODERATOR_CONTACT}")

HELP_MESSAGE = (f'Справка:\n\n'
                f'\n'
                f'По всем вопросам - {config.MODERATOR_CONTACT}\n')

START_MESSAGE = (f'Привет!')


def get_all_user_info(user: User) -> str:
    text = (f'Пользователь\n\n'
            f'id: {user.get_id()}\n'
            f'tag: @{user.get_tag()}\n'
            f'username: {user.get_username()}\n'
            f'balance: {user.get_balance()}\n')
    return text


def get_user_info(user: User) -> str:
    text = (f'Пользователь\n\n'
            f'id: {user.get_id()}\n'
            f'username: {user.get_username()}\n'
            f'balance: {user.get_balance()}\n')
    return text
