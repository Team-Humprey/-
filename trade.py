import pyupbit
from Get_allassistant import get_assistant
import logging
import decimal
from GetItem import get_items
from class_coin_trade import coin_trade


min_order_amt = 5000

def start_buytrade(buy_amt, except_items):
    
    while True:
 
        logging.info("*********************************************************")
        logging.info("매수금액 : " + str(buy_amt))
        logging.info("매수 제외종목 : " + str(except_items))
        logging.info("*********************************************************")

        target_items = get_items('KRW', except_items)
 
        for target_item in target_items:
 
            rsi_val = False
            ocl_val = False
 
            logging.info('체크중....[' + str(target_item['market']) + ']')
 
            indicators_data = get_assistant(target_item['market'], 'D', 200, 5)

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
                available_amt = coin_trade.get_KRW()
                #['available_krw']
 
                if buy_amt == 'M':
                    buy_amt = available_amt

                if decimal(str(available_amt)) < decimal(str(buy_amt)):
                    logging.info('주문 가능금액[' + str(available_amt) + ']이 입력한 주문금액[' + str(buy_amt) + '] 보다 작습니다.')
                    continue

                if decimal(str(buy_amt)) < decimal(str(min_order_amt)):
                    logging.info('주문금액[' + str(buy_amt) + ']이 최소 주문금액[' + str(min_order_amt) + '] 보다 작습니다.')
                    continue
 
                logging.info('시장가 매수 시작! [' + str(target_item['market']) + ']')
                logging.info('시장가 매수 종료! [' + str(target_item['market']) + ']')

                if except_items.strip():
                    except_items = except_items + ',' + target_item['market'].split('-')[1]
                else:
                    except_items = target_item['market'].split('-')[1]