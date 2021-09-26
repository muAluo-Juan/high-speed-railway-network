"""
Add weather related data and major holidays to delay number data of railway stations with station type
Input: the path of  delay number data of railway stations with station type
Output: railway stations delay data.csv
"""
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

def merge_dataFrame(left , right , on_list):

    result = pd.merge(left, right, how='inner', on=on_list)
    return result

def get_date(date):
    date1 = date.split(" ")[0]
    return date1

station_delay_data_path = '/delay number data of railway stations with station type.csv'
weather_data_path = '/weather related data.csv'
merge_data_save_path = '/railway stations delay data.csv'

delay_data = pd.read_csv(station_delay_data_path, low_memory=False)

delay_data['date_nyr'] = delay_data.apply(lambda x: get_date(x.start_time), axis=1)

weather_data = pd.read_csv(weather_data_path, low_memory=False)

merge_result = merge_dataFrame(delay_data, weather_data, on_list=['station_name', 'date_nyr'])

merge_result = merge_result.rename(columns={'up_arrival_delay': 'up_arrival_delay_number'})
merge_result = merge_result.rename(columns={'down_arrival_delay': 'down_arrival_delay_number'})
merge_result = merge_result.rename(columns={'up_departure_delay': 'up_departure_delay_number'})
merge_result = merge_result.rename(columns={'down_depature_delay': 'down_depature_delay_number'})
merge_result = merge_result.rename(columns={'county': 'district'})
merge_result = merge_result.rename(columns={'holiday': 'major_holiday'})
merge_result = merge_result.rename(columns={'temp': 'temperature'})


merge_result.to_csv(path_or_buf=merge_data_save_path, columns=['station_name',
    'province', 'city', 'district', 'start_time', 'end_time',
 'up_arrival_delay_number', 'down_arrival_delay_number', 'up_departure_delay_number',
  'down_depature_delay_number', 'wind', 'weather', 'temperature',
  'major_holiday'], encoding="ANSI", index=False)