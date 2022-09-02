import yfinance as yf
from src.Constant_Field import HISTORY_STOCK_TRADE_PATH,ASSETS_PATH,STOCK_LIST_FILE_NAME,STOCK_NUMBER_COLUMN,STOCK_NAME_COLUMN,HISTORY_STOCK_LIST_NAME
import h5py
import os
import time
import datetime
import pandas as pd
# 讀取csv檔

current_time = datetime.datetime.now()
stock_list = pd.read_csv(os.path.join(ASSETS_PATH, STOCK_LIST_FILE_NAME))
for i in stock_list.index:
    if i % 100 == 0:
        print('{} stock history has been crawled'.format(i))
    # 抓取股票資料
    stock_id = stock_list.loc[i, STOCK_NUMBER_COLUMN] + '.TW'
    data = yf.Ticker(stock_id)
    stock_df = data.history(period ='max')
    stock_df.to_hdf(os.path.join(HISTORY_STOCK_TRADE_PATH, HISTORY_STOCK_LIST_NAME.format(current_time.date())), mode ='a', key = stock_id)
