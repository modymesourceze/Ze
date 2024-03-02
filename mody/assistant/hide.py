import json
import os
import re

from telethon.events import CallbackQuery

from mody import zeub


@zeub.tgbot.on(CallbackQuery(data=re.compile(b"hide_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./mody/hide.txt"):
        jsondata = json.load(open("./mody/hide.txt"))
        try:
            reply_pop_up_alert = jsondata[f"{timestamp}"]["text"]
        except KeyError:
            reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات زد إي"
    else:
        reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في سيـرفرات زد إي"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
