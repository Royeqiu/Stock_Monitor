import datetime
def turn_to_datetime(date_str:str):
    year, month, day = date_str.split('-')
    return datetime.datetime(int(year), int(month), int(day))