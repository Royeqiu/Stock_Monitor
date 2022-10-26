class Market_Stock_Constant():
    TW_WEIGHTED_INDEX_ID = '^TWII'
    TW_WEIGHTED_INDEX_NAME = '台灣加權指數'
    MARKET_BASE_INDEX_NAME = 'market_base_index.csv'
    MARKET_INDEX_PATH = 'market_index/'
    MARKET_TECHNOLOGICAL_INDEX_NAME = 'market_technological_index.csv'

class Daily_Stock_Constant():
    DAILY_STOCK_LIST_NAME = 'daily_stock_list_{}.csv'
    DAILY_STOCK_TRADE_PATH = 'daily_stock/'
    STOCK_NUMBER_COLUMN = '證券代號'
    STOCK_NAME_COLUMN = '證券名稱'


class Stock_Trade_Constant():
    STOCK_NUMBER_COLUMN = 'stock_number'
    STOCK_NAME_COLUMN = 'stock_name'
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
    COMPANY_OTC_TYPE = 'otc'
    COMPANY_SII_TYPE = 'sii'

class Index_Class_Constant():
    MEAN_INDEX_NAME = 'mean_index'
    INDEX_HISTORY_STOCK_PATH = 'index_history_stock/'
    INDEX_HISTORY_STOCK_NAME = 'index_history_stock.h5'
    ADL_INDEX_NAME = 'ADL_Index'
    OVER_MEAN_INDEX_NAME = 'over_mean_index'
class Technological_Index_Constant():
    class Basic_Market_Index_Constant():
        TEN_DAYS_RANGE = 10
        TWENTY_DAYS_RANGE = 20
        THIRTY_DAYS_RANGE = 30
        FIFTY_DAYS_RANGE = 50
        ONE_HUNDRED_DAYS_RANGE = 100
        TWO_HUNDRED_DAYS_RANGE = 200
    class Advance_Decline_Line_Market_Index_Constant():
        INDEX_NAMES = ["20_ADL", "30_ADL", "50_ADL", "100_ADL", "200_ADL"]
    class Mean_Stock_Index_Constant():
        INDEX_NAMES = ["20_means", "30_means", "50_means", "100_means", "200_means"]
        MEAN_DAY_RANGE = [20, 30, 50, 100, 200]
    class Over_Mean_Stock_Index_Constant():
        INDEX_NAMES = ["over_20_means", "over_30_means", "over_50_means", "over_100_means", "over_200_means"]
        MEAN_DAY_RANGE = [20, 30, 50, 100, 200]

class Company_Monthly_Earning_Constant():

    SII_EARNING_URL_AFTER_IFRS = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_{}_{}_0.html'
    SII_EARNING_URL_BEFORE_IFRS = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_{}_{}.html'
    OTC_EARNING_URL_AFTER_IFRS = 'https://mops.twse.com.tw/nas/t21/otc/t21sc03_{}_{}_0.html'
    OTC_EARNING_URL_BEFORE_IFRS = 'https://mops.twse.com.tw/nas/t21/otc/t21sc03_{}_{}.html'
    REPORT_STRUCTURAL_LEVELS = 'levels'
    COMPANY_NUMBER_COLUMN = '公司代號'
    CURRENT_MONTHLY_EARNING_COLUMN = '當月營收'
    TOTAL_EARNING_COLUMN = '合計'
    HISTORY_EARNING_REPORT_PATH = 'history_earning_report'
    MONTHLY_HISTORY_EARNING_REPORT_FILE_NAME = 'monthly_earning_report_{}_{}.csv'
    MOM_PERCENTAGE_CHANGE = '上月比較增減(%)'
    MONTH = 'month'

class Error_MSG():
    class Company_Monthly_Earning_Error():
        COMPANY_TYPE_VALUE_ERROR = 'The type only accpet sii or otc'
        REPORT_DATE_OVER_CURRENT_DATE_ERROR =  'Report date over current date'

class Mongo_DB_Constant():

    DB_NAME = 'market_info'
    STOCK_TRADE_HISTORY_COLLECTION = 'stock_trade_history'
    STOCK_INDEX_HISTORY_COLLECTION = 'stock_index_history'
    MARKET_INDEX_COLLECTION = 'market_index'