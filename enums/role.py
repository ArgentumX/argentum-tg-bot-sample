from enum import Enum

from errors.api_error import ApiError


class Role(Enum):
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_name(name: str):
        for role in list(Role):
            if role.name == name:
                return role
        raise ApiError.internal_error(f"Cant find Role by name: {name}")