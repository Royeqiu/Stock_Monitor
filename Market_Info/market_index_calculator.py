from src.Market_Index_Pipeline import Market_Index_Pipeline
from src.Constant_Field import Index_Class_Constant,Stock_Trade_Constant,General_Constant,Market_Stock_Constant,Technological_Index_Constant
import pandas as pd
import os
class Market_Index_Calculator():
    def __init__(self,stock_dfs,pipelines):
        #self.pipelines = [Index_Class_Constant.ADL_INDEX_NAME]
        self.pipelines = pipelines
        self.market_index_pipeliner = Market_Index_Pipeline(self.pipelines)
        self.stock_dfs = stock_dfs
    def calculate_index(self):
        self.market_index_df = self.market_index_pipeliner.calculate_index(self.stock_dfs[Stock_Trade_Constant.STOCK_NUMBER_COLUMN].values,
                                                       Technological_Index_Constant.Basic_Market_Index_Constant.TWO_HUNDRED_DAYS_RANGE)
        self.market_index_df = self.market_index_df.sort_values(by=[Stock_Trade_Constant.STOCK_DATE_COLUMN])

    def save_market_index_to_csv(self):
        if not os.path.exists(Market_Stock_Constant.MARKET_INDEX_PATH):
            os.mkdir(Market_Stock_Constant.MARKET_INDEX_PATH)
        self.market_index_df.to_csv(os.path.join(Market_Stock_Constant.MARKET_INDEX_PATH,
                                            Market_Stock_Constant.MARKET_TECHNOLOGICAL_INDEX_NAME), index=False)

    def get_market_index_df(self):
        return self.market_index_df


