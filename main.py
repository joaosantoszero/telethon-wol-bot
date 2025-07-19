from flask import Flask
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
import asyncio

app = Flask(__name__)

# 🔐 Suas credenciais (use variáveis de ambiente se quiser)
api_id = int(os.environ.get("API_ID"))  # ou direto: api_id = 26207366
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")
chat_id = os.environ.get("CHAT_ID")  # pode ser string ou int

# 🔌 Função reutilizável para enviar mensagem
async def enviar_comando(comando):
    async with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        await client.send_message(chat_id, comando)

@app.route('/ligar')
def ligar():
    asyncio.run(enviar_comando('/ligar'))
    return 'Comando /ligar enviado'

@app.route('/desligar')
def desligar():
    asyncio.run(enviar_comando('/desligar'))
    return 'Comando /desligar enviado'

@app.route('/')
def home():
    return 'Online. Use /ligar ou /desligar'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)  # ative o debug para ver futuros erros
