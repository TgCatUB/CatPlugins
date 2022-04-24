# Created by @Jisan7509

import base64
import logging
import random

import requests
from telethon import functions, types
from telethon.errors.rpcerrorlist import UserNotParticipantError, YouBlockedUserError
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers import media_type
from userbot.helpers.utils import _catutils, reply_id
from userbot import catub

plugin_category = "useless"

LOGS = logging.getLogger(__name__)


@catub.cat_cmd(
    pattern="dis$",
    command=("dis", plugin_category),
    info={
        "header": "Distorting media",
        "usage": "{tr}dis <reply to media>",
    },
)
async def cat(event):
    "Reply this command to a video to convert it to distorted media"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if mediatype and mediatype not in ["Gif", "Video", "Sticker", "Photo", "Voice"]:
        return await edit_delete(event, "__Reply to a media file__")
    cat = await edit_or_reply(event, "__🎞Converting into distorted media..__")
    async with event.client.conversation("@distortionerbot") as conv:
        try:
            msg = await conv.send_message(reply)
            media = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
            if "Downloading" in media.raw_text:
                media = await conv.get_response()
        except YouBlockedUserError:
            await cat.edit("Please unblock @distortionerbot and try again")
            return
        await cat.delete()
        badcat = await event.client.send_file(event.chat_id, media, reply_to=reply)
        out = media_type(media)
        if out in ["Gif", "Video", "Sticker"]:
            await _catutils.unsavegif(event, badcat)
    await event.client.delete_messages(conv.chat_id, [msg.id, media.id])


@catub.cat_cmd(
    pattern="kiss(?:\s|$)([\s\S]*)",
    command=("kiss", plugin_category),
    info={
        "header": "Sends random kiss",
        "usage": [
            "{tr}kiss",
            "{tr}kiss <1-20>",
        ],
    },
)
async def kiss(event):
    """Its useless for single like you. Get a lover first"""
    inpt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    count = 1 if not inpt else int(inpt)
    if count < 0 and count > 20:
        await edit_delete(event, "`Give value in range 1-20`")
    res = base64.b64decode(
        "aHR0cHM6Ly90Lm1lL2pvaW5jaGF0L0NtZEEwVzYtSVVsbFpUUTk="
    ).decode("utf-8")
    resource = await event.client(GetFullChannelRequest(res))
    chat = resource.chats[0].username
    try:
        await event.client(
            functions.channels.GetParticipantRequest(
                channel=chat, participant=catub.uid
            )
        )
    except UserNotParticipantError:
        await event.client(Get(res.split("/")[4]))
        await event.client.edit_folder(resource.full_chat.id, 1)
        await event.client(
            functions.account.UpdateNotifySettingsRequest(
                peer=chat,
                settings=types.InputPeerNotifySettings(
                    show_previews=False,
                    silent=True,
                ),
            )
        )
    catevent = await edit_or_reply(event, "`Wait babe...`😘")
    maxmsg = await event.client.get_messages(chat)
    start = random.randint(31, maxmsg.total)
    start = min(start, maxmsg.total - 40)
    end = start + 41
    kiss = []
    async for x in event.client.iter_messages(
        chat, min_id=start, max_id=end, reverse=True
    ):
        try:
            if x.media and x.media.document.mime_type == "video/mp4":
                link = f"{res.split('j')[0]}{chat}/{x.id}"
                kiss.append(link)
        except AttributeError:
            pass
    kisss = random.sample(kiss, count)
    for i in kisss:
        nood = await event.client.send_file(event.chat_id, i, reply_to=reply_to_id)
        await _catutils.unsavegif(event, nood)
    await catevent.delete()
