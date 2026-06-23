from telethon import TelegramClient, events, Button

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"

OWNER_ID_1 = 6744331332
OWNER_ID_2 = 7803165903

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

# حالت مکالمه (برای گرفتن شماره و کد)
user_state = {}

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.sender_id == OWNER_ID_1:
        await event.reply(
            "• درود **علی رلکس** مالک اتحادیه [ @NEGAN_RELX ] به ربات اتکر زد ایکس خوش آمدید لطفا از منوی زیر انتخاب نمایید !",
            buttons=[
                [Button.text("🎵 اضافه کردن رسانه"), Button.text("حمله به ویسکال ☠")]
            ]
        )

    elif event.sender_id == OWNER_ID_2:
        await event.reply(
            "• درود مالک گرامی [ @XMrAmer ] به ربات ZX خوش آمدید از منوی زیر کار خود را انتخاب کنید !",
            buttons=[
                [Button.text("🎵 اضافه کردن رسانه"), Button.text("حمله به ویسکال ☠"), Button.text("➕ افزودن اتکر ☠️")]
            ]
        )

    else:
        await event.reply("• شما به ربات اتکر زد ایکس دسترسی ندارید برای دسترسی به @XMrAmer پیام دهید")


@client.on(events.NewMessage)
async def handle(event):
    if event.sender_id not in [OWNER_ID_1, OWNER_ID_2]:
        return

    user_id = event.sender_id
    text = event.raw_text

    # مرحله شروع ساخت سشن
    if text == "➕ افزودن اتکر ☠️":
        user_state[user_id] = {"step": "phone"}
        await event.reply("• برای افزودن اتکر شماره اکانت را وارد کنید:")

    # گرفتن شماره
    elif user_state.get(user_id, {}).get("step") == "phone":
        user_state[user_id]["phone"] = text
        user_state[user_id]["step"] = "code"

        try:
            await client.send_code_request(text)
            await event.reply("• کد ارسال شد، لطفا کد تایید را وارد کنید:")
        except Exception as e:
            await event.reply(f"خطا در ارسال کد: {str(e)}")
            user_state.pop(user_id, None)

    # گرفتن کد
    elif user_state.get(user_id, {}).get("step") == "code":
        phone = user_state[user_id]["phone"]
        code = text

        try:
            await client.sign_in(phone, code)

            await event.reply("✓ ورود موفقیت آمیز بود سشن ساخته شد!")
            user_state.pop(user_id, None)

        except Exception as e:
            await event.reply(f"خطا در ورود: {str(e)}")
            user_state.pop(user_id, None)

    # بخش رسانه (همون قبلی خودت)
    elif text == "حمله به ویسکال ☠":
        await event.reply("• لطفا لینک گروه را ارسال کنید !")

    elif text == "🎵 اضافه کردن رسانه":
        await event.reply(
            "• چه رسانه ای میخواهید اضافه نمایید !؟",
            buttons=[
                [Button.text("🎵 آهنگ MP3"), Button.text("ویدئو MP4 🎥")]
            ]
        )

    elif text == "🎵 آهنگ MP3":
        await event.reply("• آهنگ MP3 را ارسال کنید !")

    elif text == "ویدئو MP4 🎥":
        await event.reply("• ویدئو MP4 را ارسال کنید !")


print("Bot is running...")
client.run_until_disconnected()
