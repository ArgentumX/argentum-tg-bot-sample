from enum import Enum


class BaseAction(str, Enum):
    def __str__(self):
        return self.name
