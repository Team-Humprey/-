import time 
import pyupbit
import pandas as pd
import datetime
import os

from Get_allassistant import get_assistant
import logging
import decimal
from GetItem import get_items

class coin_trade:
    # 생성자
    def __init__(self):
        self.coinKey = "KRW-BTC"
        try:
            access = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
            secret = os.environ['UPBIT_OPEN_API_SECRET_KEY']
            self.login = pyupbit.Upbit(access, secret)
        except:
            print("환경변수오류. 환경변수를 바꾸고 다시 실행하거나 set_login_key()를 실행해주세요")    
        try:
            balance_df = pd.DataFrame(self.login.get_balances()) # 암호화폐 잔고 조회
            print(balance_df) 
        except:
            print("로그인 오류. set_login_key를 다시 해주세요")

    # 로그인 실패시 새로운 키 설정
    def set_login_key(self, accessKey, secretKey):
        access = accessKey
        secret = secretKey
        self.login = pyupbit.Upbit(access, secret)
        try:
            balance_df = pd.DataFrame(self.login.get_balances()) # 암호화폐 잔고 조회
            print(balance_df) 
            return 0
        except:
            print("로그인 오류. set_login_key를 다시 해주세요")
            return 1

    # 코인 종목 변경. 디폴트는 KRW-BTC (비트코인)
    def set_coin_key(self, coinName):
        self.coinKey = coinName


    # 잔고 조회
    def get_balance(self, ticker):
        balances = self.login.get_balances()
        for b in balances:
            if b['currency'] == ticker:
                if b['balance'] is not None:
                    return float(b['balance'])
                else:
                    return 0
        return 0

    # 한화 잔고 조회   
    def get_KRW(self):
        return self.get_balance("KRW")

    # 간단한 변동성 돌파 전략으로 매수 목표가 조회
    def get_target_price(self, k):
        ticker = self.coinKey
        df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
        target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
        return target_price

    # 시작 시간 조회
    def get_start_time(self):
        ticker = self.coinKey
        df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
        start_time = df.index[0]
        return start_time

    
    # 현재가 조회
    def get_current_price(self):
        ticker = self.coinKey
        return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

    # 코인 사기 (가격)
    def buy_coin(self, price):
        self.login.buy_market_order(self.coinKey, price)

    # 코인 팔기 (가격)
    def sell_coin(self, price):
        self.login.buy_market_order(self.coinKey, price)

    # 간단한 봇 예시
    def start_bot(self):
            
        while True:
            try:
                now = datetime.datetime.now()
                start_time = self.get_start_time()
                end_time = start_time + datetime.timedelta(days=1)

                if start_time < now < end_time - datetime.timedelta(seconds=10):
                    target_price = self.get_target_price(0.5)
                    current_price = self.get_current_price()
                    if target_price < current_price:
                        krw = self.get_KRW()
                        if krw > 5000:
                            self.buy_coin(krw*0.9995)
                            print("bought", self.coinKey,"with", krw*0.9995 )
                else:
                    btc = self.get_balance("BTC")
                    if btc > 0.00008:
                        self.sell_coin(btc*0.9995)
                        print("selled", self.coinKey,"for", btc*0.9995 )
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(1)

    def start_rsi_bot(self, buy_amt, except_items):
        while True:
            logging.info("*********************************************************")
            logging.info("매수금액 : " + str(buy_amt))
            logging.info("매수 제외종목 : " + str(except_items))
            logging.info("*********************************************************")

            target_items = pyupbit.get_items('KRW', except_items)
    
            for target_item in target_items:
    
                rsi_val = False
                ocl_val = False
    
                logging.info('체크중....[' + str(target_item['market']) + ']')
    
                indicators_data = pyupbit.get_assistant(target_item['market'], 'D', 200, 5)

                if len(indicators_data) < 5:
                    logging.info('캔들 데이터 부족으로 매수 대상에서 제외....[' + str(target_item['market']) + ']')
                    continue

                if (decimal(str(indicators_data[0][0]['RSI'])) > decimal(str(indicators_data[0][1]['RSI']))
                    and decimal(str(indicators_data[0][1]['RSI'])) > decimal(str(indicators_data[0][2]['RSI']))
                    and decimal(str(indicators_data[0][3]['RSI'])) > decimal(str(indicators_data[0][2]['RSI']))
                    and decimal(str(indicators_data[0][2]['RSI'])) < decimal(str(30))):
                    rsi_val = True
    
                if (decimal(str(indicators_data[2][0]['OCL'])) > decimal(str(indicators_data[2][1]['OCL']))
                    and decimal(str(indicators_data[2][1]['OCL'])) > decimal(str(indicators_data[2][2]['OCL']))
                    and decimal(str(indicators_data[2][3]['OCL'])) > decimal(str(indicators_data[2][2]['OCL']))
                    and decimal(str(indicators_data[2][1]['OCL'])) < decimal(str(0))
                    and decimal(str(indicators_data[2][2]['OCL'])) < decimal(str(0))
                    and decimal(str(indicators_data[2][3]['OCL'])) < decimal(str(0))):
                    ocl_val = True

                if rsi_val and ocl_val:
                    logging.info('매수대상 발견....[' + str(target_item['market']) + ']')
                    logging.info(indicators_data[0])
                    logging.info(indicators_data[1])
                    logging.info(indicators_data[2])
    
                    # 잔고조회
                    available_amt = pyupbit.get_krwbal()['available_krw']
    
                    if buy_amt == 'M':
                        buy_amt = available_amt

                    if decimal(str(available_amt)) < decimal(str(buy_amt)):
                        logging.info('주문 가능금액[' + str(available_amt) + ']이 입력한 주문금액[' + str(buy_amt) + '] 보다 작습니다.')
                        continue

                    if decimal(str(buy_amt)) < decimal(str(pyupbit.min_order_amt)):
                        logging.info('주문금액[' + str(buy_amt) + ']이 최소 주문금액[' + str(pyupbit.min_order_amt) + '] 보다 작습니다.')
                        continue
    
                    logging.info('시장가 매수 시작! [' + str(target_item['market']) + ']')
                    #rtn_buycoin_mp = upbit.buycoin_mp(target_item['market'], buy_amt)
                    logging.info('시장가 매수 종료! [' + str(target_item['market']) + ']')
                    #logging.info(rtn_buycoin_mp)

                    if except_items.strip():
                        except_items = except_items + ',' + target_item['market'].split('-')[1]
                    else:
                        except_items = target_item['market'].split('-')[1]