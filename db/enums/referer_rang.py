import enum

from errors.api_error import ApiError


class RefererRangData:
    def __init__(self, enum_id: int, interests: float):
        self.enum_id = enum_id
        self.interests = interests


class RefererRang(enum.Enum):
    DEFAULT = RefererRangData(0, 0.1)
    AGENT = RefererRangData(1, 0.1)
    PLATINUM = RefererRangData(2, 0.5)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value.enum_id

    @property
    def enum_id(self):
        return self.value.enum_id

    @property
    def interests(self):
        return self.value.interests

    @staticmethod
    def get_by_name(rang_name):
        for referer_rang in list(RefererRang):
            if referer_rang.name == rang_name:
                return referer_rang
        raise ApiError.internal_error(f"Cant find RefererRang by name: {rang_name} ")

    @staticmethod
    def has_name(rang_name: str) -> bool:
        for referer_rang in list(RefererRang):
            if referer_rang.name == rang_name:
                return True
        return False

    @staticmethod
    def get_by_id(enum_id):
        for referer_rang in list(RefererRang):
            if referer_rang.enum_id == enum_id:
                return referer_rang
        raise ApiError.internal_error(f"Cant find RefererRang by id: {enum_id} ")
