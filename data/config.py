from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
CHANNEL = env.str('CHANNEL')

DB_NAME = 'db.sqlite3'
BASE_DIR = Path(__file__).parent.parent
TIME_ZONE = 'Asia/Tashkent'

assert BOT_TOKEN and CHANNEL

