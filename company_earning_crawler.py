from Stock_Info.company_monthly_earning_crawler import Company_Monthly_Earnging_Report_Crawler
import os
import pandas as pd
from src.Constant_Field import Company_Monthly_Earning_Constant,General_Constant,Error_MSG,Stock_Trade_Constant
from mongo.mongo_connector import Mongo_DB_Connector
from src.Date_Operation import date_string_formating,get_previous_date


if __name__ == '__main__':
    company_monthly_earning_report_crawler = Company_Monthly_Earnging_Report_Crawler()
    mongo_db_connector = Mongo_DB_Connector()
    date_range = get_previous_date(48)
    print(date_range)
    for date in date_range:
        year,month = date.split('-')
        year = int(year)
        month = int(month)
        print('Download {}-{} earning_report.'.format(year,month))
        sii_monthly_df = company_monthly_earning_report_crawler.get_monthly_earning_report(General_Constant.COMPANY_SII_TYPE,year,month)
        otc_monthly_df = company_monthly_earning_report_crawler.get_monthly_earning_report(General_Constant.COMPANY_OTC_TYPE,year,month)
        total_monthly_df = pd.concat([sii_monthly_df,otc_monthly_df])
        file_path = Company_Monthly_Earning_Constant.HISTORY_EARNING_REPORT_PATH
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        total_monthly_df = total_monthly_df.rename(columns = {Company_Monthly_Earning_Constant.COMPANY_NUMBER_COLUMN:Stock_Trade_Constant.STOCK_NUMBER_COLUMN,
                                                  Company_Monthly_Earning_Constant.COMPANY_NAME_COLUMN:Stock_Trade_Constant.STOCK_NAME_COLUMN,
                                                  Company_Monthly_Earning_Constant.COMMENT_COLUMN:Company_Monthly_Earning_Constant.COMMENT_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.MOM_PERCENTAGE_CHANGE_COLUMN:Company_Monthly_Earning_Constant.MOM_PERCENTAGE_CHANGE_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.LAST_MONTH_EARNING_COLUMN:Company_Monthly_Earning_Constant.LAST_MONTH_EARNING_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.YOY_PERCENTAGE_CHANGE_COLUMN:Company_Monthly_Earning_Constant.YOY_PERCENTAGE_CHANGE_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.LAST_YEAR_EARNING_COLUMN:Company_Monthly_Earning_Constant.LAST_YEAR_EARNING_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.CURRENT_MONTHLY_EARNING_COLUMN:Company_Monthly_Earning_Constant.CURRENT_MONTHLY_EARNING_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.YOY_CUMULATIVE_PERCENTAGE_CHANGE_COLUMN:Company_Monthly_Earning_Constant.YOY_CUMULATIVE_PERCENTAGE_CHANGE_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.LAST_YEAR_CUMULATIVE_EARNING_COLUMN:Company_Monthly_Earning_Constant.LAST_YEAR_CUMULATIVE_EARNING_ENGLISH_COLUMN,
                                                  Company_Monthly_Earning_Constant.CURRENT_CUMULATIVE_EARNING_COLUMN:Company_Monthly_Earning_Constant.CURRENT_CUMULATIVE_EARNING_ENGLISH_COLUMN})

        total_monthly_df[Company_Monthly_Earning_Constant.EARNING_DATE] = date_string_formating(year,month,level=2)
        mongo_db_connector.insert_into('stock_monthly_earning_report',total_monthly_df)