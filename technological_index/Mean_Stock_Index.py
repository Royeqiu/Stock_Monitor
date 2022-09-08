from typing import Tuple,List
import pandas as pd
from technological_index.Base_Stock_Index import Base_Stock_Index
from src.Constant_Field import Stock_Trade_Constant
from src.Constant_Field import Technological_Index_Constant
class MEAN_Stock_Index(Base_Stock_Index):
    def __init__(self):
        self.index_names = Technological_Index_Constant.Mean_Stock_Index.index_names
        self.mean_day_range = Technological_Index_Constant.Mean_Stock_Index.mean_day_range
    def calculate_index(self, stock_trade_df:pd.DataFrame) -> Tuple[List[str], List[pd.Series]]:
        result_series = []
        for day_range in self.mean_day_range:
            result_series.append(stock_trade_df[Stock_Trade_Constant.STOCK_CLOSE_COLUMN].rolling(day_range,center=False).mean().fillna(0))

        return (self.index_names,result_series)