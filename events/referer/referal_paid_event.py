from events.referer.referer_event import RefererEvent
from objects.referer.referer import Referer


class ReferalPaidEvent(RefererEvent):
    def __init__(self, referer: Referer, referal: Referer):
        self.referal = referal
        super().__init__(referer)
