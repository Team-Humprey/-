import time 
import pyupbit
import pandas as pd
import datetime
import os

class coin_trade:
    # 생성자
    def __init__(self):
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