from SendRequest import send_request

# market : 대상 마켓
# except_item : 제외 종목

def get_items(market, except_item):
    rtn_list = []
    markets = market.split(',')
    except_items = except_item.split(',')
 
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails": "false"}
    response = send_request("GET", url, querystring, "")
    data = response.json()
 
    for data_for in data:
        for market_for in markets:
            if data_for['market'].split('-')[0] == market_for:
                rtn_list.append(data_for)
 
    for rtnlist_for in rtn_list[:]:
        for exceptItemFor in except_items:
            for marketFor in markets:
                if rtnlist_for['market'] == marketFor + '-' + exceptItemFor:
                    rtn_list.remove(rtnlist_for)
 
    return rtn_list