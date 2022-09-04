from src.Constant_Field import Daily_Stock_Constant,Stock_Trade_Constant,General_Constant
from src.Date_Operation import turn_to_datetime
import os
import pandas as pd
daily_stock_list_names = os.listdir(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH)
def get_last_datetime(daily_stock_list_names:list):
    datetime_list = []
    for name in daily_stock_list_names:
        datetime_list.append(turn_to_datetime(name.split('_')[-1][:10]))
    return sorted(datetime_list,key = lambda x:x,reverse=True)[0]
latest_datetime = get_last_datetime(daily_stock_list_names)
latest_daily_stock = Daily_Stock_Constant.DAILY_STOCK_LIST_NAME.format(latest_datetime.date())
latest_daily_stock_df = pd.read_csv(os.path.join(Daily_Stock_Constant.DAILY_STOCK_TRADE_PATH, latest_daily_stock))
latest_daily_stock_list_df = latest_daily_stock_df[[Stock_Trade_Constant.STOCK_NUMBER_COLUMN, Stock_Trade_Constant.STOCK_NAME_COLUMN]]
if not os.path.exists(General_Constant.ASSETS_PATH):
    os.mkdir(General_Constant.ASSETS_PATH)
latest_daily_stock_list_df.to_csv(os.path.join(General_Constant.ASSETS_PATH, General_Constant.STOCK_LIST_FILE_NAME), index = False)
