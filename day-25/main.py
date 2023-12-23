# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data.condition)

# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# temp_celsius = monday.temp[0]
# temp_fahrenheit = (9*temp_celsius)/5 + 32
# print(temp_fahrenheit)

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231223.csv")
colors_list = squirrel_data["Primary Fur Color"]

colors_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [
        len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]),
        len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]),
        len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]),
    ]
}

data = pandas.DataFrame(colors_dict)
data.to_csv("colors.csv")
