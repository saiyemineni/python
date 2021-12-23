import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unq_colors = data['Primary Fur Color'].unique()
unq_colors = unq_colors[1:]
unq_colors_count = []
for color in unq_colors:
    color_count = len(data[data['Primary Fur Color'] == color])
    unq_colors_count.append(color_count)

unq_data = {"unqiue color": unq_colors,"count":unq_colors_count}
df_unq_data = pd.DataFrame(unq_data)
df_unq_data.to_csv("Squirrel_count.csv")
print(df_unq_data)

