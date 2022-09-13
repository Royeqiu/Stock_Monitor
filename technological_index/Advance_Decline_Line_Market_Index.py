from typing import Tuple,List
from src.Constant_Field import Index_Class_Constant,Technological_Index_Constant,Stock_Trade_Constant
from technological_index.Base_Market_Index import Base_Market_Index
import pandas as pd
import os
from collections import defaultdict
class Advance_Decline_Line_Index(Base_Market_Index):
    def __init__(self):
        pass

    def calculate_index(self,latest_stock_list) -> Tuple[List[str],List[pd.Series]]:
        company_count_dict = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))
        index_names = Technological_Index_Constant.Mean_Stock_Index.index_names
        for stock_index, stock_id in enumerate(latest_stock_list):
            if stock_index%10 ==0:
                print('{} stock has been processed'.format(stock_index))
            key_id = stock_id + '.TW'
            stock_df = pd.read_hdf(os.path.join(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH,Index_Class_Constant.INDEX_HISTORY_STOCK_NAME),key=key_id)
            for index, date, stock_price in zip(stock_df.index,stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].values, stock_df[Stock_Trade_Constant.STOCK_CLOSE_COLUMN].values):
                for name in index_names:
                    if stock_price > stock_df.iloc[index][name]:
                        company_count_dict[date][name][1] += 1
                    else:
                        company_count_dict[date][name][0] += 1

        res_dict = dict()
        for name in index_names:
            tmp_res = []
            for date in stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].values:
                tmp_res.append(company_count_dict[date][name][1]/(company_count_dict[date][name][1] + company_count_dict[date][name][0]))
            res_dict[name] = tmp_res
        res_dict[Stock_Trade_Constant.STOCK_DATE_COLUMN] = stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].values
        return pd.DataFrame(res_dict)
