import pandas as pd

def get_macd(candle_datas, loop_cnt):
    macd_list = []
 
    df = pd.DataFrame(candle_datas[0])
    df = df.iloc[::-1]
    df = df['trade_price']

    exp1 = df.ewm(span=12, adjust=False).mean()
    exp2 = df.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()
 
    for i in range(0, int(loop_cnt)):
        macd_list.append(
            {"type": "MACD", "DT": candle_datas[0][i]['candle_date_time_kst'], "MACD": round(macd[i], 4),
            "SIGNAL": round(exp3[i], 4),
            "OCL": round(macd[i] - exp3[i], 4)})
 
    return macd_list