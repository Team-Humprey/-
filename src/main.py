import class_coin_trade as class_ct
import class_telegram_bot as class_tb

ct = class_ct.coin_trade()
#로그인 실패시 실행
#ct.set_login_key("access key", "secret key")

telegram = class_tb.telegram_bot()
telegram.send_telegram_message("아이디 변경 완료")


ct.set_coin_key("KRW-BTC")

# 변동성 돌파 전략으로 봇 실행. BTC 한 종목 대상 전량 매수-매도
ct.start_bot()

# rsi 전략으로 봇 실행 특정 종목 제외 후 나머지 대상 전체에 대한 매수-매도
ct.start_rsi_bot(10000, "BTC")
