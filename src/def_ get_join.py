import pandas as pd
import pyupbit
from upbitpy import Upbitpy

updater.dispatcher.add_handler(CommandHandler('get', get_command, pass_args=True))

def get_command(bot, update, args) :
    find = args[0]
    upbit = Upbitpy()
    check_find = "0"
    for ret in upbit.get_market_all() :
        if find == ret['korean_name'] :
            if "KRW" in ret['market'] :
                check_find = "1"
                ticker1 = upbit.get_ticker([ret['market']])
                reply_text = ret["korean_name"] + "의 업비트 원화 시세는 " + str(ticker1[0]['trade_price']) + "원 입니다."
                update.message.reply_text(reply_text)
    if check_find == "0" :
        update.message.reply_text(find + "는 업비트에 없습니다.")