import pymongo
import pandas as pd
from Stock_Trade.daily_stock_trade_crawler import Daily_Stock_Trade_Crawler
from Stock_Trade.history_stock_trade_crawler import History_Stock_Trade_Crawler


class Mongo_DB_Connector():
    def __init__(self):
        self.db = pymongo.MongoClient("mongodb://localhost:27017/")
        self.stock_db = self.db['market_info']

    def insert_into(self,collection:str,df:pd.DataFrame):
        try:
            assert df.shape[0] != 0, 'the input size is 0'
            collection = self.stock_db.get_collection(collection)
            inserted_dict = df.to_dict(orient='records')
            collection.insert_many(inserted_dict)
        except Exception as e:
            print(str(e))

    def drop_collection(self,collection:str):
        self.stock_db.get_collection(collection).drop()

    def create_collection(self,collection:str):
        self.db.createCollection(collection)

    def query_from_collection(self,collection:str,condition_dict:dict):
        res = self.stock_db.get_collection(collection).find(condition_dict)
        df = pd.DataFrame(list(res))
        return df

if __name__ =='__main__':
    daily_stock_trade_crawler = Daily_Stock_Trade_Crawler()
    stock_list = daily_stock_trade_crawler.get_daily_stock_list()
    #stock_list = pd.DataFrame({'stock_number':['0050'],'stock_name':['元大台灣50']})
    mongo_db_connector = Mongo_DB_Connector()
    history_stock_trade_crawler = History_Stock_Trade_Crawler(stock_list)
    history_stock_trade_crawler.crawle_history_stock(period='max')
    daily_stock_trade_dfs = history_stock_trade_crawler.get_history_stock_dfs()
    for daily_stock_trade_df in daily_stock_trade_dfs:
        mongo_db_connector.insert_into('stock_trade_history')
    selected_df = mongo_db_connector.query_from_collection('stock_trade_history',{'stock_number':'0050.TW'})
    print(selected_df)
    print(selected_df[selected_df['Date']=='2022-10-24'])
