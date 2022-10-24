from src.Stock_Index_Pipeline import Stock_Index_Pipeline
from src.Constant_Field import Index_Class_Constant,Stock_Trade_Constant,General_Constant,History_Stock_Constant
import os

class Stock_Index_Calculator():
    def __init__(self,stock_dfs,pipelines):
        #self.pipelines = [Index_Class_Constant.MEAN_INDEX_NAME]
        self.pipelines = pipelines
        self.stock_index_pipeliner = Stock_Index_Pipeline(self.pipelines)
        self.stock_index_dfs = []
        self.stock_dfs = stock_dfs

    def calculate_index(self):
        for i,stock_df in enumerate(self.stock_dfs):
            if i % 100 == 0:
                print('{} stock history has been calcuated {}'.format(i, ','.join(self.pipelines)))
            appended_stock_df = self.stock_index_pipeliner.calculate_index(stock_df)
            self.stock_index_dfs.append(appended_stock_df)

    def save_stock_index_to_hdf(self):
        index_history_file = os.path.join(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH, Index_Class_Constant.INDEX_HISTORY_STOCK_NAME)
        if os.path.exists(index_history_file):
            os.remove(index_history_file)
        for i,appended_stock_df in enumerate(self.stock_index_dfs):
            if i % 100 == 0:
                print('{} stock history has been calcuated {}'.format(i,','.join(self.pipelines)))
            if not os.path.exists(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH):
                os.mkdir(Index_Class_Constant.INDEX_HISTORY_STOCK_PATH)
            stock_id = appended_stock_df[Stock_Trade_Constant.STOCK_NUMBER_COLUMN][0]
            appended_stock_df.to_hdf(index_history_file, mode ='a', key = stock_id)

    def get_stock_index_dfs(self):
        return self.stock_index_dfs
