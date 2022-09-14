from src.Index_Class_Loader import Index_Class_Loader
from src.Constant_Field import Market_Stock_Constant,Stock_Trade_Constant
import pandas as pd
import os
from functools import reduce

class Market_Index_Pipeline():

    def __init__(self,pipelines:list):
        self.pipelines = pipelines
        self.index_class_loader = Index_Class_Loader()
        self.index_classes = [self.index_class_loader.get_class(index_name)() for index_name in self.pipelines]

    def calculate_index(self,stock_trade_df:pd.DataFrame,date_range:int):
        return self.pipe(stock_trade_df,date_range)

    def pipe(self,latest_stock_list,date_range)->pd.DataFrame:
        market_index_df_list = []
        for index_template_name,index_class in zip(self.pipelines,self.index_classes):
            index_df = index_class.calculate_index(latest_stock_list,date_range)
            market_index_df_list.append(index_df)
        market_index_df = reduce(lambda left,right: pd.merge(left,right,on=Stock_Trade_Constant.STOCK_DATE_COLUMN,how = 'outer'),market_index_df_list)
        return market_index_df