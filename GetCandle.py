from SendRequest import send_request

# target_item : 대상 종목
# tick_kind : 캔들 종류
# ing_range : 조회 범위

def get_candle(target_item, tick_kind, inq_range):

    # 분붕
    if tick_kind == "1" or tick_kind == "3" or tick_kind == "5" or tick_kind == "10" or tick_kind == "15" or tick_kind == "30" or tick_kind == "60" or tick_kind == "240":
        target_url = "minutes/" + tick_kind
    # 일봉
    elif tick_kind == "D":
        target_url = "days"
    # 주봉
    elif tick_kind == "W":
        target_url = "weeks"
    # 월봉
    elif tick_kind == "M":
        target_url = "months"
    # 잘못된 입력
    else:
        raise Exception("잘못된 틱 종류:" + str(tick_kind))
 
    querystring = {"market": target_item, "count": inq_range}
    res = send_request("GET", "https://api.upbit.com" + "/v1/candles/" + target_url, querystring, "")
    candle_data = res.json()
 
    return candle_data