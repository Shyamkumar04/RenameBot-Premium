import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6570438926:AAGCEdh2QEYjAr2sdlInagudO-RLe08KmlQ")

API_ID = int(os.environ.get("API_ID", "20244111"))

API_HASH = os.environ.get("API_HASH", "b76d27da2a4220fe109fe9ef0e866530")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
