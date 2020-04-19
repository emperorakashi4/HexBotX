from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("`Muting User Globally!`")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("`User Is Already Gmuted!`")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("`You Are Muted In All The Chats Where I Am The Admin\nMessage Me To Get Yourself Unmuted!`")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("`Removing Global Mute!`")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("`User Can Already Speak Freely!`")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("`You Are Unmuted!\nPlease Be Careful Next Time!`")

@command(outgoing=True, pattern=r"^.gmute ?(\d+)?", allow_sudo=True)
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("`Muting User Globally!`")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to gmute them.")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("`User Is Already Gmuted!`")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("`You Are Muted In All The Chats Where I Am The Admin\nMessage Me To Get Yourself Unmuted!`")

@command(outgoing=True, pattern=r"^.ungmute ?(\d+)?", allow_sudo=True)
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("`Removing Global Mute!`")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit("Please reply to a user or add their into the command to ungmute them.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("`User Can Already Speak Freely!`")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("`You Are Unmuted!\nPlease Be Careful Next Time!`")

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
