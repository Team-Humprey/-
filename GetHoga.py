import decimal

def get_hoga(cur_price):
    if decimal(str(cur_price)) < 10:
        hoga_val = 0.01
    elif decimal(str(cur_price)) < 100:
        hoga_val = 0.1
    elif decimal(str(cur_price)) < 1000:
        hoga_val = 1
    elif decimal(str(cur_price)) < 10000:
        hoga_val = 5
    elif decimal(str(cur_price)) < 100000:
        hoga_val = 10
    elif decimal(str(cur_price)) < 500000:
        hoga_val = 50
    elif decimal(str(cur_price)) < 1000000:
        hoga_val = 100
    elif decimal(str(cur_price)) < 2000000:
        hoga_val = 500
    else:
        hoga_val = 1000
 
    return hoga_val