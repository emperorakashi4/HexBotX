"""Emoji

Available Commands:

.link"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "link":

        await event.edit(input_str)

        animation_chars = [
        
            "[CLICK ON THIS MESSAGE TO JOIN FREE NUDES GROUP\n\nCLICK HERE TO JOIN MY CHANNEL\n\nJOIN THIS CHANNE FOR NUDES OF INDIAN GIRLS\n\nJOIN THIS CHANNEL NOW TO GET ALL NUDES OF INDIAN GIRLS\n\nCLICK ON THIS MESSAGE NOW](https://t.me/joinchat/AAAAAEeHVdrWMlbMYhVumw)"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
