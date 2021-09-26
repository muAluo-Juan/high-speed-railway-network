"""
Add weather related data and major holidays to high-speed train operation data with delay time and train direction
Input: the path of high-speed train operation data with delay time and train direction
Output: high-speed trains operation data.csv
"""
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)

def merge_dataFrame(left , right , on_list):
    result = pd.merge(left, right, how='inner',on=on_list)
    return result

def get_date(date):
    date1 = date.split(" ")[0]
    return date1

station_delay_data_path = '/high-speed train operation data with delay time and train direction.csv'
weather_data_path = '/weather related data.csv'
merge_data_save_path = '/high-speed trains operation data.csv'

delay_data = pd.read_csv(station_delay_data_path, low_memory=False)

delay_data['date_nyr'] = delay_data.apply(lambda x: get_date(x.date), axis=1)

weather_data = pd.read_csv(weather_data_path, low_memory=False)

merge_result = merge_dataFrame(delay_data, weather_data, on_list=['station_name', 'date_nyr'])

merge_result = merge_result.rename(columns={'date_nyr': 'date'})

merge_result.to_csv(path_or_buf=merge_data_save_path, columns=["date", "train_num", "train_direction",
"station_name", "station_order", "scheduled_arrival_time", "scheduled_departure_time", "stop_time", "actual_arrival_time",
"actual_departure_time", "arrival_delay", "departure_delay", "wind", "weather", "temperature", "major_holiday"], index=False)











