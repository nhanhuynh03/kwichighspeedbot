# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID','10803244'))
    API_HASH = str(getenv('API_HASH','66011f96ce4ead7208d6b0afd0519170'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','5614282668:AAFjoIVptHabtgdSMzGBncUzMaJ0qO9xIC8'))
    name = str(getenv('SESSION_NAME', 'NhanGenerator'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001600150522'
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1653476825").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME','@NhanGenerator_Bot'))
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://Nhanhuynh:test@cluster0.velka01.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL','nhangenerator'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS")).split())) 
