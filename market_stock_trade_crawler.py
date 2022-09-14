import yfinance as yf
from src.Constant_Field import Market_Stock_Constant,Stock_Trade_Constant
import os

# 抓取大盤資料
stock_id = Market_Stock_Constant.TW_WEIGHTED_INDEX_ID
data = yf.Ticker(stock_id)
market_df = data.history(period ='max')
market_df = market_df.reset_index(level = 0)
if not os.path.exists(Market_Stock_Constant.MARKET_INDEX_PATH):
    os.mkdir(Market_Stock_Constant.MARKET_INDEX_PATH)
market_df = market_df.sort_values(by=Stock_Trade_Constant.STOCK_DATE_COLUMN,ascending=False)
market_df.to_csv(os.path.join(Market_Stock_Constant.MARKET_INDEX_PATH, Market_Stock_Constant.MARKET_BASE_INDEX_NAME), index = False)
