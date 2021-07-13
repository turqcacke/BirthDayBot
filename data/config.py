from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

assert BOT_TOKEN
