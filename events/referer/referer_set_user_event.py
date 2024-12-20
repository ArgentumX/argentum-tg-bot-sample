from events.referer.referer_event import RefererEvent
from objects.referer.referer import Referer


class RefererSetUserEvent(RefererEvent):
    def __init__(self, referer: Referer):
        super().__init__(referer)
