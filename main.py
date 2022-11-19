# 227

# with open('weather_data.csv') as data_file:
#   data = data_file.readline()
#   print(data)

# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data['temp'].mean())
# print(data['temp'].max())

# # 228
# ##Get Data in Columns
# print(data['Condition'])
# print(data.Condition)

# ##Get Data in Row
# print(data[data.temp == data.temp.max()])

# ##Create a dataframe from scratch
# data_dict = {'students': ['Aida', 'Jason', 'Angela'], 'scores': [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data.csv')

# 229
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count':
    [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
