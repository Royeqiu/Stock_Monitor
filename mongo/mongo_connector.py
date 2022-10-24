import pymongo
import pandas as pd
from Stock_Trade.daily_stock_trade_crawler import Daily_Stock_Trade_Crawler
from Stock_Trade.history_stock_trade_crawler import History_Stock_Trade_Crawler
daily_stock_trade_crawler = Daily_Stock_Trade_Crawler()
stock_list = daily_stock_trade_crawler.get_daily_stock_list()
#stock_list = pd.DataFrame({'stock_number':['0050'],'stock_name':['元大台灣50']})

history_stock_trade_crawler = History_Stock_Trade_Crawler(stock_list)
history_stock_trade_crawler.crawle_history_stock(period='max')
daily_stock_trade_dfs = history_stock_trade_crawler.get_history_stock_dfs()


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = myclient['market_info']
collection = my_db.get_collection('stock_trade_history')
for daily_stock_trade_df in daily_stock_trade_dfs:
    if daily_stock_trade_df.shape[0] != 0:
        continue
    try:
        inserted_dict = daily_stock_trade_df.to_dict('records')
        collection.insert_many(inserted_dict)
    except Exception as e:
        print(str(e))
        print(inserted_dict)
res = collection.find({'stock_number':'0050.TW'})
print(list(res))
selected_df = pd.DataFrame(list(res))
print(selected_df)
print(selected_df[selected_df['Date']=='2022-10-24'])
