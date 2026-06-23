from telethon import TelegramClient, events

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("ربات موزیک روشنه ✅")

print("Bot is running...")
client.run_until_disconnected()