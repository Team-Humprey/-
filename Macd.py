import pandas as pd
import requests

def MACD(tradePrice):
    exp12 = tradePrice.ewm(span=12, adjust = False).mean()
    exp26 = tradePrice.ewm(span=26, adjust = False).mean()
    macd = exp12-exp26
    exp = macd.ewm(span=9, adjust = False).mean()
    return exp

if __name__ == "__main__":
    url = "https://api.upbit.com/v1/candles/days"
    querystring = {"market" : "KRW-BTC", "count" : "200"}
    
    response = requests.request("GET", url, params=querystring)
    
    data = response.json()
    
    df = pd.DataFrame(data)
    df = df.iloc[::-1]
    
    macd = MACD(df['trade_price'])
    print(macd[0])