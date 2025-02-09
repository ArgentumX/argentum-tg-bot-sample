from events.event_manager import EventListener
from events.time.new_day_event import NewDayEvent


@EventListener(NewDayEvent)
async def on_new_day(event: NewDayEvent):
    pass
