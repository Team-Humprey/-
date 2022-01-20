from GetCandle import get_candle;
from GetRSI import get_rsi;
from GetBB import get_bb;
from GetMacd import get_macd;

def get_assistant(target_item, tick_kind, inq_range, loop_cnt):
    assistant_data = []
    candle_datas = []
    candle_data = get_candle(target_item, tick_kind, inq_range)
 
    if len(candle_data) >= 30:
        for i in range(0, int(loop_cnt)):
            candle_datas.append(candle_data[i:int(len(candle_data))])
        rsi_data = get_rsi(candle_datas)
        macd_data = get_macd(candle_datas, loop_cnt)
        bb_data = get_bb(candle_datas)
        if len(rsi_data) > 0:
            assistant_data.append(rsi_data)
        if len(macd_data) > 0:
            assistant_data.append(macd_data)
        if len(bb_data) > 0:
            assistant_data.append(bb_data)
    
    return assistant_data