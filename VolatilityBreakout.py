#변동성 돌파 전략
#1) 가격 변동폭 계산: 투자하려는 가상화폐의 전일 고가(high)에서 전일 저가(low)를 빼서 가상화폐의 가격 변동폭을 구함.
#2) 매수 기준: 당일 시간에서 (변동폭 * 0.5) 이상 상승하면 해당 가격에 바로 매수
#3) 매도 기준: 당일 종가에 매도

import time
import pyupbit
import datetime

def get_target_price(ticker):
     df = pyupbit.get_ohlcv(ticker)
     yesterday = df.iloc[-2]
 
     today_open = yesterday['close']
     yesterday_high = yesterday['high']
     yesterday_low = yesterday['low']
     target = today_open + (yesterday_high - yesterday_low) * 0.5
     return target
 
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("BTC")
 
while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10) : 
        target_price = get_target_price("BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
 
    current_price = pyupbit.get_current_price("BTC")
    print(current_price)
 
    time.sleep(1)