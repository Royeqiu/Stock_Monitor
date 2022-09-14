import yfinance as yf
from src.Constant_Field import History_Stock_Constant,General_Constant,Stock_Trade_Constant
import h5py
import os
import time
import datetime
import pandas as pd
# 讀取csv檔

current_time = datetime.datetime.now()
stock_list = pd.read_csv(os.path.join(General_Constant.ASSETS_PATH, General_Constant.STOCK_LIST_FILE_NAME))
history_stock_trade_file = os.path.join(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH,
                                        History_Stock_Constant.HISTORY_STOCK_LIST_NAME)
if os.path.exists(history_stock_trade_file):
    os.remove(history_stock_trade_file)
for i in stock_list.index:
    if i % 100 == 0:
        print('{} stock history has been crawled'.format(i))
    # 抓取股票資料
    stock_id = stock_list.loc[i, Stock_Trade_Constant.STOCK_NUMBER_COLUMN] + '.TW'
    data = yf.Ticker(stock_id)
    stock_df = data.history(period ='max')
    stock_df = stock_df.reset_index(level = 0)
    if not os.path.exists(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH):
        os.mkdir(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH)
    stock_df.to_hdf(os.path.join(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH, History_Stock_Constant.HISTORY_STOCK_LIST_NAME), mode ='a', key = stock_id)
