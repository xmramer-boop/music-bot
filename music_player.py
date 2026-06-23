from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from pyrogram import Client

api_id = 12688186
api_hash = "YOUR_HASH"

user = Client("session", api_id=api_id, api_hash=api_hash)

vc = PyTgCalls(user)

async def play(chat_id, file):
    await vc.join_group_call(
        chat_id,
        AudioPiped(file)
    )
