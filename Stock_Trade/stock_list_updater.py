from src.Constant_Field import Stock_Trade_Constant,General_Constant
import os
class Stock_List_Updater():
    def __init__(self,daily_trade_df):
        self.daily_trade_df = daily_trade_df
    def get_latest_daily_stock_list(self):
        latest_daily_stock_list_df = self.daily_stock_df[[Stock_Trade_Constant.STOCK_NUMBER_COLUMN, Stock_Trade_Constant.STOCK_NAME_COLUMN]]
        return latest_daily_stock_list_df

    def save_latest_daily_stock_list(self,latest_daily_stock_list_df):
        if not os.path.exists(General_Constant.ASSETS_PATH):
            os.mkdir(General_Constant.ASSETS_PATH)
        latest_daily_stock_list_df.to_csv(os.path.join(General_Constant.ASSETS_PATH, General_Constant.STOCK_LIST_FILE_NAME), index = False)
