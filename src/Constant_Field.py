class Market_Stock_Constant():
    TW_WEIGHTED_INDEX_ID = '^TWII'
    TW_WEIGHTED_INDEX_NAME = '台灣加權指數'
    MARKET_BASE_INDEX_NAME = 'market_base_index.csv'
    MARKET_INDEX_PATH = 'market_index/'
    MARKET_TECHNOLOGICAL_INDEX_NAME = 'market_technological_index.csv'

class Daily_Stock_Constant():
    DAILY_STOCK_LIST_NAME = 'daily_stock_list_{}.csv'
    DAILY_STOCK_TRADE_PATH = 'daily_stock/'

class Stock_Trade_Constant():
    STOCK_NUMBER_COLUMN = '證券代號'
    STOCK_NAME_COLUMN = '證券名稱'
    STOCK_CLOSE_COLUMN = 'Close'
    STOCK_HIGH_COLUMN = 'High'
    STOCK_OPEN_COLUMN = 'Open'
    STOCK_LOW_COLUMN = 'LOW'
    STOCK_VOLUME_DIVIDENDS_COLUMN = 'Dividends'
    STOCK_SPLITS_COLUMN = 'Stock Splits'
    STOCK_DATE_COLUMN = 'Date'

class History_Stock_Constant():
    HISTORY_STOCK_LIST_NAME = 'history_data.h5'
    HISTORY_STOCK_TRADE_PATH = 'history_stock/'

class General_Constant():
    ASSETS_PATH = 'assets/'
    STOCK_LIST_FILE_NAME = 'stock_list.csv'

class Index_Class_Constant():
    MEAN_INDEX_NAME = 'mean_index'
    INDEX_HISTORY_STOCK_PATH = 'index_history_stock/'
    INDEX_HISTORY_STOCK_NAME = 'index_history_stock.h5'
    ADL_INDEX_NAME = 'ADL_Index'

class Technological_Index_Constant():

    class Mean_Stock_Index():
        index_names = ["20_means","30_means","50_means","100_means","200_means"]
        mean_day_range = [20,30,50,100,200]

