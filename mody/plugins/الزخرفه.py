import asyncio
import os
import sys
import urllib.request
from datetime import timedelta

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import zeub

from ..core.managers import edit_or_reply



@zeub.ze_cmd(pattern="زخرفة ?(.*)")
async def zilzal(event):
    card = event.pattern_match.group(1)
    chat = "@ZZ_ARBot"
    reply_id_ = await reply_id(event)
    ze = await edit_or_reply(event, "**- ارسـل (.زخرفه) + اسمـك بالانكلـش**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zeub(unblock("ZZ_ARBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await ze.delete()


@zeub.ze_cmd(pattern="زغرفه ?(.*)")
async def zelzal(event):
    card = event.pattern_match.group(1)
    chat = "@Z_ENBot"
    reply_id_ = await reply_id(event)
    ze = await edit_or_reply(event, "**- ارسـل (.زخرفه) + اسمـك بالانكلـش**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(card)
        except YouBlockedUserError:
            await zeub(unblock("Z_ENBot"))
            await conv.send_message(card)
        await asyncio.sleep(2)
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await ze.delete()

