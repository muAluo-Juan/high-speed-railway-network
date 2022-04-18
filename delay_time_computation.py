"""
Delay time computation for high-speed trains.
Input: the file path of high-speed train operation data after preprocessing
Output: the file after delay time computation
"""

import pandas as pd
import numpy as np
import datetime

from pandas import DataFrame

data = pd.read_csv('./high-speed train operation data after preprocessing.csv') # change to the path of high-speed train operation data after preprocessing
data_array = np.array(data)

# process the date
for i in data_array:
    i[1] = datetime.datetime.strptime(i[1], '%d/%m/%Y')
    i[1] = str(i[1])
    i[1] = i[1][:10]

# sort by train_name
idd = np.lexsort([data_array[:, 2]])
data_array = data_array[idd, :]

result = []
for i in data_array:
    # no arrival delay at departure station
    if i[4] == 1:
        arrival_delay = 0
    else:
        scheduled_arrive = int(i[5].split(':')[0]) * 60 + int(i[5].split(':')[1])
        actual_arrive = int(i[8].split(':')[0]) * 60 + int(i[8].split(':')[1])
        arrival_delay = actual_arrive - scheduled_arrive

    # no departure delay at terminal station
    if i[7] == '----' and i[4] != 1:
        departure_delay = 0
    else:
        scheduled_depart = int(i[6].split(':')[0]) * 60 + int(i[6].split(':')[1])
        actual_depart = int(i[9].split(':')[0]) * 60 + int(i[9].split(':')[1])
        departure_delay = actual_depart - scheduled_depart

    temp = [i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], arrival_delay, departure_delay]
    result.append(temp)

data_file = DataFrame(result)
data_file.to_csv('./high-speed train operation data with delay time.csv', mode='a', index=False, header=False)
