from typing import Tuple,List
from src.Constant_Field import Index_Class_Constant,Technological_Index_Constant,Stock_Trade_Constant
from technological_index.Base_Market_Index import Base_Market_Index

import pandas as pd
import os
from collections import defaultdict
class Advance_Decline_Line_Index(Base_Market_Index):
    def __init__(self):
        self.index_names = []
        pass

    def calculate_index(self,latest_stock_list,date_range) -> Tuple[List[str],List[pd.Series]]:
        company_count_dict = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))
        mean_index_names = Technological_Index_Constant.Mean_Stock_Index_Constant.INDEX_NAMES
        for stock_index, stock_id in enumerate(latest_stock_list):
            if stock_index % 50 == 0:
                print('{} stock has been processed'.format(stock_index))
            key_id = stock_id + '.TW'
            stock_df = pd.read_hdf(os.path.join(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH,Index_Class_Constant.INDEX_HISTORY_STOCK_NAME),key=key_id)
            tail_df = stock_df.tail(date_range)
            for index in range(date_range - 1, -1, -1):
                if index >= tail_df.shape[0]:
                    continue
                date = tail_df.iloc[index][Stock_Trade_Constant.STOCK_DATE_COLUMN]
                stock_price = tail_df.iloc[index][Stock_Trade_Constant.STOCK_CLOSE_COLUMN]
                for mean_name in mean_index_names:
                    if stock_price >= tail_df.iloc[index][mean_name] and tail_df.iloc[index][mean_name]!=0:
                        company_count_dict[date][mean_name][1] += 1
                    elif stock_price < tail_df.iloc[index][mean_name] and tail_df.iloc[index][mean_name]!=0:
                        company_count_dict[date][mean_name][0] += 1
                    else:
                        pass
        res_dict = dict()
        res_dict[Stock_Trade_Constant.STOCK_DATE_COLUMN] = tail_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].values
        ADL_index_names = Technological_Index_Constant.Mean_Stock_Index_Constant.INDEX_NAMES
        for mean_name, ADL_name in zip(mean_index_names, ADL_index_names):
            tmp_res = []
            for date in tail_df[Stock_Trade_Constant.STOCK_DATE_COLUMN]:
                tmp_res.append(company_count_dict[date][mean_name][1]/(company_count_dict[date][mean_name][1] + company_count_dict[date][mean_name][0]))
            res_dict[ADL_name] = tmp_res
        return pd.DataFrame(res_dict)