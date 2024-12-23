from abc import abstractmethod, ABC

from db.enums.referer_rang import RefererRang


class Referer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_rang(self) -> RefererRang:
        pass

    @abstractmethod
    async def set_rang(self, rang: RefererRang) -> None:
        pass

    @abstractmethod
    async def add_referal(self, user_id: int) -> None:
        pass

    @abstractmethod
    async def set_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    async def get_user_id(self) -> int:
        pass

    @abstractmethod
    def get_referal_link(self):
        pass
