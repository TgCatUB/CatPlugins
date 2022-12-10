import requests
from userbot.core.managers import edit_or_reply

pawn = [
    "nsfw",
    "nsfw_gifs",
    "nsfw_gif",
    "realgirls",
    "porn",
    "porn_gifs",
    "porninfifteenseconds",
    "CuteModeSlutMode",
    "NSFW_HTML5",
    "besthqporngifs",
    "boobs",
    "pussy",
    "jigglefuck",
    "GirlsFinishingTheJob",
    "SheLikesItRough",
    "dirtysmall",
    "NsfwGifsMonster",
    "RedheadGifs",
    "IndianPorn",
    "DesiBoners",
    "IndianBabes",
    "Mmsvideos",
    "snapleaks",
    "creampie",
    "creampies",
    "workgonewild",
    "militarygonewild",
    "BustyPetite",
    "cumsluts",
    "HappyEmbarrassedGirls",
    "suicidegirls",
    "porninaminute",
    "SexInFrontOfOthers",
    "tiktoknsfw",
    "tiktokporn",
    "TikThots",
    "NSFWFunny",
    "GWNerdy",
    "WatchItForThePlot",
    "HoldTheMoan",
    "OnOff",
    "TittyDrop",
    "extramile",
    "adorableporn",
]

endpoints = {
    "v1": {
        "end": [
            "pussy",
            "cum",
            "boobs",
            "bj",
            "anal",
            "hentai",
            "feet",
            "blowjob",
            "poke",
            "holo",
            "baka",
        ],
        "api": "http://api.nekos.fun:8080/api/",
        "checker": "image",
    },
    "v2": {
        "end": [
            "lewd",
            "spank",
            "gasm",
            "tickle",
            "slap",
            "pat",
            "neko",
            "meow",
            "lizard",
            "kiss",
            "hug",
            "fox_girl",
            "feed",
            "cuddle",
            "ngif",
            "smug",
            "woof",
            "wallpaper",
            "goose",
            "gecg",
            "avatar",
            "waifu",
        ],
        "api": "https://nekos.life/api/v2/img/",
        "checker": "url",
    },
}


def nekos(endpoint=None, endpoints=endpoints):
    if endpoint:
        for i in endpoints:
            if endpoint in endpoints[i]["end"]:
                api = endpoints[i]["api"]
                checker = endpoints[i]["checker"]
        result = requests.get(api + endpoint).json()
        return result[checker]
    return (
        endpoints["v1"]["end"]
        + endpoints["v2"]["end"]
        + endpoints["v3"]["end"]
        + endpoints["v4"]["end"]
    )


async def importent(event):
    cat = ["-1001199597035", "-1001459701099", "-1001436155389", "-1001321431101"]
    if str(event.chat_id) in cat:
        await edit_or_reply(event, "**Yes I'm GAY**")
        await event.client.kick_participant(event.chat_id, "me")
        return True
    return False


def nsfw(catagory):
    catagory.sort(key=str.casefold)
    horny = "**Catagory :** "
    for i in catagory:
        horny += f" `{i.lower()}` |"
    return horny


API = "https://catmemeapi2023.herokuapp.com/gimme"


"""
#Blame Heroku

"v3": {
    "end": [
        "ass",
        "bdsm",
        "boobjob",
        "creampie",
        "cuckold",
        "elves",
        "ero",
        "femdom",
        "foot",
        "gangbang",
        "glasses",
        "incest",
        "manga",
        "masturbation",
        "nsfwMobileWallpaper",
        "orgy",
        "public",
        "tentacles",
        "thighs",
        "uniform",
        "vagina",
        "yuri",
        "zettaiRyouiki",
    ],
    "api": "https://hmtai.herokuapp.com/nsfw/",
    "checker": "url",
},
"v4": {
    "end": ["doujin", "gifs", "netorare", "maid", "panties", "school", "succubus"],
    "api": "https://akaneko-api.herokuapp.com/api/",
    "checker": "url",
},
"""