from src.Index_Class_Loader import Index_Class_Loader
import pandas as pd
class Stock_Index_Pipeliner():

    def __init__(self,pipelines:list):
        self.pipelines = pipelines
        self.index_class_loader = Index_Class_Loader()
        self.index_classes = [self.index_class_loader.get_class(index_name)() for index_name in self.pipelines]

    def calculate_index(self,stock_trade_df:pd.DataFrame):
        return self.pipe(stock_trade_df)

    def pipe(self,stock_trade_df:pd.DataFrame)->pd.DataFrame:
        copied_stock_trade_df = stock_trade_df.copy()
        for index_template_name,index_class in zip(self.pipelines,self.index_classes):
            index_names, index_serieses = index_class.cal_culate_index(copied_stock_trade_df)
            for index_name, index_series in zip(index_names,index_serieses):
                copied_stock_trade_df[index_name] = index_series
        return copied_stock_trade_df