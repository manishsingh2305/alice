import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24518841
API_HASH = "b7c1f8bf146188cd80c58541e4ed46c7"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8155616469:AAFOzPqbWoylW1Myc8vS8vYuFAQz1AYjnt0"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://manishbusiness2305:<REDARDO2305>@cluster0.bw67v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002416471139

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6829753965

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/manishsingh2305/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/+L0-E4XFnNlM0NTU1"
SUPPORT_GROUP = "https://t.me/+L0-E4XFnNlM0NTU1"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQF2ILkATq61aXLgcfP3mR9QX92_pJgTI5rzGQfcq2b2i70wijS7CNmRLuk1DrBSekAivb_pechKdDbRCTomJZxsfVv8nSRRUTyfdXTGOzC0IuyYM5h6OQWbTy0iAgbVuHz_A_wJ6nfbc-WC_cyo7QXtxs7imGZBdgZVS_mwoLIH74mgPvieRSpUT1lzYSDchrt2gr10xkM5NSFRLx0fBl2Vn1aDKfTQAN62-yQMczmC8KfORw-RDb93EmOAr1dpCiNEq1DscH4XUa-C42e7JJe-ZAErscOhA4NMsoinYETRct7kktVSNNnG6wkHuFkiA497KUKTbumemg-VgJa2OWeL_fO61gAAAAGXFcZtAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"

PING_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
STATS_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
STREAM_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6db77c76a81203df78556-47aae7f54844b99721.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
