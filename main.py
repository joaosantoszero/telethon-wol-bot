from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread
import asyncio

# Dados do seu bot pessoal (que envia as mensagens)
api_id = 26207366
api_hash = "a9401a6884f6a5d79f82da6df74593ba"
session_str = "1AZWarzkBu4JrbaQUQ0z2s9DPt-yLcN2N5z64saO1aSZsrw5e16n18ehYzZ73DMX6KRoc2vnljMGja1Wyr4qRkmUbUzskwf_OcZSR7PG2ANfSdrgZL1PIOMiJ-IoZxJ8BlLXWtgr1OJ43ybkqB2Ly-g_JFz9Md84Ipe_fZDHTBNXYmr-5SJm5scIml3WeT2aYgFQLVcHa39LtDnqCIJ3voYvFuFulaJJrXFM46eRnvndY9tmBUByh0sOPG9gKqSUa-0iyFpNlPevulzQXrakzn7vG_kiqSfFajC03JsLu3MOdNOzWTtF1I9hUmkfMh8FObEcBVBSD0e3sflRdLcKvgxcKhXKR5T0="
TARGET_BOT_USERNAME = "PCControlJack1_bot"  # sem @

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

# Fake server com rotas reais para acionar os comandos
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot ativo via Render"

@app.route('/ligar')
def send_ligar():
    asyncio.create_task(client.send_message(TARGET_BOT_USERNAME, "/ligar"))
    return "Comando /ligar enviado."

@app.route('/desligar')
def send_desligar():
    asyncio.create_task(client.send_message(TARGET_BOT_USERNAME, "/desligar"))
    return "Comando /desligar enviado."

@app.route('/status')
def send_status():
    asyncio.create_task(client.send_message(TARGET_BOT_USERNAME, "/status"))
    return "Comando /status enviado."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Inicia o servidor Flask em segundo plano
flask_thread = Thread(target=run_flask)
flask_thread.start()

# Inicia o bot
client.start()
client.run_until_disconnected()
