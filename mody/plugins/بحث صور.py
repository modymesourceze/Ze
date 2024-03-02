import asyncio
import aiohttp
import os
import shutil
import time
from bs4 import BeautifulSoup
from datetime import datetime
from telethon.utils import guess_extension
from urllib.parse import urlencode

from . import zeub
from ..Config import Config

MODY_APP_ID = "6e65179ed1d879f3d905e28ef8803625"


@zeub.ze_cmd(pattern="صور (.*)")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**╮ ❐ جـاري البحث عن الصـور  ...𓅫╰**")
    ze = event.pattern_match.group(1)
    wze_dir = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY,
        ze
    )
    if not os.path.isdir(wze_dir):
        os.makedirs(wze_dir)
    input_url = "https://bots.shrimadhavuk.me/search/"
    headers = {"USER-AGENT": "UseTGBot"}
    url_lst = []
    async with aiohttp.ClientSession() as requests:
        data = {
            "q": ze,
            "app_id": MODY_APP_ID,
            "p": "GoogleImages"
        }
        reponse = await requests.get(
            input_url,
            params=data,
            headers=headers
        )
        response = await reponse.json()
        for result in response["results"]:
            if len(url_lst) > 9:
                break
            caption = result.get("description")
            image_url = result.get("url")
            image_req_set = await requests.get(image_url)
            image_file_name = str(time.time()) + "" + guess_extension(
                image_req_set.headers.get("Content-Type")
            )
            image_save_path = os.path.join(
                wze_dir,
                image_file_name
            )
            with open(image_save_path, "wb") as f_d:
                f_d.write(await image_req_set.read())
            url_lst.append(image_save_path)
    if not url_lst:
        await event.edit(f"**- اووبـس .. لم استطـع ايجـاد صـور عـن {ze} ؟!**\n**- حـاول مجـدداً واكتـب الكلمـه بشكـل صحيح**")
        return
    await event.reply(
        file=url_lst,
        parse_mode="html",
        force_document=True
    )
    for each_file in url_lst:
        os.remove(each_file)
    shutil.rmtree(wze_dir, ignore_errors=True)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"**- اكتمـل البحث عـن {ze} في {ms} ثانيـه ✓**",
        link_preview=False
    )
    await asyncio.sleep(5)
    await event.delete()



@zeub.ze_cmd(pattern="خلفيات (.*)")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**╮ ❐ جـاري البحث عن خلفيـات  ...𓅫╰**")
    ze = event.pattern_match.group(1)
    wze_dir = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY,
        ze
    )
    if not os.path.isdir(wze_dir):
        os.makedirs(wze_dir)
    input_url = "https://bots.shrimadhavuk.me/search/"
    headers = {"USER-AGENT": "UseTGBot"}
    url_lst = []
    async with aiohttp.ClientSession() as requests:
        data = {
            "q": ze,
            "app_id": MODY_APP_ID,
            "p": "GoogleImages"
        }
        reponse = await requests.get(
            input_url,
            params=data,
            headers=headers
        )
        response = await reponse.json()
        for result in response["results"]:
            if len(url_lst) > 9:
                break
            caption = result.get("description")
            image_url = result.get("url")
            image_req_set = await requests.get(image_url)
            image_file_name = str(time.time()) + "" + guess_extension(
                image_req_set.headers.get("Content-Type")
            )
            image_save_path = os.path.join(
                wze_dir,
                image_file_name
            )
            with open(image_save_path, "wb") as f_d:
                f_d.write(await image_req_set.read())
            url_lst.append(image_save_path)
    if not url_lst:
        await event.edit(f"**- اووبـس .. لم استطـع ايجـاد خلفيـات عـن {ze} ؟!**\n**- حـاول مجـدداً واكتـب الكلمـه بشكـل صحيح**")
        return
    await event.reply(
        file=url_lst,
        parse_mode="html",
        force_document=True
    )
    for each_file in url_lst:
        os.remove(each_file)
    shutil.rmtree(wze_dir, ignore_errors=True)
    end = datetime.now()
    ms = (end - start).seconds
    await event.edit(
        f"**- اكتمـل البحث عـن {ze} في {ms} ثانيـه ✓**",
        link_preview=False
    )
    await asyncio.sleep(5)
    await event.delete()
