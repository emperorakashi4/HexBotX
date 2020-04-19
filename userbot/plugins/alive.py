"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in Heroku"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Gracias! HexBot Is Alive!!\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot created by:` [Akashi](tg://user?id=1089637689)\n"
                     f"`Forked By`: {DEFAULTUSER}\n"
                     "[Deploy This Userbot](https://github.com/emperorakashi4/HexBot)")
