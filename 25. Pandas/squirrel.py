# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas as pd
import numpy as np

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data.columns)
# print(data["Primary Fur Color"].head())

# Treating Unknown Colors
data = data["Primary Fur Color"].replace(np.nan, "Unknown")

colors = data.unique()
count = []

for color in colors:
    color_count = len(data[data == color])
    count.append(color_count)

squirrel_dict = {
    "color": colors,
    "count": count
}

squirrel_df = pd.DataFrame(squirrel_dict)

print(squirrel_df)
squirrel_df.to_csv("squirrel_count.csv")
