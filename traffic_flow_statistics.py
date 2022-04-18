"""
Statistics on train operation of junction stations.
Input: the file path of junction stations
Output: junction stations data
"""
import pandas as pd
import numpy as np
import json

from pandas import DataFrame

train_delay_file = pd.read_csv('./junction stations.csv')
station_delay_file = pd.read_csv('./high-speed train operation data with delay time.csv')
train_delay_array = np.array(train_delay_file)
station_delay_arrray = np.array(station_delay_file)

with open('./junction station info.json') as f:
    junction_station = json.load(f)

result = []
for i in junction_station:
    up_arrival_delay_number  = 0
    down_arrival_delay_number = 0
    up_departure_delay_number = 0
    down_depature_delay_number = 0
    up_number = 0
    down_number = 0

    k = 0
    while station_delay_arrray[k][0] != i:
        if k == len(station_delay_arrray) - 1:
            break
        k += 1
    print(k)
    while station_delay_arrray[k][0] == i:
        province = station_delay_arrray[k][1]
        city = station_delay_arrray[k][2]
        district = station_delay_arrray[k][3]
        up_arrival_delay_number += station_delay_arrray[k][6]
        down_arrival_delay_number += station_delay_arrray[k][7]
        up_departure_delay_number += station_delay_arrray[k][8]
        down_depature_delay_number += station_delay_arrray[k][9]
        k += 1
        if k >= len(station_delay_arrray):
            break

    for j in train_delay_array:
        if j[3] == i:
            if j[2] == "上行":
                up_number += 1
            elif j[2] == "下行":
                down_number += 1
    temp = [i, province, city, district, up_number, down_number, up_arrival_delay_number, down_arrival_delay_number, up_departure_delay_number, down_depature_delay_number]
    result.append(temp)

result_file = DataFrame(result)
result_file.to_csv('./junction stations data.csv', mode='a', header=False, index=False)
