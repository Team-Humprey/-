import json

class  load_data:
  DATA_PATH = "../data/"
  with open(DATA_PATH + "bot-data.json", encoding="utf-8") as jsonBotData:
    botData = json.load(jsonBotData)
    # print(botData)            

  def chat_id(self):
    CHAT_ID = load_data.botData['chat']['id']
    return CHAT_ID 
  
  def chat_first_name(self):
    CHAT_FIRST_NAME = load_data.botData['chat']['first_name']
    return CHAT_FIRST_NAME 
  
  def chat_last_name(self):
    CHAT_LAST_NAME = load_data.botData['chat']['last_name']
    return CHAT_LAST_NAME 
  
  def chat_token(self):
    CHAT_TOKEN = load_data.botData['chat']['token']
    return CHAT_TOKEN 