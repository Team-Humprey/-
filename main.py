import pyupbit
import logging
from trade import start_buytrade

if __name__ == '__main__':

    rsi_buy_value = input("매수 기준 RSI 값(ex. 30):")
    rsi_sell_value = input("매도 기준 RSI 값(ex. 70):")
    buy_amt = input("매수금액(ex:10000):")
 
    logging.info("매수 기준 RSI 값:" + str(rsi_buy_value))
    logging.info("매도 기준 RSI 값:" + str(rsi_sell_value))
    logging.info("매수금액:" + str(buy_amt))

    start_buytrade(rsi_buy_value, rsi_sell_value, buy_amt)
 