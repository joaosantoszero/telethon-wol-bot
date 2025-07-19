from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

api_id = 26207366
api_hash = "a9401a6884f6a5d79f82da6df74593ba"
session_str = "1AZWarzkBu4JrbaQUQ0z2s9DPt-yLcN2N5z64saO1aSZsrw5e16n18ehYzZ73DMX6KRoc2vnljMGja1Wyr4qRkmUbUzskwf_OcZSR7PG2ANfSdrgZL1PIOMiJ-IoZxJ8BlLXWtgr1OJ43ybkqB2Ly-g_JFz9Md84Ipe_fZDHTBNXYmr-5SJm5scIml3WeT2aYgFQLVcHa39LtDnqCIJ3voYvFuFulaJJrXFM46eRnvndY9tmBUByh0sOPG9gKqSUa-0iyFpNlPevulzQXrakzn7vG_kiqSfFajC03JsLu3MOdNOzWTtF1I9hUmkfMh8FObEcBVBSD0e3sflRdLcKvgxcKhXKR5T0="

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(pattern="/ligar"))
async def ligar(event):
    await event.reply("⚙️ Enviando comando para ligar o PC...")

@client.on(events.NewMessage(pattern="/desligar"))
async def desligar(event):
    await event.reply("🛑 Enviando comando para desligar o PC...")

@client.on(events.NewMessage(pattern="/status"))
async def status(event):
    await event.reply("✅ Bot online, pronto para receber comandos.")

client.start()
client.run_until_disconnected()
