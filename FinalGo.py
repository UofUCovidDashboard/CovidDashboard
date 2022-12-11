# Color Palette:
# 205072 dark green
# 329D9C medium blue green 
# 56C596 jade
# 7BE495 lime ish 
# CFF4D2 key limeish

# Covid Dashboard needs:
## Necessary imports
import json
from bokeh.plotting import figure
from bokeh.palettes import GnBu3, OrRd3
from datetime import datetime as dt
from bokeh.layouts import gridplot
from bokeh.layouts import layout
from bokeh.io import show
from bokeh.models import CustomJS, DateRangeSlider
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.layouts import row
from bokeh.layouts import column
from bokeh.plotting import figure, output_file, show
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.models import LinearAxis, Range1d
from bokeh.models import Range1d

## pull the data from the data scrape json files
days = [2, 3, 5, 6, 7, 8, 9, 10]
data = []
for i in range(len(days)):
    filename = "12-" + str(days[i]) + "-22.json"
    with open(filename) as file:
        data.append(json.load(file))
# pull the daily data out
dailyData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        dailyData.append(data[i][j]["dailydeaths"])
# pull the normalized data out 
totalData = []
for i in range(len(data)):
    for j in range(len(data[i])):
        totalData.append(data[i][j]["totaldeaths"])

## define the list of country names 
countryNames = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Taiwan', 'Mexico']
# REMOVE THIS AND FIX WITH THE AVERAGE DAILY DEATH DATA
dailyAverage = []
normalizedAverage = []
temporaryDailyData = [12, 14, 15, 17, 18, 19, 30, 34, 35, 36, 46, 24, 25, 47, 37, 46, 25, 25, 25, 24, 24, 50, 46, 3, 24]

# Pull data for a few countries. We chose the US, Taiwan, Italy, Mexico and Germany.

usaData = []
usaNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "USA":
            usaData.append(float(data[i][j]["dailydeaths"]))
            usaNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(usaData) / 8)
normalizedAverage.append(sum(usaNormalized) / 8)

indiaData = []
indiaNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "India":
            indiaData.append(float(data[i][j]["dailydeaths"]))
            indiaNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(indiaData) / 8)
normalizedAverage.append(sum(indiaNormalized) / 8)

franceData = []
franceNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "France":
            franceData.append(float(data[i][j]["dailydeaths"]))
            franceNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(franceData) / 8)
normalizedAverage.append(sum(franceNormalized) / 8)

germanyData = []
germanyNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Germany":
            germanyData.append(float(data[i][j]["dailydeaths"]))
            germanyNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(germanyData) / 8)
normalizedAverage.append(sum(germanyNormalized) / 8)

brazilData = []
brazilNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Brazil":
            brazilData.append(float(data[i][j]["dailydeaths"]))
            brazilNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(brazilData) / 8)
normalizedAverage.append(sum(brazilNormalized) / 8)

koreaData = []
koreaNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "S. Korea":
            koreaData.append(float(data[i][j]["dailydeaths"]))
            koreaNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(koreaData) / 8)
normalizedAverage.append(sum(koreaNormalized) / 8)

japanData = []
japanNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Japan":
            japanData.append(float(data[i][j]["dailydeaths"]))
            japanNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(japanData) / 8)
normalizedAverage.append(sum(japanNormalized) / 8)

italyData = []
italyNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Italy":
            italyData.append(float(data[i][j]["dailydeaths"]))
            italyNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(italyData) / 8)
normalizedAverage.append(sum(italyNormalized) / 8)

ukData = []
ukNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "UK":
            ukData.append(float(data[i][j]["dailydeaths"]))
            ukNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(ukData) / 8)
normalizedAverage.append(sum(ukNormalized) / 8)

russiaData = []
russiaNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Russia":
            russiaData.append(float(data[i][j]["dailydeaths"]))
            russiaNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(russiaData) / 8)
normalizedAverage.append(sum(russiaNormalized) / 8)

turkeyData = []
turkeyNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Turkey":
            turkeyData.append(float(data[i][j]["dailydeaths"]))
            turkeyNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(turkeyData) / 8)
normalizedAverage.append(sum(turkeyNormalized) / 8)

taiwanData = []
taiwanNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Taiwan":
            taiwanData.append(float(data[i][j]["dailydeaths"]))
            taiwanNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(taiwanData) / 8)
normalizedAverage.append(sum(taiwanNormalized) / 8)

mexicoData = []
mexicoNormalized = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j]["name"] == "Mexico":
            mexicoData.append(float(data[i][j]["dailydeaths"]))
            mexicoNormalized.append(float(data[i][j]["totaldeaths"]))
dailyAverage.append(sum(mexicoData) / 8)
normalizedAverage.append(sum(mexicoNormalized) / 8)


dates = [dt(2022, 12, 2), dt(2022, 12, 3), dt(2022, 12, 5), dt(2022, 12, 6), dt(2022, 12, 7), dt(2022, 12, 8), dt(2022, 12, 9), dt(2022, 12, 10)]

# Plot 1 should contain an overview of all the countries. It will be averaged over all the data. I named it "All Country"
allCountry = figure(x_range = countryNames, height = 200,width = 1500, title="Average Daily Deaths Per Country Over a One Week Period",
                    toolbar_location = None,tools="",x_axis_label='Country', y_axis_label='Daily Deaths')
allCountry.vbar(x = countryNames,top = dailyAverage,width= 0.5, color = "#205072")
allCountry.xgrid.grid_line_color = None
allCountry.y_range.start = 0
allCountry.background_fill_color = "#56C596"
allCountry.outline_line_color = "#CFF4D2"
allCountry.outline_line_width = 3

# Plot 2 should contain a zoomed in view of the selected countries and their details. I named it "Zoomed"
shortLists = ['USA','Taiwan','Mexico','Italy','Germany']
typeDatas = ['Daily','Normalized']

data = {'Countries'  : shortLists,
        'Daily'      : [2, 1, 4, 3, 2],
        'Normalized' : [5, 3, 3, 2, 4]}

palette = ["#c9d9d3", "#718dbf", "#e84d60"]

# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (shortList, typeData) for shortList in shortLists for typeData in typeDatas ]
counts = sum(zip(data['Daily'], data['Normalized']), ()) # like an hstack

source = ColumnDataSource(data=dict(x=x, counts=counts))

zoomed = figure(x_range=FactorRange(*x), height=300, width = 750, title="Detailed COVID Stats for Select Countries", y_axis_label='Deaths')

zoomed.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=typeDatas, start=1, end=2))
zoomed.yaxis.axis_label = "Daily Death Rates"
zoomed.y_range = Range1d(-10,250)
zoomed.extra_y_ranges['foo'] = Range1d(0,1)
# FIX THIS
ax2 = LinearAxis(y_range_name = "foo", axis_label = "Normalized Ratio")
zoomed.add_layout(ax2, 'left')
zoomed.y_range.start = 0
zoomed.x_range.range_padding = 0.1
zoomed.xaxis.major_label_orientation = 1
zoomed.xgrid.grid_line_color = None



# Plot 3 should contain an interactive plot with a detailed view. The legend is interactable. I named it "Interactive"
interactive = figure(title="Daily COVID Death Rates for Select Countries", x_axis_label='Dates', x_axis_type = "datetime", y_axis_label='Daily Deaths',
                     height = 300, width = 750)
interactive.line(dates, usaData, legend_label="USA", color="black", line_width=2)
interactive.line(dates, taiwanData, legend_label="Taiwan", color="#008B8B", line_width=2)
interactive.line(dates, mexicoData, legend_label="Mexico", color="#FFF8DC", line_width=2)
interactive.line(dates, italyData, legend_label="Italy", color="#6495ED", line_width=2)
interactive.line(dates, germanyData, legend_label="Germany", color="#00FA9A", line_width=2)
interactive.y_range = Range1d(-10,250)
interactive.legend.click_policy = "hide"
interactive.background_fill_color = "#7BE495"
interactive.outline_line_color = "#CFF4D2"
interactive.outline_line_width = 2

# Plot 4 should contain historical data over an adjustable period. It needs a slider to adjust the range. I named it "Historical"
dummyNormData = [0.3, 0.4, 0.5, 0.6, 0.7]
# REPLACE WITH NORMALIZED DATA FOR 5 COUNTRIES
historical = figure(title="Historical Normalized Death Rate Over a Week Long Period", x_axis_label='Dates', x_axis_type = "datetime", y_axis_label='Normalized Death Rate',
                    height = 250,width = 1500)
historical.line(dates, dummyNormData, legend_label="USA", color="blue", line_width=2)
historical.background_fill_color = "#7BE495"
historical.outline_line_color = "#CFF4D2"
historical.outline_line_width = 2
# set up RangeSlider
date_range_slider = DateRangeSlider(
    value=(dates[2], dates[5]),
    start=dates[0], end=dates[7],
    bar_color ="#56C596",
    step = 1,
    margin = (5,5,25,5)
)

date_range_slider.js_link("value", historical.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", historical.x_range, "end", attr_selector=1)


# This section contains the details for the dashboard as a whole. 
overallTitle = Div(
    text="""
          <b>Covid Dashboard 5250 Fall 2022 </b>
          """,
    width=750,
    height=10,
    margin = (5,650,25,650) 
    
)
OverallStatistics = Div(
    text="""
          <b>  Global Statistics</b>
          """,
    width=105,
    height=15,
    margin = (5,650,5,700),
    background = "#CFF4D2",
)
SelectStatistics = Div(
    text="""
          <b> Statistics for Select Countries</b>
          """,
    width=200,
    height=10,
    margin = (5,200,15,670) 
)
LegendInstructions = Div(
    text="""
          <i> Toggle data on and off in the "Daily Covid Rates" by Country graph by clicking the data on the legend.</i>
          """,
    width=750,
    height=10,
    margin = (5,5,5,850) 
)
SliderInstructions = Div(
    text="""
          <i>Adjust the data range with the slider:</i>
          """,
    width=250,
    height=10,
    margin = (5,5,5,500) 
)
overall = layout([
    [overallTitle],
    [OverallStatistics],
    [allCountry],
    [historical],
    [SliderInstructions, date_range_slider],
    [SelectStatistics],
    [zoomed,interactive],
    [LegendInstructions],
    
])

show(overall)