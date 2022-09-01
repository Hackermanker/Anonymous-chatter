from pyrogram import Client, filters

API_ID = "10872318"
API_HASH = "d4582d8cdb1e41a2df51e404940d6e8f"
BOT_TOKEN = "5778268282:AAEn-Y8xKw86jHp-lzkwtfZbNUmFxj-q0Sk"


ROGUE = Client(
    name="RogueBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot Started")

ROGUE.run()



    
    

