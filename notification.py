import asyncio
import json
import telegram

# loading config file
with open("assets\\config.json") as f:
    config = json.load(f)
    
# getting messaging-configs from config
API_token = config["Telegram-API-token"]
cID = config["Telegram-Target-Chat"]

async def send(msg, chat_ID, token):
    bot = telegram.Bot(token=token)
    await bot.sendMessage(chat_id=chat_ID, text=msg)
    print("Message Sent!")


def notify_none_found():
    message = config["message-no-codes"]

    asyncio.run(send(msg=message, chat_ID=cID, token=API_token))

    return 0

def notify_new_codes(codes):
    message = config["message-new-codes-header"]

    for code in codes:
        message = message + config["message-new-codes-body"].format(code=code)

    asyncio.run(send(msg=message, chat_ID=cID, token=API_token))

    return 0