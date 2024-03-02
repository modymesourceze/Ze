import os
import shutil
from asyncio import sleep
from telethon import events

from . import zeub
from ..core.logger import logging
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.echo_sql import addecho, get_all_echos, get_echos, is_echo, remove_all_echos, remove_echo, remove_echos

from ..sql_helper.autopost_sql import get_all_post
from ..core.logger import logging
from . import BOTLOG, BOTLOG_CHATID
plugin_category = "الادوات"
LOGS = logging.getLogger(__name__)
zeself = True

POSC = gvarstatus("Z_POSC") or "(مم|ذاتية|ذاتيه|جلب الوقتيه)"

ZelzalSelf_cmd = (
    "𓆩 [ᯓ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 - حفـظ الذاتيـه 🧧](t.me/source_ze) 𓆪\n\n"
    "**⪼** `.تفعيل الذاتيه`\n"
    "**لـ تفعيـل الحفظ التلقائي للذاتيـه**\n"
    "**سوف يقوم حسابك بحفظ الذاتيه تلقائياً في حافظة حسابك عندما يرسل لك اي شخص ميديـا ذاتيـه**\n\n"
    "**⪼** `.تعطيل الذاتيه`\n"
    "**لـ تعطيـل الحفظ التلقائي للذاتيـه**\n\n"
    "**⪼** `.ذاتيه`\n"
    "**بالـرد ؏ــلى صـوره ذاتيـه لحفظهـا في حال كان امر الحفظ التلقائي معطـل**\n\n\n"
    "**⪼** `.اعلان`\n"
    "**الامـر + الوقت بالدقائق + الرسـاله**\n"
    "**امـر مفيـد لجماعـة التمويـل لـ عمـل إعـلان مـؤقت بالقنـوات**\n\n"
    "\n 𓆩 [🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱](t.me/source_ze) 𓆪"
)

@zeub.ze_cmd(pattern="الذاتيه")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalSelf_cmd)

@zeub.ze_cmd(pattern=f"{POSC}(?: |$)(.*)")
async def oho(event):
    if not event.is_reply:
        return await event.edit("**- ❝ ⌊بالـرد علـى صورة ذاتيـة التدميـر 𓆰...**")
    D_S_I = await event.get_reply_message()
    pic = await D_S_I.download_media()
    await zeub.send_file("me", pic, caption=f"**⎉╎تم حفـظ الصـورة الذاتيـه .. بنجـاح ☑️𓆰**")
    await event.delete()

@zeub.ze_cmd(pattern="(تفعيل الذاتيه|تفعيل الذاتية)")
async def start_datea(event):
    global zeself
    if zeself:
        return await edit_or_reply(event, "**⎉╎حفظ الذاتيـة التلقـائي .. مفعـله مسبقـاً ☑️**")
    zeself = True
    await edit_or_reply(event, "**⎉╎تم تفعيـل حفظ الذاتيـة التلقائـي .. بنجـاح ☑️**")

@zeub.ze_cmd(pattern="(تعطيل الذاتيه|تعطيل الذاتية)")
async def stop_datea(event):
    global zeself
    if zeself:
        zeself = False
        return await edit_or_reply(event, "**⎉╎تم تعطيـل حفظ الذاتيـة التلقائـي .. بنجـاح ☑️**")
    await edit_or_reply(event, "**⎉╎حفظ الذاتيـة التلقـائي .. معطلـه مسبقـاً ☑️**")

@zeub.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread))
async def sddm(event):
    global zeself
    zelzal = event.sender_id
    malath = zeub.uid
    if zelzal == malath:
        return
    if zeself:
        sender = await event.get_sender()
        chat = await event.get_chat()
        pic = await event.download_media()
        await zeub.send_file("me", pic, caption=f"[ᯓ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 - حفـظ الذاتيـه 🧧](t.me/source_ze) .\n\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n**⌔╎مࢪحبـاً عـزيـزي المـالك 🫂\n⌔╎ تـم حفـظ الذاتيـة تلقائيـاً .. بنجـاح ☑️** ❝\n**⌔╎المـرسـل** {_format.mentionuser(sender.first_name , sender.id)} .")

#Code For T.me/D_S_I
@zeub.ze_cmd(pattern="اعلان (\d*) ([\s\S]*)")
async def selfdestruct(destroy):
    ze = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ze[1]
    ttl = int(ze[0])
    zelzal = ttl * 60 #تعييـن الوقـت بالدقائـق بدلاً من الثـوانـي
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, message)
    await sleep(zelzal)
    await smsg.delete()

#Code For T.me/D_S_I
@zeub.ze_cmd(pattern="إعلان (\d*) ([\s\S]*)")
async def selfdestruct(destroy):
    ze = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ze[1]
    ttl = int(ze[0])
    zelzal = ttl * 60 #تعييـن الوقـت بالدقائـق بدلاً من الثـوانـي
    text = message + f"\n\n**- هذا الاعلان سيتم حذفه تلقـائيـاً بعـد {zelzal} دقائـق ⏳**"
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(zelzal)
    await smsg.delete()


@zeub.on(events.NewMessage(incoming=True))
async def gpost(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await zeub.send_message(int(chat), event.message)
