import pandas as pd

data = pd.read_csv('weather_data.csv')
# print(data['temp'])


data_dict = data.to_dict()
print(data_dict)


temp_list = data['temp'].to_list()
print(temp_list)

avg_temp = data['temp'].mean()
print(f"Average temperature : {round(avg_temp,2)}")

max_temp = data['temp'].max()
print(f"Maximum temperature: {max_temp}")

print(data[data['day'] == 'Monday'])
monday = data[data['day'] == 'Monday']
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)