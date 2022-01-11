import pandas as pd
import pyupbit

price_KRW = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH", "KRW-XRP"])
print("\nBTC : {0:>10,} 원".format(int(price_KRW["KRW-BTC"])))
print("ETH : {0:>10,} 원".format(int(price_KRW["KRW-ETH"])))
print("XRP : {0:>10,} 원".format(int(price_KRW["KRW-XRP"])))

price_BTC = pyupbit.get_current_price("BTC-ETH")
print("ETH : {} BTC\n".format(price_BTC))

price_BTC = pyupbit.get_current_price("BTC-ETH")
print("ETH : {} BTC\n".format(price_BTC))

df = pyupbit.get_ohlcv("KRW-BTC")
print(df)