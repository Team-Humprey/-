import telegram
import class_load_data

def send_message(message):
  load_data = class_load_data.load_data()
  CHAT_ID = load_data.chat_id()
  CHAT_TOKEN = load_data.chat_token()
  bot = telegram.Bot(token=CHAT_TOKEN)
  bot.sendMessage(chat_id=CHAT_ID, text=message)
  return message

# 테스트코드
# print(send_message("test"))