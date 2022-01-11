import telegram
import class_load_data

from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class telegram_bot:
  # 클래스 생성자
  def __init__(self):
    self.load_data = class_load_data.load_data()
    self.CHAT_ID = self.load_data.chat_id()
    self.CHAT_TOKEN = self.load_data.chat_token()
    self.bot = telegram.Bot(token=self.CHAT_TOKEN)
    self.updater = Updater(token=self.CHAT_TOKEN, use_context=True)
    self.dispatcher = self.updater.dispatcher
  
  # 메시지 전송 함수
  def send_telegram_message(self, message):
    self.bot.sendMessage(chat_id=self.CHAT_ID, text=message)

  # 봇 시작 함수
  def start_bot(self, update, context):
    self.send_telegram_message("봇 작동 시작")

  # 봇 종료 함수
  def stop_bot(self, update, context):
    self.send_telegram_message("봇 작동 종료")

  # 비트코인의 현재 가격을 알려주는 메시지

  # 

  # CommandHandler 생성 함수
  def handler_initialize(self):
    # handler 정의
    self.start_handler = CommandHandler('start', self.start_bot)
    self.stop_handler = CommandHandler('stop', self.stop_bot)
    # handler 추가
    self.dispatcher.add_handler(self.start_handler)
    self.dispatcher.add_handler(self.stop_handler)

# 클래스 작동 테스트
# Bot=telegram_bot()
# Bot.handler_initialize()

# Bot.updater.start_polling()
# Bot.updater.idle()