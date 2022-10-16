from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = ""
API_HASH = ""
BOT_TOKEN = ""


ROGUE = Client(
    name="Anonymous-chatter",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_BUTTONS = [[
  InlineKeyboardButton("ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ", url="t.me/botupdatesastra")
]]

@ROGUE.on_message(filters.command("start"))
async def start_cmd(client,message):
    await message.reply_photo(
        photo="https://te.legra.ph/file/05a3e40fa06809b07abd4.jpg",
        caption="Hello guyzz i m just a testing machine of unwanted things",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )

@ROGUE.on_message(filters.command("about"))
async def about_cmd(client,message):
    await message.reply_text("Bot status")
    


print("Bot Started")

ROGUE.run()



    
    

