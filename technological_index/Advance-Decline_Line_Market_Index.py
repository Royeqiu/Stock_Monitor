from typing import Tuple,List
from src.Constant_Field import Index_Class_Constant,Technological_Index_Constant,Stock_Trade_Constant
from technological_index import Base_Market_Index
import pandas as pd
import os
from collections import defaultdict
class Advance_Decline_Line_Index(Base_Market_Index):
    def __init__(self):
        pass

    def calculate_index(self,latest_stock_list) -> Tuple[List[str],List[pd.Series]]:
        company_count_dict = defaultdict(lambda :defaultdict(lambda :defaultdict[int]))
        index_names = Technological_Index_Constant.Mean_Stock_Index.index_names
        for stock_id in latest_stock_list:
            key_id = stock_id + '.TW'
            stock_df =  pd.read_hdf(os.path.join(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH,Index_Class_Constant.INDEX_HISTORY_STOCK_NAME),key=key_id)
            for index,date,stock_price in zip(stock_df.index,stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].values,stock_df[Stock_Trade_Constant.STOCK_CLOSE_COLUMN].values):
                for name in index_names:
                    if stock_price > stock_df.iloc[index][name]:
                        company_count_dict[date][name][1] += 1
                    else:
                        company_count_dict[date][name][0] += 1

