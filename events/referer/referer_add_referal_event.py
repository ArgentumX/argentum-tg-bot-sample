from events.referer.referer_event import RefererEvent
from objects.referer.referer import Referer


class RefererAddReferalEvent(RefererEvent):
    def __init__(self, referer: Referer):
        super().__init__(referer)
