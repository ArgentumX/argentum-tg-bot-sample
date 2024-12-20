from config import config
from enums.role import Role


def is_admin(user_id: int) -> bool:
    return user_id in config.ADMINS.keys()


def get_roles(user_id: int) -> list[Role]:
    res = [Role.USER]
    if is_admin(user_id):
        res.append(Role.ADMIN)
    return res
