from flask import Flask
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

app = Flask(__name__)

# 🔧 Coloque aqui suas credenciais
api_id = 26207366
api_hash = "a9401a6884f6a5d79f82da6df74593ba"
session_string = "1AZWarzkBu4JrbaQUQ0z2s9DPt-yLcN2N5z64saO1aSZsrw5e16n18ehYzZ73DMX6KRoc2vnljMGja1Wyr4qRkmUbUzskwf_OcZSR7PG2ANfSdrgZL1PIOMiJ-IoZxJ8BlLXWtgr1OJ43ybkqB2Ly-g_JFz9Md84Ipe_fZDHTBNXYmr-5SJm5scIml3WeT2aYgFQLVcHa39LtDnqCIJ3voYvFuFulaJJrXFM46eRnvndY9tmBUByh0sOPG9gKqSUa-0iyFpNlPevulzQXrakzn7vG_kiqSfFajC03JsLu3MOdNOzWTtF1I9hUmkfMh8FObEcBVBSD0e3sflRdLcKvgxcKhXKR5T0="
chat_id = "8166163944"  # ou ID numérico do bot

@app.route('/ligar')
def ligar():
    with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        client.send_message(chat_id, '/ligar')
    return 'Comando /ligar enviado'

@app.route('/desligar')
def desligar():
    with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        client.send_message(chat_id, '/desligar')
    return 'Comando /desligar enviado'

@app.route('/')
def home():
    return 'Online. Use /ligar ou /desligar'

if __name__ == '__main__':
    app.run()
