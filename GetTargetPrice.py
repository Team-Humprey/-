import decimal
from GetHoga import get_hoga

# cal_type : H:호가로, R:비율로
# st_price : 기준가격
# chg_val : 변화단위

def get_targetprice(cal_type, st_price, chg_val):

    rtn_price = st_price

    if cal_type.upper() == "H":
 
        for i in range(0, abs(int(chg_val))):
 
            hoga_val = get_hoga(rtn_price)
 
            if decimal(str(chg_val)) > 0:
                rtn_price = decimal(str(rtn_price)) + decimal(str(hoga_val))
            elif decimal(str(chg_val)) < 0:
                rtn_price = decimal(str(rtn_price)) - decimal(str(hoga_val))
            else:
                break

    elif cal_type.upper() == "R":
 
        while True:
 
            hoga_val = get_hoga(st_price)
 
            if decimal(str(chg_val)) > 0:
                rtn_price = decimal(str(rtn_price)) + decimal(str(hoga_val))
            elif decimal(str(chg_val)) < 0:
                rtn_price = decimal(str(rtn_price)) - decimal(str(hoga_val))
            else:
                break
 
            if decimal(str(chg_val)) > 0:
                if decimal(str(rtn_price)) >= decimal(str(st_price)) * (
                        decimal(str(1)) + (decimal(str(chg_val))) / decimal(str(100))):
                    break
            elif decimal(str(chg_val)) < 0:
                if decimal(str(rtn_price)) <= decimal(str(st_price)) * (
                        decimal(str(1)) + (decimal(str(chg_val))) / decimal(str(100))):
                    break
 
    return rtn_price