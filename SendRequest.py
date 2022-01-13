import requests
import time

def send_request(reqType, reqUrl, reqParam, reqHeader):
    err_sleep_time = 0.3

    while True:
        response = requests.request(reqType, reqUrl, params=reqParam, headers=reqHeader)

        if 'Remaining-Req' in response.headers:
 
            hearder_info = response.headers['Remaining-Req']
            start_idx = hearder_info.find("sec=")
            end_idx = len(hearder_info)
            remain_sec = hearder_info[int(start_idx):int(end_idx)].replace('sec=', '')
 
        if int(remain_sec) < 3:
            time.sleep(err_sleep_time)
 
        if response.status_code == 200 or response.status_code == 201:
            break

        elif response.status_code == 429:
            time.sleep(err_sleep_time)
 
    return response