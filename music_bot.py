from telethon import TelegramClient, events, Button    
    
api_id = 12688186    
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"    
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"    
    
OWNER_ID_1 = 6744331332    
OWNER_ID_2 = 7803165903    
    
client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)    
    
@client.on(events.NewMessage(pattern="/start"))    
async def start(event):    
    if event.sender_id == OWNER_ID_1:    
        await event.reply(    
            "سلام علی رلکس 👑",    
            buttons=[    
                [Button.inline("🎵 اضافه کردن رسانه", b"media"),    
                 Button.inline("☠️ حمله به ویسکال", b"attack")]    
            ]    
        )    
    
    elif event.sender_id == OWNER_ID_2:    
        await event.reply(    
            "سلام ادمین 👑",    
            buttons=[    
                [Button.inline("🎵 رسانه", b"media"),    
                 Button.inline("☠️ حمله", b"attack"),    
                 Button.inline("➕ افزودن اتکر", b"add")]    
            ]    
        )    
    
    else:    
        await event.reply("دسترسی ندارید ❌")    
    
# کلیک روی دکمه‌ها    
@client.on(events.CallbackQuery)    
async def callbacks(event):    
    data = event.data.decode()    
    
    if data == "media":    
        await event.edit(    
            "انتخاب رسانه:",    
            buttons=[    
                [Button.inline("🎵 MP3", b"mp3"),    
                 Button.inline("🎥 MP4", b"mp4")]    
            ]    
        )    
    
    elif data == "attack":    
        await event.edit("لینک گروه را ارسال کنید 👇")    
    
    elif data == "add":    
        await event.edit("• برای افزودن اتکر شماره اکانت آن را برای ورود سشن وارد نمایید !")    
        response = await client.wait_for_new_message(event.chat_id)    
        phone_number = response.text    
    
        if phone_number.startswith("+98") and len(phone_number) == 13:    
            await client.send_code_request(phone_number)    
            await event.edit("• کد ارسال شده به شماره را برای تأیید وارد نمایید !")    
            response = await client.wait_for_new_message(event.chat_id)    
            verification_code = response.text    
    
            try:    
                await client.sign_in(phone_number, verification_code)    
                if client.is_user_authorized():    
                    await event.edit("✓ ورود موفقیت آمیز بود سشن شما با موفقیت ساخته شد !")    
                else:    
                    await event.edit("• پسورد اکانت را وارد نمایید !")    
                    response = await client.wait_for_new_message(event.chat_id)    
                    password = response.text    
                    await client.sign_in(phone_number, verification_code, password=password)    
                    await event.edit("✓ ورود موفقیت آمیز بود سشن شما با موفقیت ساخته شد !")    
            except Exception as e:    
                await event.edit(f"خطا در ورود: {str(e)}")    
        else:    
            await event.edit("• شماره وارد شده معتبر نیست. لطفا شماره صحیح را وارد کنید.")    
    
    elif data == "mp3":    
        await event.edit("آهنگ MP3 را ارسال کنید 🎵")    
    
    elif data == "mp4":    
        await event.edit("ویدیو MP4 را ارسال کنید 🎥")    
    
print("Bot is running...")    
client.run_until_disconnected()
