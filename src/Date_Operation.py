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

def get_previous_date(date_range):
    year,month,_ = get_current_date(type = 'other')
    res = []
    for i in range(1,date_range):
        month_delta = month - i
        year_delta = year
        while month_delta <= 0:
            month_delta += 12
            year_delta -= 1

        res.append(date_string_formating(year_delta,month_delta,level=2))
    return res

def date_string_formating(year:str,month:str,day:str = '00',level=2):

    if type(year) != str:
        year = str(year)
    if type(month) != str:
        month = str(month)
    if type(day) != str:
        day = str(day)
    if int(year) < 1911:
        year = str(int(year) + 1911)

    if len(month) == 1:
        month = '0{}'.format(month)
    if level == 2:
        return '-'.join([year,month])
    assert level == 3 and day != '00', 'input of day is null.'
    if len(day) == 1:
        day = '0{}'.format(day)
    return '-'.join([year,month,day])