from events.event import Event


class NewDayEvent(Event):
    def __init__(self):
        super().__init__()
