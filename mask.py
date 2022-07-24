# credits to @mrconfused and @sandy1709

import os

from telegraph import exceptions, upload_file
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from userbot import Convert, catub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.functions import delete_conv
from userbot.plugins import awooify, baguette, iphonex, lolice

plugin_category = "extra"


@catub.cat_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(event):
    "Hazmat suit maker"
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.media):
        return await edit_delete(event, "```Reply to a media file...```")
    chat = "@hazmat_suit_bot"
    output = await Convert.to_image(
        event, reply_message, dirct="./temp", file="mask.png", rgb=True
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    await edit_or_reply(output[0], "```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            flag = await conv.send_file(output[1])
        except YouBlockedUserError:
            await catub(unblock("hazmat_suit_bot"))
            flag = await conv.send_file(output[1])
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await output[0].delete()
        await event.client.send_file(
            event.chat_id,
            response,
            reply_to=reply_message,
        )
    await delete_conv(event, chat, flag)
    if os.path.exists(output[1]):
        os.remove(output[1])


@catub.cat_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def _(event):
    "replied Image will be face of other image"
    replied = await event.get_reply_message()
    if not (replied and replied.media):
        return await edit_or_reply(event, "Reply to a supported media file")
    output = await Convert.to_image(
        event,
        replied,
        dirct="./temp",
        file="awooify.png",
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    size = os.stat(output[1]).st_size
    if size > 5242880:
        os.remove(output[1])
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await edit_or_reply(output[0], "`Generating image..`")
    try:
        response = upload_file(output[1])
        os.remove(output[1])
    except exceptions.TelegraphException as exc:
        os.remove(output[1])
        return await edit_or_reply(output[0], f"ERROR: {str(exc)}")
    cat = f"https://telegra.ph{response[0]}"
    cat = await awooify(cat)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=replied)


@catub.cat_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def _(event):
    "replied Image will be face of other image"
    replied = await event.get_reply_message()
    if not (replied and replied.media):
        return await edit_or_reply(event, "Reply to a supported media file")
    output = await Convert.to_image(
        event,
        replied,
        dirct="./temp",
        file="lolice.png",
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    size = os.stat(output[1]).st_size
    if size > 5242880:
        os.remove(output[1])
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await edit_or_reply(output[0], "`Generating image..`")
    try:
        response = upload_file(output[1])
        os.remove(output[1])
    except exceptions.TelegraphException as exc:
        os.remove(output[1])
        return await edit_or_reply(output[0], f"ERROR: {str(exc)}")
    cat = f"https://telegra.ph{response[0]}"
    cat = await lolice(cat)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=replied)


@catub.cat_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def _(event):
    "replied Image will be face of other image"
    replied = await event.get_reply_message()
    if not (replied and replied.media):
        return await edit_or_reply(event, "Reply to a supported media file")
    output = await Convert.to_image(
        event,
        replied,
        dirct="./temp",
        file="bun.png",
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    size = os.stat(output[1]).st_size
    if size > 5242880:
        os.remove(output[1])
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await edit_or_reply(output[0], "`Generating image..`")
    try:
        response = upload_file(output[1])
        os.remove(output[1])
    except exceptions.TelegraphException as exc:
        os.remove(output[1])
        return await edit_or_reply(output[0], f"ERROR: {str(exc)}")
    cat = f"https://telegra.ph{response[0]}"
    cat = await baguette(cat)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=replied)


@catub.cat_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def _(event):
    "replied image as iphone x wallpaper."
    replied = await event.get_reply_message()
    if not (replied and replied.media):
        return await edit_or_reply(event, "Reply to a supported media file")
    output = await Convert.to_image(
        event,
        replied,
        dirct="./temp",
        file="iphx.png",
    )
    if output[1] is None:
        return await edit_delete(
            output[0], "__Unable to extract image from the replied message.__"
        )
    size = os.stat(output[1]).st_size
    if size > 5242880:
        os.remove(output[1])
        return await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
    await edit_or_reply(output[0], "`Generating image..`")
    try:
        response = upload_file(output[1])
        os.remove(output[1])
    except exceptions.TelegraphException as exc:
        os.remove(output[1])
        return await edit_or_reply(output[0], f"ERROR: {str(exc)}")
    cat = f"https://telegra.ph{response[0]}"
    cat = await iphonex(cat)
    await output[0].delete()
    await event.client.send_file(event.chat_id, cat, reply_to=replied)
