from telethon import TelegramClient, events

api_id = 123456          # apna API ID yahan likhna
api_hash = "YOUR_API_HASH"   # apna API Hash yahan likhna

client = TelegramClient("my_session", api_id, api_hash)

@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping(event):
    await event.reply("Pong ✅")

print("Userbot started...")

client.start()
client.run_until_disconnected()
