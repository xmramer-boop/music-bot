from telethon import TelegramClient, events
import os

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"

OWNER_ID = 7803165903  # آیدی عددی تلگرام خودت

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

os.makedirs("music", exist_ok=True)

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("ربات موزیک روشنه ✅")

@client.on(events.NewMessage)
async def save_music(event):
    if event.sender_id != OWNER_ID:
        return

    if event.audio:
        file_path = await event.download_media(file="music/")
        await event.reply(f"فایل ذخیره شد ✅\n{file_path}")

print("Bot is running...")
client.run_until_disconnected()
