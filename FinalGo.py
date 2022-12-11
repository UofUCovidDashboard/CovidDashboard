# Color Palette:
# 205072 dark green
# 329D9C medium blue green 
# 56C596 jade
# 7BE495 lime ish 
# CFF4D2 key limeish




# Covid Dashboard needs:
## Necessary imports
import json
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure, show
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
from bokeh.plotting import figure, output_file, show
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
countryNames = ['USA', 'India', 'France', 'Germany', 'Brazil', 'S. Korea', 'Japan', 'Italy', 'UK', 'Russia', 'Turkey', 'Spain', 'Vietnam', 'Australia', 'Argentina', 'Netherlands', 'Taiwan', 'Iran', 'Mexico', 
'Indonesia', 'Poland', 'Colombia', 'Austria', 'Portugal', 'Greece']
# REMOVE THIS AND FIX WITH THE AVERAGE DAILY DEATH DATA
temporaryDailyData = [12, 14, 15, 17, 18, 19, 30, 34, 35, 36, 46, 24, 25, 47, 37, 46, 25, 25, 25, 24, 24,50,46,3,24]

# Pull data for a few countries. We chose the US, Taiwan, Italy, Mexico and Germany.

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
# Plot 1 should contain an overview of all the countries. It will be averaged over all the data. I named it "All Country"

allCountry = figure(x_range = countryNames, height = 250,width = 1500, title="Average Daily Deaths Per Country Over a One Week Period",
                    toolbar_location = None,tools="",x_axis_label='Country', y_axis_label='Daily Deaths')
allCountry.vbar(x = countryNames,top = temporaryDailyData,width= 0.5, color = "#205072")
allCountry.xgrid.grid_line_color = None
allCountry.y_range.start = 0
allCountry.background_fill_color = "#56C596"
allCountry.outline_line_color = "#CFF4D2"
allCountry.outline_line_width = 3

# Plot 2 should contain a zoomed in view of the selected countries and their details. I named it "Zoomed"
shortList = ['USA','Taiwan','Mexico','Italy','Germany']
dates_short = ["12-2","12-3","12-5","12-6","12-7","12-8","12-9","12-10"]
dummyDailyData = {'death rate': shortList,
                  '12-2'    : [5, 7, 80, 34, 45],
                  '12-3'    : [5, 7, 80, 34, 45],
                  '12-5'    : [5, 7, 80, 34, 45],
                  '12-6'    : [5, 7, 80, 34, 45],
                  '12-7'    : [5, 7, 80, 34, 45],
                  '12-8'    : [5, 7, 80, 34, 45],
                  '12-9'    : [45, 37, 0, 84, 5],
                  '12-10'    : [5, 7, 80, 34, 45]
                                                    }
dummyNormData = {'death rate': shortList,
                 '12-2'    : [5, 7, 80, 34, 45],
                  '12-3'    : [5, 7, 80, 34, 45],
                  '12-5'    : [5, 7, 80, 34, 45],
                  '12-6'    : [5, 7, 80, 34, 45],
                  '12-7'    : [5, 7, 80, 34, 45],
                  '12-8'    : [5, 7, 80, 34, 45],
                  '12-9'    : [45, 37, 0, 84, 5],
                  '12-10'    : [5, 7, 80, 34, 45]
                                                    }

zoomed = figure(y_range = shortList, title="Detailed COVID Death Rate Data for Five Countries",height = 400,width= 500, 
                x_axis_label='Country', y_axis_label='Daily Deaths')
zoomed.hbar_stack(dates_short,y = 'Country',width= 0.3, 
                  source = ColumnDataSource(dummyDailyData))
zoomed.hbar_stack(dates_short,y = 'Country',width= 0.3, 
                  source = ColumnDataSource(dummyNormData))
zoomed.xgrid.grid_line_color = None
zoomed.background_fill_color = "#7BE495"
zoomed.outline_line_color = "#CFF4D2"
zoomed.outline_line_width = 2

# Plot 3 should contain an interactive plot with a detailed view. The legend is interactable. I named it "Interactive"
interactive = figure(title="Daily COVID Death Rates by Country", x_axis_label='Dates', x_axis_type = "datetime", y_axis_label='Daily Deaths',
                     height = 400, width = 500)
interactive.line(dates, usaData, legend_label="USA", color="black", line_width=2)
interactive.line(dates, taiwanData, legend_label="Taiwan", color="#008B8B", line_width=2)
interactive.line(dates, mexicoData, legend_label="Mexico", color="#FFF8DC", line_width=2)
interactive.line(dates, italyData, legend_label="Italy", color="#6495ED", line_width=2)
interactive.line(dates, germanyData, legend_label="Germany", color="#00FA9A", line_width=2)
#interactive.legend.orientation = "horizontal"
#interactive.legend.location= "top_center"
interactive.legend.click_policy = "hide"
interactive.background_fill_color = "#7BE495"
interactive.outline_line_color = "#CFF4D2"
interactive.outline_line_width = 2

# Plot 4 should contain historical data over an adjustable period. It needs a slider to adjust the range. I named it "Historical"

historical = figure(title="Historical Daily Death Rate over a Week Long Period", x_axis_label='Dates', x_axis_type = "datetime", y_axis_label='Daily Deaths',
                    height = 400,width = 500)
historical.line(dates, usaData, legend_label="USA", color="blue", line_width=2)
historical.background_fill_color = "#7BE495"
historical.outline_line_color = "#CFF4D2"
historical.outline_line_width = 2
# set up RangeSlider
date_range_slider = DateRangeSlider(
    title ="Adjust the data range with the slider",
    value=(dates[2], dates[5]),
    start=dates[0], end=dates[7],
    bar_color ="#56C596",
    step = 1,
)

date_range_slider.js_link("value", historical.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", historical.x_range, "end", attr_selector=1)


# This section contains the details for the dashboard as a whole. 
overallTitle = Div(
    text="""
          <p>Covid Dashboard 5250 Fall 2022 </p>
          """,
    width=750,
    height=10,
    margin = (5,650,5,650) 
)
spacer = Div(
    text="""
          <p>      </p>
          <p>     <p>
          """,
    width=500,
    height=10,
    margin = (25,25,25,25) 
)
LegendInstructions = Div(
    text="""
          <p> "Toggle data on and off in the Daily Covid Rates by</p>
          <p> Country graph by clicking the data on the legend"<p>
          """,
    width=750,
    height=10,
    margin = (5,150,5,250) 
)
overall = layout([
    [overallTitle],
    [allCountry],
    [historical, zoomed,interactive],
    [spacer, date_range_slider, spacer, LegendInstructions]
])

show(overall)