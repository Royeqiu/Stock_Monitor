import yfinance as yf
from src.Constant_Field import History_Stock_Constant,Stock_Trade_Constant
import os


class History_Stock_Trade_Crawler():
    def __init__(self,stock_list):
        # 讀取csv檔
        self.stock_list = stock_list
        self.history_stock_trade_file = os.path.join(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH,
                                        History_Stock_Constant.HISTORY_STOCK_LIST_NAME)
        self.stock_dfs = []
        self.stock_dict = {}

    def crawle_history_stock(self,period='max'):
        for i in self.stock_list.index:
            if i % 100 == 0:
                print('{} stock history has been crawled'.format(i))
            # 抓取股票資料
            stock_id = self.stock_list.loc[i, Stock_Trade_Constant.STOCK_NUMBER_COLUMN] + '.TW'
            print(i, stock_id)
            data = yf.Ticker(stock_id)
            # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
            stock_df = data.history(period = period)
            stock_df = stock_df.reset_index(level = 0)
            stock_df[Stock_Trade_Constant.STOCK_NUMBER_COLUMN] = stock_id
            stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN] = stock_df[Stock_Trade_Constant.STOCK_DATE_COLUMN].apply(lambda x: x.date().strftime("%Y-%m-%d"))
            self.stock_dict[stock_id] = stock_df
            self.stock_dfs.append(stock_df)

    def get_history_stock_df(self,stock_id):
        return self.stock_dict[stock_id]

    def get_history_stock_dfs(self):
        return self.stock_dfs

    def save_history_stock_trade_to_hdf(self):
        if not os.path.exists(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH):
            os.mkdir(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH)
        if os.path.exists(self.history_stock_trade_file):
            print('remove old data and start to up to date')
            os.remove(self.history_stock_trade_file)
        for stock_df in self.stock_dfs:
            stock_id = stock_df[Stock_Trade_Constant.STOCK_NUMBER_COLUMN][0]
            stock_df.to_hdf(os.path.join(History_Stock_Constant.HISTORY_STOCK_TRADE_PATH, History_Stock_Constant.HISTORY_STOCK_LIST_NAME), mode ='a', key = stock_id)

