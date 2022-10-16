import os
from pyrogram import Client, filters
CHAT_ID = int(os.environ.get("CHAT_ID", 0))
USER_ID = int(os.environ.get("USER_ID", 0))
Bot = Client(
    "Anonymous-chatter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """ `Hai {}, 
Am a Anonymous messagin bot Bot You can use me to chat as an anonymous admin . 
Use /help For knowing more.`
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Updates', url=f"https://telegram.me/botupdatesastra"), 
        InlineKeyboardButton('Deploy your own', url=f"https://GitHub.com/Hackermanker/Anonymous-chatter"),
        ]]
    )
@Bot.on_message(filters.private & filters.all & filters.user(USER_ID))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)
Bot.run()

    
    

