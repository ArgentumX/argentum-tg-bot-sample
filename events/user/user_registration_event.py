from events.user.user_event import UserEvent
from objects.user.user import User


class UserRegistrationEvent(UserEvent):
    def __init__(self, user: User):
        super().__init__(user)
