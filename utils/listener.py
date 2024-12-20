from events.event_manager import EventListener
from events.time.NewDayEvent import NewDayEvent


@EventListener(NewDayEvent)
async def on_new_day(event: NewDayEvent):
    pass
