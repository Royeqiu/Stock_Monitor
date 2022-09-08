from typing import Tuple,List
import pandas as pd
class Base_Stock_Index():
    def __init__(self):
        pass

    def calculate_index(self,stock_trade_df:pd.DataFrame) -> Tuple[List[str],List[pd.Series]]:
        pass