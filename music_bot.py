from telethon import TelegramClient, events, Button    
import os    
    
api_id = 12688186    
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"    
bot_token = "8576876988:AAHPT7WAzo_I2N0-RLGZ840GBX91qfvv0lI"    
    
OWNER_ID_1 = 6744331332  # آیدی عددی اول    
OWNER_ID_2 = 7803165903  # آیدی عددی دوم    
    
client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)    
    
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
                [Button.text("🎵 اضافه کردن رسانه"), Button.text("حمله به ویسکال ☠")]    
            ]    
        )    
    else:    
        await event.reply(    
            "• شما به ربات اتکر زد ایکس [ Atkar ZX ] دسترسی ندارید برای دسترسی به @XMrAmer پیام دهید"    
        )    
    
@client.on(events.NewMessage)    
async def handle_buttons(event):    
    if event.sender_id not in [OWNER_ID_1, OWNER_ID_2]:    
        return    
    
    if event.text == "حمله به ویسکال ☠":    
        await event.reply("• لطفا لینک گروه را برای حمله به گروه ارسال کنید !")    
        
    elif event.text == "🎵 اضافه کردن رسانه":    
        await event.reply(    
            "• چه رسانه ای میخواهید برای پخش اضافه نمایید !؟",    
            buttons=[    
                [Button.text("🎵 آهنگ MP3"), Button.text("ویدئو MP4 🎥")]    
            ]    
        )    
        
    elif event.text == "🎵 آهنگ MP3":    
        await event.reply("• لطفا آهنگ 🎵 خود را با فرمت MP3 برای پخش در ویسکال ارسال کنید !")    
        
    elif event.text == "ویدئو MP4 🎥":    
        await event.reply("• لطفا ویدئو 🎥 خود را با فرمت MP4 برای پخش در ویسکال ارسال کنید !")    
    
print("Bot is running...")    
client.run_until_disconnected()
