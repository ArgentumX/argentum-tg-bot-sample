import enum

from errors.api_error import ApiError


class AssociationType(enum.Enum):
    REFERER = "REFERER"
    REFERAL = "REFERAL"

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_name(name) -> enum.Enum:
        for association in list(AssociationType):
            if association.name == name:
                return association
        raise ApiError.internal_error(f"Cant find Association type by name: {name} ")
