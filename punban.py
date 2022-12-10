# Created by @Jisan7509
# All rights reserved.

import asyncio
import os
import random
import re

import requests
from bs4 import BeautifulSoup
from pySmartDL import SmartDL
from telethon.errors.rpcerrorlist import WebpageCurlFailedError
from urlextract import URLExtract
from userbot import catub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.functions import age_verification, unsavegif
from userbot.helpers.utils import reply_id

from .helpers import nsfw as useless

API = useless.API
horny = useless.nsfw(useless.pawn)

plugin_category = "useless"


def redlink(link, checker=False):
    pattern = re.compile(r"redgifs\.com\/?(?:watch\/)?([^\n.-]*)")
    regx = pattern.search(link)
    link = "https://www.redgifs.com/watch/" + regx[1]
    if checker:
        return link, f"./temp/{regx[1]}.mp4"
    return link


def redgif(link):
    link, file_name = redlink(link, True)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    red = requests.Session()
    source = red.get(link)
    soup = BeautifulSoup(source.text, "lxml")
    links = [itm["content"] for itm in soup.findAll("meta", property="og:video")]
    try:
        media_url = links[1]
    except IndexError:
        media_url = links[0]
    with red.get(media_url, stream=True) as r:
        with open(file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            return file_name


async def message_splitter(string_list, string, event):
    message = []
    for i in string_list:
        string += f"{i}\n"
        if len(string) > 4000:
            message.append(string)
            string = ""
    if string:
        message.append(string)
    count_msg = len(message)
    await event.edit(message[0], parse_mode="html")
    reply_to_msg = event.id
    if count_msg > 1:
        for i in range(1, count_msg):
            new_event = await catub.send_message(
                event.chat_id, message[i], parse_mode="html", reply_to=reply_to_msg
            )
            reply_to_msg = new_event.id


@catub.cat_cmd(
    pattern="porn(?:\s|$)([\s\S]*)",
    command=("porn", plugin_category),
    info={
        "header": "Get a porn video or gif or pic.",
        "usage": [
            "{tr}porn",
            "{tr}porn <options/subreddit>",
        ],
        "examples": "{tr}porn nsfw_gifs",
        "options": horny,
    },
)
async def very(event):  # sourcery skip: low-code-quality
    """Random porn post"""
    reply_to = await reply_id(event)
    sub_r = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    if await age_verification(catevent, reply_to):
        return
    flag = await useless.importent(catevent)
    if flag:
        return
    max_try = 0
    while max_try < 5:
        subreddit_api = (
            f"{API}/{sub_r}" if sub_r else f"{API}/{random.choice(useless.pawn)}"
        )
        try:
            cn = requests.get(subreddit_api)
            r = cn.json()
        except ValueError:
            return await edit_delete(catevent, "Value error!.")
        try:
            postlink = r["postLink"]
            title = r["title"]
            media_url = r["url"]
        except KeyError:
            return await edit_delete(
                catevent,
                "**(ノಠ益ಠ)ノ  You sure this is a valid catagory/subreddit ??**",
                time=20,
            )
        if "https://i.imgur.com" in media_url and media_url.endswith(".gifv"):
            media_url = media_url.replace(".gifv", ".mp4")
        elif "redgifs" in media_url:
            media_url = redgif(media_url)
        try:
            sandy = await event.client.send_file(
                event.chat_id,
                media_url,
                caption=f"<b><a href = {postlink}>{title}</a></b>",
                reply_to=reply_to,
                parse_mode="html",
            )
            if media_url.endswith((".mp4", ".gif")):
                await unsavegif(event, sandy)
                if os.path.exists(media_url):
                    os.remove(media_url)
            await catevent.delete()
            break
        except (WebpageCurlFailedError, ValueError):
            await edit_or_reply(catevent, f"**Value error!!..Link is :** {media_url}")
            await asyncio.sleep(3)
            await edit_or_reply(
                catevent,
                f"**Just hold your candel and Sit tight....\n\nAuto retry limit = {max_try+1}/5**",
            )
            await asyncio.sleep(1)
            max_try += 1
            if max_try == 5:
                await edit_delete(
                    catevent,
                    "**ಥ‿ಥ   Sorry i could'nt found, try with difference catagory**",
                )


@catub.cat_cmd(
    pattern="bulkporn(?:\s|$)([\s\S]*)",
    command=("bulkporn", plugin_category),
    info={
        "header": "download porn videos or gifs or pics in bulk.",
        "usage": [
            "{tr}bulkporn",
            "{tr}bulkporn <options/subreddit> <count>",
        ],
        "examples": "{tr}bulkporn nsfw_gifs 10",
        "options": horny,
    },
)
async def bad(event):
    """Download porn in bulk"""
    count = 3
    sub_r = random.choice(useless.pawn)
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt:
        sub_r = intxt
        if " " in intxt:
            sub_r, count = intxt.split(" ")

    if int(count) > 30:
        return await edit_delete(event, "**Value error!.. Count value 1 to 30**")
    catevent = await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    if await age_verification(catevent, reply_to):
        return
    flag = await useless.importent(catevent)
    if flag:
        return
    subreddit_api = f"{API}/{sub_r}/{count}"
    try:
        cn = requests.get(subreddit_api)
        r = cn.json()
    except ValueError:
        return await edit_delete(catevent, "Value error!.")
    title = []
    postlink = []
    media_url = []
    try:
        postlink.extend(x["postLink"] for x in r["memes"])
        title.extend(x["title"] for x in r["memes"])
        media_url.extend(x["url"] for x in r["memes"])
    except KeyError:
        return await edit_delete(
            catevent,
            "**(ノಠ益ಠ)ノ  You sure this is a valid catagory/subreddit ??**",
            time=20,
        )
    for i, (m, p, t) in enumerate(zip(media_url, postlink, title), start=1):
        if "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "redgifs" in m:
            media_url = redgif(m)
        else:
            media_url = m
        try:
            sandy = await event.client.send_file(
                event.chat_id,
                media_url,
                caption=f"<b><a href = {p}>{t}</a></b>",
                reply_to=reply_to,
                parse_mode="html",
            )
            if media_url.endswith((".mp4", ".gif")):
                await unsavegif(event, sandy)
                if os.path.exists(media_url):
                    os.remove(media_url)
            await edit_or_reply(
                catevent,
                f"**Bulk Download Started.\n\nCatagory :  `{sub_r}`\nFile Downloaded :  {i}/{count}**",
            )
            await asyncio.sleep(2)
        except (WebpageCurlFailedError, ValueError):
            await event.client.send_message(
                event.chat_id, f"**Value error!!..Link is :** {m}"
            )
        if i == int(count):
            await catevent.delete()


@catub.cat_cmd(
    pattern="rsearch(?:\s|$)([\s\S]*)",
    command=("rsearch", plugin_category),
    info={
        "header": "Get a list porn video or gif or pic from reddit /redgif /imgur.",
        "usage": [
            "{tr}rsearch",
            "{tr}rsearch <options/subreddit> <count>",
        ],
        "examples": "{tr}rsearch nsfw_gifs 10",
        "options": horny,
    },
)
async def pussy(event):
    """Send a list of reddit posts"""
    count = 5
    sub_r = random.choice(useless.pawn)
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt:
        sub_r = intxt
        if " " in intxt:
            sub_r, count = intxt.split(" ")

    if int(count) > 30:
        return await edit_delete(event, "**Value error!.. Count value 1 to 30**")
    catevent = await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    subreddit_api = f"{API}/{sub_r}/{count}"
    try:
        cn = requests.get(subreddit_api)
        r = cn.json()
    except ValueError:
        return await edit_delete(catevent, "Value error!.")
    if await age_verification(catevent, reply_to):
        return
    flag = await useless.importent(catevent)
    if flag:
        return
    title = []
    pwnlist = []
    media_url = []
    try:
        title.extend(x["title"] for x in r["memes"])
        media_url.extend(x["url"] for x in r["memes"])
    except KeyError:
        return await edit_delete(
            catevent,
            "**(ノಠ益ಠ)ノ  You sure this is a valid catagory/subreddit ??**",
            time=20,
        )
    for i, (m, t) in enumerate(zip(media_url, title), start=1):
        if "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "redgifs" in m:
            media_url = redlink(m)
        pwnlist.append(f"<b><i>{i}. <a href = {media_url}>{t}</a></b>")
    string = f"<b>{count} results for {sub_r} :</b>\n\n"
    await message_splitter(pwnlist, string, catevent)


@catub.cat_cmd(
    pattern="xsearch(?:\s|$)([\s\S]*)",
    command=("xsearch", plugin_category),
    info={
        "header": "Get a list of porn videos from xvideo",
        "usage": [
            "{tr}xsearch",
            "{tr}xsearch <search> <count> ",
            "{tr}xsearch <search> ; <count> ; <page no>",
        ],
        "examples": [
            "{tr}xsearch",
            "{tr}xsearch stepsis ; 10",
            "{tr}xsearch stepsis ; 10 ; 3",
        ],
    },
)
async def cat(event):
    """Send a list of xvideos posts"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    page = 0
    xtext = "stepsis"
    xcount = None
    if intxt:
        xtext = intxt
        if ";" in intxt:
            try:
                xtext, xcount, page = intxt.split(";")
            except ValueError:
                xtext, xcount = intxt.split(";")
    catevent = await edit_or_reply(event, "**Just hold a min you horny kid...**")
    if await age_verification(catevent, reply_to):
        return
    flag = await useless.importent(catevent)
    if flag:
        return
    page = requests.get(f"https://www.xvideos.com/?k={xtext}&p={int(page)}")
    soup = BeautifulSoup(page.text, "lxml")
    col = soup.findAll("div", {"class": "thumb"})
    if not col:
        return await edit_delete(
            catevent, "`No links found for that query , try differnt search...`", 60
        )

    listlink = []
    listname = []
    pwnlist = []
    for i in col:
        a = i.find("a")
        tmplink = a.get("href")
        links = f"https://www.xvideos.com{tmplink}"
        listlink.append(links)
        name = tmplink.split("/")[2]
        listname.append(name)
    await edit_or_reply(
        catevent,
        f"**{len(listlink)} results found for {xtext} :\nSending {xcount if xcount else 'All'} results out of them.**",
    )

    mylink = listlink[: int(xcount)] if xcount else listlink
    for count, (l, n) in enumerate(zip(mylink, listname), start=1):
        req = requests.get(l)
        soup = BeautifulSoup(req.text, "lxml")
        soups = soup.find("div", {"id": "video-player-bg"})
        for a in soups.find_all("a", href=True):
            link = a["href"]
        pwnlist.append(
            f"<b><i>{count}. <a href = {link}>{n.replace('_',' ').title()}</a></b>"
        )

    string = f"<b>Showing {xcount}/{len(listlink)} results for {xtext}.</b>\n\n"
    await message_splitter(pwnlist, string, catevent)


@catub.cat_cmd(
    pattern="linkdl(?: |$)([\s\S]*)",
    command=("linkdl", plugin_category),
    info={
        "header": "download porn video or gif in bulk or single from xvideos, imgur or redgif or direct link.\n\nFor multiple link give one space between links or reply to to any link contain text, like listporn or xsearch post",
        "usage": "{tr}linkdl <input link /reply to link>",
        "examples": "{tr}linkdl https://redgifs.com/watch/virtuousgorgeousindianspinyloach https://i.imgur.com/3Ffkon9.gifv",
    },
)
async def wants_ur_noods(event):  # sourcery skip: low-code-quality
    """Download ~~porns~~ *posts from link"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event,
            "**ಠ∀ಠ  Reply to valid link or give valid link url as input...you moron!!**",
        )
    extractor = URLExtract()
    plink = extractor.find_urls(intxt)
    catevent = await edit_or_reply(event, "** Just hold a sec u horny kid...**")
    if await age_verification(catevent, reply_to):
        return
    flag = await useless.importent(catevent)
    if flag:
        return
    i = 0
    for m in plink:
        media_url = m
        if not m.startswith("https://"):
            m = "https://" + m
        if "xvideo" in m:
            if ".mp4" not in m:
                req = requests.get(m)
                soup = BeautifulSoup(req.text, "lxml")
                soups = soup.find("div", {"id": "video-player-bg"})
                for a in soups.find_all("a", href=True):
                    m = a["href"]
            await edit_or_reply(
                catevent,
                "**Just hold your candel & sit tight, It will take some time...**",
            )
            if not os.path.isdir("./temp"):
                os.mkdir("./temp")
            xvdo = SmartDL(m, "./temp/porn.mp4", progress_bar=False)
            xvdo.start(blocking=False)
            xvdo.wait("finished")
            media_url = "./temp/porn.mp4"
        elif "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "redgifs.com/watch" in m:
            media_url = redgif(m)
        try:
            sandy = await event.client.send_file(
                event.chat_id, media_url, reply_to=reply_to
            )
            if media_url.endswith((".mp4", ".gif")):
                await unsavegif(event, sandy)
                if os.path.exists(media_url):
                    os.remove(media_url)
            await edit_or_reply(
                catevent,
                f"**Download Started.\n\nFile Downloaded :  {i+1}/{len(plink)}**",
            )
            await asyncio.sleep(2)
        except (WebpageCurlFailedError, ValueError):
            await event.client.send_message(
                event.chat_id, f"**Value error!!..Link is :** {m}"
            )
        i += 1
        if i == len(plink):
            await catevent.delete()
