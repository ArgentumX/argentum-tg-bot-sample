from loguru import logger

from errors.api_error import ApiError


class Blacklist:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.blacklist = self.read_blacklist()

    def add(self, user_id: int) -> None:
        if blacklist.contains(user_id):
            raise ApiError.bad_request("Пользователь уже в чёрном списке")
        self.blacklist.add(user_id)
        self.save_blacklist()
        logger.info(f"user {user_id} was banned")

    def remove(self, user_id: int) -> None:
        if not blacklist.contains(user_id):
            raise ApiError.bad_request("Пользователя нет в чёрном списке")
        self.blacklist.remove(user_id)
        self.save_blacklist()
        logger.info(f"user {user_id} was unbanned")

    def contains(self, user_id: int) -> bool:
        return user_id in self.blacklist

    def save_blacklist(self) -> None:
        with open(self.file_name, "w+") as file:
            for user_id in self.blacklist:
                print(user_id, file=file)

    def read_blacklist(self) -> set[int]:
        result = set()
        with open(self.file_name, "a+") as file:
            file.seek(0)
            for x in file.readlines():
                result.add(int(x))
        return result


blacklist = Blacklist("blacklist.txt")
