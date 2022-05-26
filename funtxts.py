import requests
from userbot import catub
from userbot.core.managers import edit_or_reply

plugin_category = "fun"


@catub.cat_cmd(
    pattern="tcat$",
    command=("tcat", plugin_category),
    info={
        "header": "Some random cat facial text art",
        "usage": "{tr}tcat",
    },
)
async def hmm(cat):
    "Some random cat facial text art"
    reactcat = requests.get("https://nekos.life/api/v2/cat").json()
    await edit_or_reply(cat, reactcat["cat"])


@catub.cat_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(cat):
    "Some random Funny questions"
    whycat = requests.get("https://nekos.life/api/v2/why").json()
    await edit_or_reply(cat, whycat["why"])


@catub.cat_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(cat):
    "Some random facts"
    factcat = requests.get("https://nekos.life/api/v2/fact").json()
    await edit_or_reply(cat, factcat["fact"])
