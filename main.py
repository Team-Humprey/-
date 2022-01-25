import pyupbit
import logging
from trade import start_buytrade

if __name__ == '__main__':

    buy_amt = input("매수금액(M:최대, 10000:1만원) : ").upper()
    except_items = input("매수 제외종목(종목코드, ex:BTC,ETH) : ").upper()
 
    logging.info("*********************************************************")
    logging.info("매수금액 : " + str(buy_amt))
    logging.info("매수 제외종목 : " + str(except_items))
    logging.info("*********************************************************")

    start_buytrade(buy_amt, except_items)
 