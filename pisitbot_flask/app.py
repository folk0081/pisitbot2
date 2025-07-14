
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Bot is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook:", data)
    return {"status": "ok"}
