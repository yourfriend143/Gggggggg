import os

def get_int(name, default):
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return int(default)
    try:
        return int(value)
    except ValueError:
        return int(default)

def get_str(name, default=""):
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default
    return value

def get_list_of_ints(name, default):
    value = os.getenv(name)
    if value is None or value.strip() == "":
        value = default
    try:
        return list(map(int, value.split()))
    except ValueError:
        return list(map(int, default.split()))

API_ID = get_int("API_ID", 23283708)
API_HASH = get_str("API_HASH")
BOT_TOKEN = get_str("BOT_TOKEN")

CHANNEL_ID = get_int("CHANNEL_ID", -1002363362847)
OWNER_ID = get_list_of_ints("OWNER_ID", "6481888008")

FREEMIUM_LIMIT = get_int("FREEMIUM_LIMIT", 0)
PREMIUM_LIMIT = get_int("PREMIUM_LIMIT", 10000)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing!")

if not API_HASH:
    raise ValueError("API_HASH is missing!")
