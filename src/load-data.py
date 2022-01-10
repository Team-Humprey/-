import json

DATA_PATH = "../data/"

def load_data():
  with open(DATA_PATH + "bot-data.json", encoding="utf-8") as jsonBotData:
    botData = json.load(jsonBotData)
    print(botData)

  CHAT_ID = botData['chat']['id']
  CHAT_FIRST_NAME = botData['chat']['first_name']
  CHAT_LAST_NAME = botData['chat']['last_name']
  CHAT_TOKEN = botData['chat']['token']
  
  return CHAT_ID, CHAT_FIRST_NAME, CHAT_LAST_NAME, CHAT_TOKEN