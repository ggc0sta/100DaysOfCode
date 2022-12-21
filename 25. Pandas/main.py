# with open("weather_data.csv", mode="r") as file:
#     weather_data = file.readlines()

import csv

with open("weather_data.csv") as file:
    weather_data = csv.reader(file, delimiter=",")
    temp = []
    for row in weather_data:
        if row[1] != "temp":
            temp.append(int(row[1]))


# print(temp)


import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))  # data frame
# print(type(data["temp"]))  # series: single list or column
# print(data)
# print(data["temp"])


data_dict = data.to_dict()  # converting to dictionary
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# Calculating avg temperature
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # Retrieve data in columns
# print(data["condition"])
# print(data.condition)

# Retrieve data in rows
# print(data[data["day"] == "Monday"])
#
# # Which row of data had the max temp of the week
# print(data[data["temp"] == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print(monday)
fahrenheit = monday.temp * 9/5 + 32

print(fahrenheit)


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
