import requests
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from . import zeub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

ModyPH_cmd = (
    "𓆩 [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 - كـاشـف الارقـام العربيــة](t.me/source_ze) 𓆪\n\n"
    "**➥ الامــر ↵**\n\n"
    "➥ `.اكشف` + الـرقـم مـع مفتـاح الـدولة\n\n"
    "**➥ الوصـف :**\n"
    "**- لجـلب قائمـه بـ أسمـاء صاحب رقـم هـاتف معيـن**\n\n"
)


@zeub.ze_cmd(pattern="اكشف(?: |$)([\s\S]*)")
async def _(event): #Code by T.me/D_S_I
    number = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not number and reply:
        number = reply.text
    if not number:
        return await edit_delete(event, "**- الرقم خطأ او لم تقم بادخال كود الدولة +**", 10)
    if "+" not in number:
        return await edit_delete(
            event, "**- الرقم خطأ او لم تقم بادخال كود الدولة +**", 10
        )
    mody = "@ZZIIIbot" #Code by T.me/D_S_I
    ze = await edit_or_reply(event, "**☣╎جـارِ الكشـف عن الرقـم 📲**\n**☣╎انتظـر قليـلاً ... ▬▭**")
    async with borg.conversation(mody) as conv: # code by t.me/D_S_I
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            ze = await conv.get_response()
            malath = ze.text
            await borg.send_message(event.chat_id, ze)
            await ze.delete()
        except YouBlockedUserError:
            await zeub(unblock("ZZIIIbot"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(number)
            ze = await conv.get_response()
            malath = ze.text
            await borg.send_message(event.chat_id, ze)
            await ze.delete()



# Copyright (C) 2023 Ze . All Rights Reserved
@zeub.ze_cmd(pattern="الكاشف")
async def cmd(modyyy):
    await edit_or_reply(modyyy, ModyPH_cmd)