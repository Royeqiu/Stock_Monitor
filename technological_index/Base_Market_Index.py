from typing import Tuple,List
import pandas as pd
class Base_Market_Index():
    def __init__(self):
        pass

    def calculate_index(self,latest_stock_list:List[str],date_range) -> Tuple[List[str],List[pd.Series]]:
        pass