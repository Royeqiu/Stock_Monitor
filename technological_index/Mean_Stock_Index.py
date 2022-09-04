from typing import Tuple,List
import pandas as pd
from technological_index.Base_Stock_Index import Base_Stock_Index
from src.Constant_Field import Stock_Trade_Constant
class MEAN_Stock_Index(Base_Stock_Index):
    def __init__(self):
        self.index_names = ["30_means","50_means","100_means","200_means"]
        self.mean_day_range = [30,50,100,200]
    def cal_culate_index(self,stock_trade_df:pd.DataFrame) -> Tuple[List[str],List[pd.Series]]:
        result_series = []
        for day_range in self.mean_day_range:
            result_series.append(stock_trade_df[Stock_Trade_Constant.STOCK_CLOSE_COLUMN].rolling(day_range,center=False).mean().fillna(0))

        return (self.index_names,result_series)