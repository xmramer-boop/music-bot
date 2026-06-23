from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

user_data = {}

@app.on_message(filters.command("start"))
def start(client, message):

    message.reply_text(
        "🎵 به ربات موزیک خوش آمدید",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🎵 رسانه", callback_data="media"),
                InlineKeyboardButton("☠ حمله به ویسکال", callback_data="vc")
            ]
        ])
    )


@app.on_callback_query()
def cb(client, query):

    if query.data == "media":
        query.message.edit_text(
            "🎵 انتخاب کن",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🎵 MP3", callback_data="mp3"),
                    InlineKeyboardButton("🎥 MP4", callback_data="mp4")
                ]
            ])
        )

    if query.data == "vc":
        query.message.edit_text("📎 لینک گروه را ارسال کن")
        user_data[query.from_user.id] = {"step": "link"}

    if query.data == "mp3":
        query.message.edit_text("🎵 فایل MP3 را ارسال کن")

    if query.data == "mp4":
        query.message.edit_text("🎥 فایل MP4 را ارسال کن")


@app.on_message(filters.text & ~filters.command("start"))
def handle(client, message):

    uid = message.from_user.id

    if uid in user_data and user_data[uid].get("step") == "link":
        user_data[uid]["link"] = message.text
        message.reply("✔ لینک ذخیره شد. الان فایل موزیک رو بفرست")

        user_data[uid]["step"] = "file"


print("Bot running...")
app.run()
