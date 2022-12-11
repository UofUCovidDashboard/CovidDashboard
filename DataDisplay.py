import json
from bokeh.plotting import figure, show
from datetime import datetime as dt

#Load all of the data
days = [2, 3, 5, 6, 7, 8, 9, 10]
data = []
for i in range(len(days)):
    filename = "12-" + str(days[i]) + "-22.json"
    with open(filename) as file:
        data.append(json.load(file))

usaData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "USA":
            usaData.append(data[i][j]["dailydeaths"])
            
taiwanData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Taiwan":
            taiwanData.append(data[i][j]["dailydeaths"])
            
mexicoData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Mexico":
            mexicoData.append(data[i][j]["dailydeaths"])
            
italyData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Italy":
            italyData.append(data[i][j]["dailydeaths"])
            
germanyData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Germany":
            germanyData.append(data[i][j]["dailydeaths"])

dates = [dt(2022, 12, 2), dt(2022, 12, 3), dt(2022, 12, 5), dt(2022, 12, 6), dt(2022, 12, 7), dt(2022, 12, 8), dt(2022, 12, 9), dt(2022, 12, 10)]

p = figure(title="Daily COVID Death Rates by Country", x_axis_label='Dates', x_axis_type = "datetime", y_axis_label='Daily Deaths')
p.line(dates, usaData, legend_label="USA", color="blue", line_width=2)
p.line(dates, taiwanData, legend_label="Taiwan", color="red", line_width=2)
p.line(dates, mexicoData, legend_label="Mexico", color="green", line_width=2)
p.line(dates, italyData, legend_label="Italy", color="orange", line_width=2)
p.line(dates, germanyData, legend_label="Germany", color="purple", line_width=2)
p.legend.click_policy = "hide"

show(p)