from events.event import Event
from objects.user.user import User


class UserEvent(Event):
    def __init__(self, user: User):
        self.user = user
        super().__init__()
