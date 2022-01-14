from os import name, uname_result
import requests
import pandas as pd
import time

def rsi(ohlc: pd.DataFrame, period: int = 14):
    ohlc["trade_price"] = ohlc["trade_price"]
    delta = ohlc["trade_price"].diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    declines[declines > 0] = 0
    
    _gain = gains.ewm(com=(period - 1), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period - 1), min_periods=period).mean()
    
    RS = _gain / _loss
    return pd.Series(100 - (100 / (1+RS)), name="RSI")

while True:
    url = "https://api.upbit.com/v1/candles/minutes/1"
    querystring = {"market":"KRW-XRP", "count":"200"}
    response = requests.request("GET", url, params=querystring)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.reindex(index=df.index[::-1]).reset_index()
    nrsi = rsi(df, 14).iloc[-1]
    print("현재 rsi : ", str(nrsi))
    time.sleep(1)