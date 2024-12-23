from abc import abstractmethod, ABC

from objects.referer.referer import Referer


class User(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_id(self) -> int:
        pass

    @abstractmethod
    def get_tag(self) -> str:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    async def add_balance(self, value: float) -> None:
        pass

    @abstractmethod
    async def remove_balance(self, value: float) -> None:
        pass

    @abstractmethod
    async def set_balance(self, value: float) -> None:
        pass

    @abstractmethod
    async def delete(self) -> None:
        pass

    @abstractmethod
    async def get_referer(self) -> Referer:
        pass

    @abstractmethod
    async def get_inviter(self) -> Referer:
        pass
