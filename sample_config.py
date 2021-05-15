import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("1761268656:AAEBAjQnqxP-B5WtbaaZNjUJ5cv_WTaqqr8", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("3142204", 12345))
    API_HASH = os.environ.get("0d9edde42afce632a54d55b22fb9b56f", "")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("994938597", "").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Sql Database url
    DB_URI = os.environ.get("mongodb+srv://01571195489s:01571195489s@cluster0.zkfcd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", "")
    
