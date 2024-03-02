import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import zeub
from ..core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البحث"

@zeub.ze_cmd(
    pattern="ريماكس ([\s\S]*)",
    command=("ريماكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريماكس + كلمـة",
    },
)
async def remaxzethon(zerm):
    ok = zerm.pattern_match.group(1)
    if not ok:
        if zerm.is_reply:
            what = (await zerm.get_reply_message()).message
        else:
            await zerm.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "spotifybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(zerm.chat_id,
                            reply_to=zerm.reply_to_msg_id,
                            silent=True if zerm.is_reply else False,
                            hide_via=True)
    await zerm.delete()
    

@zeub.ze_cmd(
    pattern="ريمكس ([\s\S]*)",
    command=("ريمكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريمكس + كلمـة",
    },
)
async def ze(event):
    if event.fwd_from:
        return
    zer = event.pattern_match.group(1)
    mody = "@spotifybot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(mody, zer)
    await tap[0].click(event.chat_id)
    await event.delete()

