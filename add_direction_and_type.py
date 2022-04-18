"""
Train direction and station type adding.
Input: the file path of high-speed train operation data with delay time and delay number data of railway stations
Output: high-speed train operation data with delay time and train direction, delayed train number data of railway stations with station type
"""
import pandas as pd
import numpy as np
import json

from pandas import DataFrame

data = pd.read_csv('./high-speed train operation data with delay time.csv')
data_array = np.array(data)
station_delay_file = pd.read_csv('./delay number data of railway stations.csv')
station_delay_array = np.array(station_delay_file)

with open('./junction station info.json') as f:
    junction_station = json.load(f)

result1 = []
result2 = []
for i in station_delay_array:
    station_type = "非枢纽站"
    for j in junction_station:
        if i[0] == j:
            station_type = "枢纽站"
    temp = [i[0], station_type, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]]
    result1.append(temp)

for j in data_array:
    if int(i[2].split('G')[1]) % 2 == 0:
        train_direction = "上行"
    else:
        train_direction = "下行"
    temp = [i[0], i[1], train_direction, i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]]
    result2.append(temp)

result_file1 = DataFrame(result1)
result_file1.to_csv('./delay number data of railway stations with station type.csv', mode='a', header=False, index=False)
result_file2 = DataFrame(result2)
result_file2.to_csv('./high-speed train operation data with delay time and train direction.csv', mode='a', header=False, index=False)
