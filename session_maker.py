from pyrogram import Client

api_id = 12688186
api_hash = "0cdd3e314b5a5487d2c99bbdc7afd450"

app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash
)

app.run()
