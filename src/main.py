import class_coin_trade as class_ct

if __name__ == '__main__':
    ct = class_ct.coin_trade()
    #로그인 실패시 실행
    #ct.set_login_key("access key", "secret key")

    ct.set_coin_key("KRW-BTC")

    # 변동성 돌파 전략으로 봇 실행. BTC 한 종목 대상 전량 매수-매도
    ct.start_bot()