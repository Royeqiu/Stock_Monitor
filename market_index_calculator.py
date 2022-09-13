from src.Market_Index_Pipeline import Market_Index_Pipeline
from src.Constant_Field import Index_Class_Constant,Stock_Trade_Constant,General_Constant,Market_Stock_Constant
import pandas as pd
import os

stock_list_df = pd.read_csv(os.path.join(General_Constant.ASSETS_PATH,General_Constant.STOCK_LIST_FILE_NAME))
pipelines = [Index_Class_Constant.ADL_INDEX_NAME]
stock_index_pipeliner = Market_Index_Pipeline(pipelines)

market_index_df = stock_index_pipeliner.calculate_index(stock_list_df[Stock_Trade_Constant.STOCK_NUMBER_COLUMN].values)

if not os.path.exists(Market_Stock_Constant.MARKET_INDEX_PATH):
    os.mkdir(Market_Stock_Constant.MARKET_INDEX_PATH)

market_index_df.to_csv(os.path.join(Market_Stock_Constant.MARKET_INDEX_PATH, Market_Stock_Constant.MARKET_TECHNOLOGICAL_INDEX_NAME), Index = False)
