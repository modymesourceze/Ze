import random
import re
import time
import psutil
from datetime import datetime
from platform import python_version

import requests
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from . import StartTime, zeub, zeversion

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import zealive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"


@zeub.ze_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    start = datetime.now()
    zeevent = await edit_or_reply(event, "**➯┊جـاري .. فحـص البـوت الخـاص بك**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    if gvarstatus("z_date") is not None:
        zzd = gvarstatus("z_date")
        zzt = gvarstatus("z_time")
        zea = f"{zzd}┊{zzt}"
    else:
        zea = f"{bt.year}/{bt.month}/{bt.day}"
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "** بـوت  زد إي 🔱 𝐙𝐄 🔱  يعمـل .. بنجـاح ☑️ 𓆩 **"
    ZE_IMG = gvarstatus("ALIVE_PIC")
    ze_caption = gvarstatus("ALIVE_TEMPLATE") or ze_temp
    caption = ze_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        zea=zea,
        telever=version.__version__,
        zdver=zeversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if ZE_IMG:
        ZE = [x for x in ZE_IMG.split()]
        PIC = random.choice(ZE)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await zeevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                zeevent,
                f"**⌔∮ عـذراً عليـك الـرد ع صـوره او ميـديـا  ➥  `.اضف صورة الفحص` <بالرد ع الصـوره او الميـديـا> ",
            )
    else:
        await edit_or_reply(
            zeevent,
            caption,
        )


ze_temp = """{ALIVE_TEXT}

**{Z_EMOJI} ✪➫➫➫➫ᘔE➫➫➫➫✪
**{Z_EMOJI} ➫♕ TEᒪE TᕼOᑎ ⌯ `{telever}`
**{Z_EMOJI} ➫♕ ᘔE ⌯ `{zdver}`
**{Z_EMOJI} ➫♕Ρყƚԋσɳ ⌯ `{pyver}`
**{Z_EMOJI} ➫♕ᏌᏢ ᎿᎥᎷᎬ ⌯ `{uptime}`
**{Z_EMOJI} ➫♕ᔕETᑌᑭ ᗪᗩTE ⌯ `{zea}`
**{Z_EMOJI} ➫♕ᏫᏔᏁᎬᎡ ✰ ⌯ {mention}
**{Z_EMOJI} [**𖠄 ᘔE ᑌᔕEᖇᗷOT 𖠄**](https://t.me/source_ze)
**{Z_EMOJI} ✪➫➫➫➫ᘔE➫➫➫➫✪"""


@zeub.ze_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
    info={
        "header": "- لـ التحـقق من ان البـوت يعمـل بنجـاح .. بخـاصيـة الانـلايـن ✓",
        "الاسـتخـدام": [
            "{tr}الفحص",
        ],
    },
)
async def amireallyialive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✥┊"
    ze_caption = "** ✪➫➫➫➫ᘔE➫➫➫➫✪️ 𓆩 **\n"
    ze_caption += f"**{Z_EMOJI} ➫♕ TEᒪE TᕼOᑎ ⌯ `{version.__version__}\n`"
    ze_caption += f"**{Z_EMOJI} ➫♕ ᘔE ⌯ `{zeversion}`\n"
    ze_caption += f"**{Z_EMOJI} ➫♕Ρყƚԋσɳ ⌯ `{python_version()}\n`"
    ze_caption += f"**{Z_EMOJI} ➫♕ᏫᏔᏁᎬᎡ ✰ ⌯ {mention}\n"
    ze_caption = "**𖠄 ᘔE ᑌᔕEᖇᗷOT 𖠄**\n"
    ze_caption = "** ✪➫➫➫➫ᘔE➫➫➫➫✪️ 𓆩 **\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, ze_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@zeub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await zealive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
