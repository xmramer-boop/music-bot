from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
vc = PyTgCalls(app)

music = None

@app.on_message(filters.command("start"))
def start(_, msg):
    msg.reply("🎵 ربات روشنه")

@app.on_message(filters.audio)
async def save_music(_, msg):
    global music
    music = await msg.download()
    await msg.reply("✅ موزیک ذخیره شد")

@app.on_message(filters.command("play"))
async def play(_, msg):
    global music
    if not music:
        return await msg.reply("اول موزیک بفرست")

    await vc.join_group_call(msg.chat.id, AudioPiped(music))
    await msg.reply("🎶 در حال پخش")

app.start()
vc.start()
print("RUNNING")
