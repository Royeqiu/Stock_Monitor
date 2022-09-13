from src.Stock_Index_Pipeline import Stock_Index_Pipeline
from src.Constant_Field import Index_Class_Constant,Stock_Trade_Constant,General_Constant,History_Stock_Constant
import pandas as pd
import os

stock_list_df = pd.read_csv(os.path.join(General_Constant.ASSETS_PATH,General_Constant.STOCK_LIST_FILE_NAME))
pipelines = [Index_Class_Constant.MEAN_INDEX_NAME]
stock_index_pipeliner = Stock_Index_Pipeline(pipelines)

for i in stock_list_df.index:
    if i % 100 == 0:
        print('{} stock history has been calcuated {}'.format(i,','.join(pipelines)))
    stock_id = stock_list_df.iloc[i][Stock_Trade_Constant.STOCK_NUMBER_COLUMN] + '.TW'
    stock_df = pd.read_hdf(os.path.join(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH, History_Stock_Constant.HISTORY_STOCK_LIST_NAME), key=stock_id)
    appended_stock_df = stock_index_pipeliner.calculate_index(stock_df)
    if not os.path.exists(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH):
        os.mkdir(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH)
    appended_stock_df.to_hdf(os.path.join(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH, Index_Class_Constant.INDEX_HISTORY_STOCK_NAME), mode ='a', key = stock_id)

