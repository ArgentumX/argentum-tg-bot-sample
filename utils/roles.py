from enums.role import Role
from decorator_logging import *

from errors.api_error import ApiError


class Roles:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.roles = self.read()

    @SyncLoggable()
    def add_role(self, user_id: int, role: Role) -> None:
        if roles.has_role(user_id, role):
            raise ApiError.bad_request(f"Пользователь уже имеет роль: {role}")

        user_roles = self.roles.get(user_id, [])
        user_roles.append(role)
        self.roles[user_id] = user_roles

        self.save()

    @SyncLoggable()
    def remove_role(self, user_id: int, role: Role) -> None:
        if not roles.has_role(user_id, role):
            raise ApiError.bad_request(f"Пользователь не имеет роли: {role}")

        user_roles = self.roles.get(user_id)
        user_roles.remove(role)
        if not user_roles:
            self.roles.pop(user_id)

        self.save()

    def has_role(self, user_id: int, role: Role) -> bool:
        return role in self.roles.get(user_id, [])

    def has_any_role(self, user_id: int, from_roles: list[Role]) -> bool:
        for role in from_roles:
            if self.has_role(user_id, role):
                return True
        return False

    def get_roles(self, user_id) -> list[Role]:
        return self.roles.get(user_id, [])

    def get_users(self, role: Role):
        result = []
        for user_id in self.roles.keys():
            if self.has_role(user_id, role):
                result.append(user_id)
        return result

    def save(self) -> None:
        with open(self.file_name, "w+") as file:
            for user_id, role_list in self.roles.items():

                str_role_list = ""
                for role in role_list:
                    str_role_list += str(role) + ","
                str_role_list = str_role_list[:-1]
                print(f"{user_id}:{str_role_list}", file=file)

    def read(self) -> dict[int, list[Role]]:
        result = dict()
        with open(self.file_name, "a+") as file:
            file.seek(0)
            for x in file.readlines():
                user_id, user_roles = x.strip().split(":")
                user_roles = list(map(Role.get_by_name, user_roles.split(",")))
                user_id = int(user_id)
                result[user_id] = user_roles
        return result # noqa


roles = Roles("roles.txt")