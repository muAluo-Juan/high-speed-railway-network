"""
Adjacent stations mileage computation.
Input: the path of high-speed trains mileage data
Output: adjacent railway stations mileage data
"""
import pandas as pd
import numpy as np
from pandas import DataFrame

file_1 = pd.read_csv('./high-speed trains mileage data1.csv')  # change to the path of high-speed trains mileage data
file_2 = pd.read_csv('./high-speed trains mileage data2.csv')
file_3 = pd.read_csv('./high-speed trains mileage data3.csv')
tt = pd.read_csv('./alllines.csv') # change to the path of all operation lines

data_1 = np.array(file_1)
data_2 = np.array(file_2)
data_3 = np.array(file_3)
tt_data = np.array(tt)

result = []
i = 0
while i < len(data_1):
    if data_1[i][1] != 1:
        dis = data_1[i][3] - data_1[i-1][3]
        from_station = data_1[i-1][2]
        to_station = data_1[i][2]

        train_name = data_1[i][0].split('/')[0]
        at = 0
        for j in tt_data:
            if j[0] == train_name:
                at = 1
                break
        if at == 0:
            train_name = data_1[i][0].split('/')[1]
        else:
            train_name = data_1[i][0].split('/')[0]

        if int(train_name.split('G')[1]) % 2 == 0:
            direction = "上行"
        else:
            direction = "下行"

        temp = [from_station, to_station, dis, direction]
        print(temp)
        result.append(temp)
    i += 1

i = 0
while i < len(data_2):
    if data_2[i][1] != 1:
        dis = data_2[i][3] - data_2[i - 1][3]
        from_station = data_2[i - 1][2]
        to_station = data_2[i][2]

        train_name = data_2[i][0].split('/')[0]
        at = 0
        for j in tt_data:
            if j[0] == train_name:
                at = 1
                break
        if at == 0:
            train_name = data_2[i][0].split('/')[1]
        else:
            train_name = data_2[i][0].split('/')[0]

        if int(train_name.split('G')[1]) % 2 == 0:
            direction = "上行"
        else:
            direction = "下行"
        temp = [from_station, to_station, dis, direction]
        print(temp)
        result.append(temp)
    i += 1

i = 0
while i < len(data_3):
    if data_3[i][1] != 1:
        dis = data_3[i][3] - data_3[i - 1][3]
        from_station = data_3[i - 1][2]
        to_station = data_3[i][2]
        train_name = data_3[i][0].split('/')[0]
        at = 0
        for j in tt_data:
            if j[0] == train_name:
                at = 1
                break
        if at == 0:
            train_name = data_3[i][0].split('/')[1]
        else:
            train_name = data_3[i][0].split('/')[0]

        if int(train_name.split('G')[1]) % 2 == 0:
            direction = "上行"
        else:
            direction = "下行"
        temp = [from_station, to_station, dis, direction]
        print(temp)
        result.append(temp)
    i += 1

result_file = DataFrame(result)
result_file.to_csv('./adjacent railway stations mileage data.csv', mode='a', index=False, header=False)

