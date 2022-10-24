from src.Constant_Field import Index_Class_Constant
from Stock_Trade.daily_stock_trade_crawler import Daily_Stock_Trade_Crawler
from Stock_Trade.history_stock_trade_crawler import History_Stock_Trade_Crawler
from Stock_Trade.stock_index_calculator import Stock_Index_Calculator
import sys

args = sys.argv[1:]


daily_stock_trade_crawler = Daily_Stock_Trade_Crawler()
daily_trade_df = daily_stock_trade_crawler.get_daily_trade()
stock_list = daily_stock_trade_crawler.get_daily_stock_list()
history_stock_trade_crawler = History_Stock_Trade_Crawler(stock_list)
history_stock_trade_crawler.crawle_history_stock()
history_stock_dfs = history_stock_trade_crawler.get_history_stock_dfs()
stock_index_calculator = Stock_Index_Calculator(history_stock_dfs,[Index_Class_Constant.MEAN_INDEX_NAME])
stock_index_calculator.calculate_index()
# self.pipelines = [Index_Class_Constant.MEAN_INDEX_NAME]
appended_stock_dfs = stock_index_calculator.get_stock_index_dfs()
