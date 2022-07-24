"""
Created by @Jisan7509
plugin for Cat_Userbot
☝☝☝
You remove this, you gay.
"""
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from userbot import Convert, catub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.functions import clippy, delete_conv
from userbot.helpers.utils import reply_id
from userbot.plugins import mention

plugin_category = "extra"


@catub.cat_cmd(
    pattern="iascii ?([\s\S]*)",
    command=("iascii", plugin_category),
    info={
        "header": "Convert media to ascii art.",
        "description": "Reply to any media files like pic, gif, sticker, video and it will convert into ascii.",
        "usage": [
            "{tr}iascii <reply to a media>",
        ],
    },
)
async def bad(event):
    "Make a media to ascii art"
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.media):
        return await edit_delete(event, "```Reply to a media file...```")
    c_id = await reply_id(event)
    chat = "@asciiart_bot"
    output = await Convert.to_image(event, reply_message, rgb=True)
    if not output[1]:
        return await edit_delete(output[0], "`Unable to convert this media..`")
    kakashi = await edit_or_reply(output[0], "```Wait making ASCII...```")
    async with event.client.conversation(chat) as conv:
        try:
            flag = await conv.send_message("/start")
        except YouBlockedUserError:
            await catub(unblock("asciiart_bot"))
            flag = await conv.send_message("/start")
        await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await conv.send_file(output[1])
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            response,
            reply_to=c_id,
            caption=f"**➥ Image Type :** ASCII Art\n**➥ Uploaded By :** {mention}",
        )
    await delete_conv(event, chat, flag)
    if os.path.exists(output[1]):
        os.remove(output[1])


@catub.cat_cmd(
    pattern="line ?([\s\S]*)",
    command=("line", plugin_category),
    info={
        "header": "Convert media to line image.",
        "description": "Reply to any media files like pic, gif, sticker, video and it will convert into line image.",
        "usage": [
            "{tr}line <reply to a media>",
        ],
    },
)
async def pussy(event):
    "Make a media to line image"
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.media):
        return await edit_delete(event, "```Reply to a media file...```")
    c_id = await reply_id(event)
    chat = "@Lines50Bot"
    output = await Convert.to_image(event, reply_message, rgb=True)
    if not output[1]:
        return await edit_delete(output[0], "`Unable to convert this media..`")
    kakashi = await edit_or_reply(output[0], "```Wait making Line art...```")
    async with event.client.conversation(chat) as conv:
        try:
            flag = await conv.send_message("/start")
        except YouBlockedUserError:
            await catub(unblock("Lines50Bot"))
            flag = await conv.send_message("/start")
        await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await conv.send_file(output[1])
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            response,
            reply_to=c_id,
            caption=f"**➥ Image Type :** LINE Art \n**➥ Uploaded By :** {mention}",
        )
    await delete_conv(event, chat, flag)
    if os.path.exists(output[1]):
        os.remove(output[1])


@catub.cat_cmd(
    pattern="clip ?([\s\S]*)",
    command=("clip", plugin_category),
    info={
        "header": "Convert media to sticker by clippy",
        "description": "Reply to any media files like pic, gif, sticker, video and it will convert into sticker by clippy.",
        "usage": [
            "{tr}clip <reply to a media>",
        ],
    },
)
async def cat(event):
    "Make a media to clippy sticker"
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.media):
        return await edit_delete(event, "```Reply to a media file...```")
    cat = await edit_or_reply(event, "```Processing...```")
    c_id = await reply_id(event)
    output = await Convert.to_image(event, reply_message, noedits=True)
    if not output[1]:
        return await edit_delete(output[0], "`Unable to convert this media..`")
    await cat.delete()
    await clippy(event.client, output[1], event.chat_id, c_id)
    if os.path.exists(output[1]):
        os.remove(output[1])
