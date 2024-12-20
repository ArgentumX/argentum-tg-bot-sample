from events.event import Event
from objects.referer.referer import Referer


class RefererEvent(Event):
    def __init__(self, referer: Referer):
        self.referer = referer
        super().__init__()
