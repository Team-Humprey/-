import time
import pyupbit
from collections import deque

#주문은 초당 8회, 분당 200회 / 주문 외 요청은 초당 30회, 분당 900회 사용 가능

tickers = []
ma20 = deque(maxlen=20)
ma60 = deque(maxlen=60)
ma120 = deque(maxlen=120)

tickers = pyupbit.get_tickers(fiat="KRW")

# 이동평균선 
def get_ticker_ma(ticker):  

    df = pyupbit.get_ohlcv(ticker, interval='day') 

    ma20.extend(df['close'])    
    ma60.extend(df['close'])    
    ma120.extend(df['close'])   

    curr_ma20 = sum(ma20) / len(ma20)  #20일선 이동평균
    curr_ma60 = sum(ma60) / len(ma60)  #60일선 이동평균
    curr_ma120 = sum(ma120) / len(ma120)   #120일선 이동평균   

    print(f'코인 심볼: {ticker}     이동 평균(20): {round(curr_ma20,2)}, 이동 평균(60): {round(curr_ma60,2)}, 이동 평균(120): {round(curr_ma120,2)}') 

while True:    
    try:        
        for tk in tickers:            
            get_ticker_ma(tk)
            time.sleep(2)
    except:
        print('오류 발생 무시')
        pass