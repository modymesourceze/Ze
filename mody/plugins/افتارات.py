import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice, InputMessagesFilterPhotos

from . import zeub

from ..core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@zeub.ze_cmd(pattern="حالات$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات واتـس ...**")
    try:
        ZER = [
            mod
            async for mod in event.client.iter_messages(
                "@RSHDO5", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZER),
            caption=f"**🎆┊حـالات واتـس قصيـرة 🧸♥️**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="ستوري انمي$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الستـوري ...**")
    try:
        ZER = [
            mod
            async for mod in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZER),
            caption=f"**🎆┊ستـوريات آنمـي قصيـرة 🖤🧧**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="رقيه$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه ...**")
    try:
        zegan = [
            mod77
            async for mod77 in event.client.iter_messages(
                "@Rqy_1", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zegan),
            caption=f"**◞مقاطـع رقيـه شرعيـة ➧🕋🌸◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="رمادي$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shababbbbR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات شبـاب ࢪمـاديه ➧🎆🖤◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="رماديه$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banatttR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات بنـات ࢪمـاديه ➧🎆🤎◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="بيست$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...🧚🏻‍♀🧚🏻‍♀╰**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@Tatkkkkkim", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات بيست تطقيـم بنـات ➧🎆🧚🏻‍♀🧚🏻‍♀◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="حب$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...♥️╰**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@tatkkkkkimh", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات حـب تمبلـرࢪ ➧🎆♥️◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="رياكشن$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        ZER = [
            mod
            async for mod in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZER),
            caption=f"** 🎬┊رياكشـن تحشيـش ➧🎃😹◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="ادت$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل مقطـع ادت ...**")
    try:
        ZER = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZER),
            caption=f"**🎬┊مقاطـع ايـدت منوعـه ➧ 🖤🎭◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="غنيلي$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الاغنيـه ...𓅫╰**")
    try:
        zegan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zegan),
            caption=f"**✦┊تم اختياࢪ الاغنيـه لك 💞🎶**\nٴ▁ ▂ ▉ ▄ ▅ ▆ ▇ ▅ ▆ ▇ █ ▉ ▂ ▁",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        

@zeub.ze_cmd(pattern="شعر$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الشعـر ...**")
    try:
        zegan = [
            mod77
            async for mod77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zegan),
            caption=f"**✦┊تم اختيـار مقطـع الشعـر هـذا لك**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="ميمز$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الميمـز ...**")
    try:
        zegan = [
            mod77
            async for mod77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zegan),
            caption=f"**✦┊تم اختيـار مقطـع الميمـز هـذا لك**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="ري اكشن$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        zere = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zere),
            caption=f"**🎆┊رياكشـن تحشيـش ➧🎃😹◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="معلومه$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل صـورة ومعلومـة ...**")
    try:
        zeph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**🎆┊صـورة ومعلومـة ➧ 🛤💡◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="تويت$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ كـت تـويت بالصـور ...**")
    try:
        zere = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zere),
            caption=f"**✦┊كـت تـويت بالصـور ➧⁉️🌉◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="خيرني$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮•⎚ لـو خيـروك بالصـور ...**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**✦┊لـو خيـروك  ➧⁉️🌉◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="ولد انمي$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@dnndxn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات آنمي شبـاب ➧🎆🙋🏻‍♂◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="بنت انمي$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات آنمي بنـات ➧🎆🧚🏻‍♀◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@zeub.ze_cmd(pattern="بنات$")
async def _(event):
    zenevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zeph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banaaaat1", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zeph),
            caption=f"**◞افتـارات بنـات تمبلـرࢪ ➧🎆🧚🏻‍♀◟**",
        )
        await zenevent.delete()
    except Exception:
        await zenevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


