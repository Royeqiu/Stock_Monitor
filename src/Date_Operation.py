import datetime
def turn_to_datetime(date_str:str):
    year, month, day = date_str.split('-')
    return datetime.datetime(int(year), int(month), int(day))

def get_current_date(type='datetime'):
    if type == 'datetime':
        return datetime.datetime.now()
    else:
        current_time = datetime.datetime.now()
        return current_time.year, current_time.month, current_time.day