# -*- coding: utf-8 -*-
"""
Data correction
Input: the file path of high-speed train operation data
Output: the file after preprocessing
"""
import pandas as pd
import numpy as np

from pandas import DataFrame

data = pd.read_csv('./high-speed train operation data.csv') # change the path to the high-speed train operation data path
print(len(data))
data_array = np.array(data)

for i in data_array:
    if i[4] == 1:
        i[8] = i[9]
        i[5] = i[6]

    if i[7] == '----' and i[4] != 1:
        i[9] = i[8]
        i[6] = i[5]

for i in data_array:
    if i[7] != '----':
        actual_arrive = int(i[8].split(':')[0]) * 60 + int(i[8].split(':')[1])
        actual_depart = int(i[9].split(':')[0]) * 60 + int(i[9].split(':')[1])
        if actual_depart < actual_arrive:
            actual_depart = actual_arrive + int((i[7].split('分钟'))[0])
            i[9] = str(int(actual_depart / 60)) + ':' + str(actual_depart % 60).zfill(2) + ':00'

result_file = DataFrame(data_array)
result_file.to_csv('./high-speed train operation data after preprocessing.csv', mode='a', index=False, header=False)
