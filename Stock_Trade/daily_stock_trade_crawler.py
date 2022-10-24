import requests
import pandas
from io import StringIO
import os
import datetime
from src.Constant_Field import Daily_Stock_Constant,Stock_Trade_Constant,General_Constant
current_time = datetime.datetime.now()

class Daily_Stock_Trade_Crawler():

    def __init__(self):
        self.address = "https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data"
        self.response = requests.get(self.address)
        data = self.response.text
        mystr = StringIO(data)
        self.daily_trade_df = pandas.read_csv(mystr)
        self.daily_stock_list_df = self.daily_trade_df[
            [Daily_Stock_Constant.STOCK_NUMBER_COLUMN, Daily_Stock_Constant.STOCK_NAME_COLUMN]]
        self.daily_stock_list_df = self.daily_stock_list_df.rename(columns = {Daily_Stock_Constant.STOCK_NUMBER_COLUMN:Stock_Trade_Constant.STOCK_NUMBER_COLUMN,Daily_Stock_Constant.STOCK_NAME_COLUMN:Stock_Trade_Constant.STOCK_NAME_COLUMN})

    def get_daily_trade(self):
        return self.daily_trade_df

    def save_daily_trade(self):
        # 儲存資料
        if not os.path.exists(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH):
            os.mkdir(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH)
        self.daily_trade_df.to_csv(os.path.join(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH, Daily_Stock_Constant.DAILY_STOCK_LIST_NAME.format(current_time.date())), index= False)

    def get_daily_stock_list(self):
        return self.daily_stock_list_df

    def save_daily_stock_list(self):
        if not os.path.exists(General_Constant.ASSETS_PATH):
            os.mkdir(General_Constant.ASSETS_PATH)
        self.latest_daily_stock_list_df.to_csv(os.path.join(General_Constant.ASSETS_PATH, General_Constant.STOCK_LIST_FILE_NAME), index = False)
