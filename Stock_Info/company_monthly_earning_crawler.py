"""
reference data:
https://www.finlab.tw/%E8%B6%85%E7%B0%A1%E5%96%AE%E7%94%A8python%E6%8A%93%E5%8F%96%E6%AF%8F%E6%9C%88%E7%87%9F%E6%94%B6/

"""
import pandas as pd
import requests
from io import StringIO
from src.Constant_Field import Company_Monthly_Earning_Constant,General_Constant,Error_MSG
from src.Date_Operation import get_current_date,turn_to_datetime

class Company_Monthly_Earnging_Report_Crawler():
    def get_monthly_earning_report(self,type, year, month):

        if year < 1911:
            year += 1911
        target_datetime = turn_to_datetime('-'.join([str(year),str(month),'28']))
        current_datetime = get_current_date()
        assert target_datetime < current_datetime, Error_MSG.Company_Monthly_Earning_Error.REPORT_DATE_OVER_CURRENT_DATE_ERROR

        if year > 1911:
            year -= 1911

        if type == General_Constant.COMPANY_SII_TYPE:
            url = Company_Monthly_Earning_Constant.SII_EARNING_URL_AFTER_IFRS.format(year, month)
            if year <= 98:
                url = Company_Monthly_Earning_Constant.SII_EARNING_URL_BEFORE_IFRS.format(year, month)
        elif type ==General_Constant.COMPANY_OTC_TYPE:
            url = Company_Monthly_Earning_Constant.OTC_EARNING_URL_AFTER_IFRS.format(year, month)
            if year <= 98:
                url = Company_Monthly_Earning_Constant.OTC_EARNING_URL_BEFORE_IFRS.format(year, month)
        else:
            raise ValueError(Error_MSG.Company_Monthly_Earning_Error.COMPANY_TYPE_VALUE_ERROR)
        r = requests.get(url)
        r.encoding = 'big5'
        dfs = pd.read_html(StringIO(r.text), encoding=r.encoding)
        df = pd.concat([df for df in dfs if 5 < df.shape[1] <= 11])
        if Company_Monthly_Earning_Constant.REPORT_STRUCTURAL_LEVELS in dir(df.columns):
            df.columns = df.columns.get_level_values(1)
        else:
            df = df[list(range(0, 10))]
            column_index = df.index[(df[0] == Company_Monthly_Earning_Constant.COMPANY_NUMBER_COLUMN)][0]
            df.columns = df.iloc[column_index]
        df[Company_Monthly_Earning_Constant.CURRENT_MONTHLY_EARNING_COLUMN] = pd.to_numeric(df[Company_Monthly_Earning_Constant.CURRENT_MONTHLY_EARNING_COLUMN], 'coerce')
        df = df[~df[Company_Monthly_Earning_Constant.CURRENT_MONTHLY_EARNING_COLUMN].isnull()]
        df = df[df[Company_Monthly_Earning_Constant.COMPANY_NUMBER_COLUMN] != Company_Monthly_Earning_Constant.TOTAL_EARNING_COLUMN]
        df = df.reset_index(drop=True)
        df.drop(df.tail(1).index,inplace = True)
        return df
