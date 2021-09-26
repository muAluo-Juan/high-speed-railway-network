"""
Delay time computation for high-speed trains.
Input: the path of high-speed train operation data with delay time
Output: delay number data of railway stations
"""
import datetime
import pandas as pd
import numpy as np
import time
from pandas import DataFrame

data = pd.read_csv('/high-speed train operation data with delay time.csv')   # corresponding path

# station_delay_array: array used by each station to count the number of delays in the time slice
duplicate = data.drop_duplicates('station_number')
duplicate = np.array(duplicate)
station_delay_array = []
for i in duplicate:
    begin_date = datetime.datetime.strptime('2019-10-8 0:00:00', "%Y-%m-%d %H:%M:%S")
    end_date = datetime.datetime.strptime('2020-1-27 23:00:00', "%Y-%m-%d %H:%M:%S")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d %H:%M:%S")
        begin_date += datetime.timedelta(hours=1)
        station_time_array = [i[4], i[3], date_str, begin_date.strftime("%Y-%m-%d %H:%M:%S"), 0, 0, 0, 0]
        station_delay_array.append(station_time_array)

data_array = np.array(data)
for i in data_array:
    # 到达延迟
    if i[11] > 0:
        arrive_time = time.strptime(i[0] + ' ' + i[6], '%Y-%m-%d %H:%M:%S')
        arrive_timestamp = time.mktime(arrive_time)
        for j in station_delay_array:
            start_time = time.strptime(j[2], '%Y-%m-%d %H:%M:%S')
            start_timestamp = time.mktime(start_time)
            end_time = time.strptime(j[3], '%Y-%m-%d %H:%M:%S')
            end_timestamp = time.mktime(end_time)
            if j[0] == i[4] and arrive_timestamp >= start_timestamp and arrive_timestamp < end_timestamp:
                if int(i[2].split('G')[1]) % 2 == 0:
                    j[4] += 1
                else:
                    j[5] += 1
                break

    # 出发延迟
    if i[12] > 0:
        depart_time = time.strptime(i[0] + ' ' + i[7], '%Y-%m-%d %H:%M:%S')
        depart_timestamp = time.mktime(depart_time)
        for j in station_delay_array:
            start_time = time.strptime(j[2], '%Y-%m-%d %H:%M:%S')
            start_timestamp = time.mktime(start_time)
            end_time = time.strptime(j[3], '%Y-%m-%d %H:%M:%S')
            end_timestamp = time.mktime(end_time)
            if j[0] == i[4] and depart_timestamp >= start_timestamp and depart_timestamp < end_timestamp:
                if int(i[2].split('G')[1]) % 2 == 0:
                    j[6] += 1
                else:
                    j[7] += 1
                break

data_target_file = DataFrame(station_delay_array)
data_target_file.to_csv('/delay number data of railway stations.csv')