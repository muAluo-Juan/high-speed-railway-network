# Introduction
These files contains the codes for the data generation of "A high-speed railway network dataset from train operation records and weather data". The data processing is done in Python. 
# Code Structure
The codes contained in this repository are used to correct the abnormal train operation records, compute the delay time of the high-speed trains, compute the delayed train number of the railway stations and merge the multiple external influencing factors which affecting train operation.

The function of each code file are as follows:

data_preprocessing.py: It used to correct the high-speed train operation records.  

delay_time_computation.py: It used to compute delay time for high-speed trains.  

delay_number_computation.py: It used to compute delayed train number for railway stations.  

stations_mileage_computation.py: It used to compute adjacent stations mileage.  

traffic flow statistics.py: It used to statistics the train operation of the railway stations.

add direction and type.py: It used to add train direction and station type.  

add_weather_and_major_holidays_to_stations_delay_data.py: It used to add weather related data and major holidays to delay number data of railway stations.  

add_weather_and_major_holidays_to_trains_operation_data.py:  It used to add weather related data and major holidays to high-speed train operation data.
# Data Availability
Dataset processed with the codes can be found publicly at the following address:
<https://doi.org/10.6084/m9.figshare.15087882.v4>
