from src.Constant_Field import Index_Class_Constant,Mongo_DB_Constant
from Stock_Trade.daily_stock_trade_crawler import Daily_Stock_Trade_Crawler
from Stock_Trade.history_stock_trade_crawler import History_Stock_Trade_Crawler
from Stock_Trade.stock_index_calculator import Stock_Index_Calculator
from mongo.mongo_connector import Mongo_DB_Connector
import pandas as pd


mongo_db_connector = Mongo_DB_Connector()

daily_stock_trade_crawler = Daily_Stock_Trade_Crawler()
daily_trade_df = daily_stock_trade_crawler.get_daily_trade()
stock_list = daily_stock_trade_crawler.get_daily_stock_list()
#stock_list = pd.DataFrame({'stock_number':['0050','2330'],'stock_name':['元大台灣50','台積電']})

history_stock_trade_crawler = History_Stock_Trade_Crawler(stock_list)
history_stock_trade_crawler.crawle_history_stock()
history_stock_dfs = history_stock_trade_crawler.get_history_stock_dfs()
#concated_history_stock_df = pd.concat(history_stock_dfs)
#mongo_db_connector.insert_into(Mongo_DB_Constant.STOCK_TRADE_HISTORY_COLLECTION,concated_history_stock_df)

stock_index_calculator = Stock_Index_Calculator(history_stock_dfs,[Index_Class_Constant.MEAN_INDEX_NAME,Index_Class_Constant.OVER_MEAN_INDEX_NAME])
stock_index_calculator.calculate_index()
# self.pipelines = [Index_Class_Constant.MEAN_INDEX_NAME]
index_stock_dfs = stock_index_calculator.get_stock_index_dfs()
concated_stock_index_df = pd.concat(index_stock_dfs)
print(concated_stock_index_df)
print(concated_stock_index_df.columns)
mongo_db_connector.insert_into(Mongo_DB_Constant.STOCK_INDEX_HISTORY_COLLECTION, concated_stock_index_df)
