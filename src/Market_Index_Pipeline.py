from src.Index_Class_Loader import Index_Class_Loader
from src.Constant_Field import Market_Stock_Constant,Stock_Trade_Constant
import pandas as pd
import os
class Market_Index_Pipeline():

    def __init__(self,pipelines:list):
        self.pipelines = pipelines
        self.index_class_loader = Index_Class_Loader()
        self.index_classes = [self.index_class_loader.get_class(index_name)() for index_name in self.pipelines]

    def calculate_index(self,stock_trade_df:pd.DataFrame):
        return self.pipe(stock_trade_df)

    def pipe(self,latest_stock_list)->pd.DataFrame:
        market_index_df = pd.read_csv(os.path.join(Market_Stock_Constant.MARKET_INDEX_PATH, Market_Stock_Constant.MARKET_BASE_INDEX_NAME))
        for index_template_name,index_class in zip(self.pipelines,self.index_classes):
            index_names, index_df = index_class.calculate_index(latest_stock_list)
            market_index_df = market_index_df.join(index_df,on=Stock_Trade_Constant.STOCK_DATE_COLUMN,how='left')
        return market_index_df