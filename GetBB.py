from GetCandle import get_candle
import numpy
import pandas as pd

def get_bb(candle_datas):

    bb_list = []
 
    for candle_data_for in candle_datas:
        df = pd.DataFrame(candle_data_for)
        dfDt = df['candle_date_time_kst'].iloc[::-1]
        df = df['trade_price'].iloc[::-1]

        unit = 2
 
        band1 = unit * numpy.std(df[len(df) - 20:len(df)])
        bb_center = numpy.mean(df[len(df) - 20:len(df)])
        band_high = bb_center + band1
        band_low = bb_center - band1
 
        bb_list.append({"type": "BB", "DT": dfDt[0], "BBH": round(band_high, 4), "BBM": round(bb_center, 4),
                            "BBL": round(band_low, 4)})
 
    return bb_list