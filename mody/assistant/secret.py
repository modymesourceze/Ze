import json
import os
import re

from telethon.events import CallbackQuery
from telethon.tl.functions.users import GetUsersRequest

from mody import zeub
from ..sql_helper.globals import gvarstatus


@zeub.tgbot.on(CallbackQuery(data=re.compile(b"secret_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    uzerid = gvarstatus("hmsa_id")
    ussr = int(uzerid) if uzerid.isdigit() else uzerid
    try:
        zzz = await zeub.get_entity(ussr)
    except ValueError:
        zzz = await zeub(GetUsersRequest(ussr))
    if os.path.exists("./mody/secret.txt"):
        jsondata = json.load(open("./mody/secret.txt"))
        try:
            message = jsondata[f"{timestamp}"]
            userid = message["userid"]
            ids = [userid, zeub.uid, zzz.id]
            if event.query.user_id in ids:
                encrypted_tcxt = message["text"]
                reply_pop_up_alert = encrypted_tcxt
            else:
                reply_pop_up_alert = "مطـي الهمسـه مـو الك 🦓"
        except KeyError:
            reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في البوت"
    else:
        reply_pop_up_alert = "- عـذراً .. هذه الرسـالة لم تعد موجـوده في البـوت"
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
