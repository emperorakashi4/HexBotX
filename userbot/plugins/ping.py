from telethon import events
from datetime import datetime


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pinging!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Ping Is\n{}".format(ms))