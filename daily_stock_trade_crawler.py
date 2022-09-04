import requests
import pandas
from io import StringIO
import os
import datetime
from src.Constant_Field import Daily_Stock_Constant
current_time = datetime.datetime.now()

address = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data"

# 取得資料
response = requests.get(address)
data = response.text
mystr = StringIO(data)
df = pandas.read_csv(mystr)
# 儲存資料
if not os.path.exists(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH):
    os.mkdir(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH)
df.to_csv(os.path.join(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH, Daily_Stock_Constant.DAILY_STOCK_LIST_NAME.format(current_time.date())), index= False)
