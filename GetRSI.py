import pandas as pd;

def get_rsi(candle_datas):
    rsi_data = []
    for candle_data_for in candle_datas:
 
        df = pd.DataFrame(candle_data_for)
        dfDt = df['candle_date_time_kst'].iloc[::-1]
        df = df.reindex(index=df.index[::-1]).reset_index()
 
        df['close'] = df["trade_price"]

        def rsi(ohlc: pd.DataFrame, period: int = 14):
            ohlc["close"] = ohlc["close"]
            delta = ohlc["close"].diff()
 
            up, down = delta.copy(), delta.copy()
            up[up < 0] = 0
            down[down > 0] = 0
 
            _gain = up.ewm(com=(period - 1), min_periods=period).mean()
            _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
 
            RS = _gain / _loss
            return pd.Series(100 - (100 / (1 + RS)), name="RSI")
 
        rsi = round(rsi(df, 14).iloc[-1], 4)
        rsi_data.append({"type": "RSI", "DT": dfDt[0], "RSI": rsi})
 
    return rsi_data