# reader=open('weather_data.csv')
# file=reader.read()
# row_list=[]
# col_list=list()
# data=""
# for item in file:
#     data+=item
#     if item == ',':
#         col_list.append(data)
#         data=""
#     elif item == '\n':
#         data=data[:-1]
#         col_list.append(data)
#         row_list.append(col_list)
#         col_list=[]
#         data=""
# print(row_list)
# reader.close()

# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#     for temp in temperature:
#         print(temp)

import pandas as pd
data=pd.read_csv("weather_data.csv")
# print(data['temp'])
# data_dict=data.to_dict()
# print(data_dict)
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition)

#Get Data in Row
#print(data[data.temp==data.temp.max()])
print(data.loc[data.temp==data.temp.max(),['day','temp']])
