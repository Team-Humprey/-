import class_coin_trade as class_ct
#import telegram

ct = class_ct.coin_trade()
#로그인 실패시 실행
#ct.set_login_key("access key", "secret key")

ct.set_coin_key("KRW-BTC")
ct.start_bot()

ct.start_rsi_bot(10000, "BTC")
