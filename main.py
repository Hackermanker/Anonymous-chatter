import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
CHAT_ID = int(os.environ.get("CHAT_ID", 0))
USER_ID = int(os.environ.get("USER_ID", 0))

Bot = Client(
    "Anonymous-chatter",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

STAR_BUTTONS = [[
  InlineKeyboardButton("DEPLOY YOUR OWN", url="https://github/Hackermanker/Anonymous-chatter"),
  InlineKeyboardButton ("UPDATED CHANNEL", url="https://t.me/botupdatesastra")
]]

@Bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        text="Hello 👋 I am a simple anonymous admin bot for messaging in specific chats. You can also make a one like me",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )
     
@Bot.on_message(filters.private & filters.all & filters.user(USER_ID))
async def start(bot, update):
    await bot.send_message(CHAT_ID,update.text)
Bot.run()

    
    

