from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID""21209802"))
API_HASH = getenv("API_HASH""eed1c8387c6ee80009527e07d9d58cc0")

BOT_TOKEN = getenv("BOT_TOKEN", "6807629743:AAHsnFL_eb9F-egK2yjvvxVgKWIcQIhpNDA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3500"))

OWNER_ID = int(getenv("OWNER_ID""6716174264"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/t_t_t_h")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/t_t_t_h")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6716174264").split()))


FAILED = "https://graph.org/file/8882cbd7cc786826d9ecb.jpg"
