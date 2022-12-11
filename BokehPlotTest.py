from bokeh.plotting import figure, show
import json

'''
file = open('12-2-22.json')

data = json.load(file)
totaldeaths = []
for i in data:
    # print(i)
    totaldeaths.append(data[:4])
    print(totaldeaths)
    
file.close()

x = [1,2,3,4,5]
y = [6,7,2,4,5]

# create a new plot with a title and axis labels
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
# add circle renderer with additional arguments
circle = p.circle(
    x,
    y,
    legend_label="Objects",
    fill_color="red",
    fill_alpha=0.5,
    line_color="blue",
    size=80,
)

glyph = circle.glyph
glyph.fill_color = "blue"
# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)
# display legend in top left corner (default is top right corner)

p.legend.location = "top_left"
# add a title to your legend
p.legend.title = "Obervations"
# change appearance of legend text
p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"
# change border and background of legend
p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.8
p.legend.background_fill_color = "navy"
p.legend.background_fill_alpha = 0.2

# add line renderer with a legend
p.line(x, y, legend_label="Temp.", line_width=2)

# change headline location to the left
p.title_location = "left"

# change headline text
p.title.text = "Changing headline text example"

# style the headline
p.title.text_font_size = "25px"
p.title.align = "right"
p.title.background_fill_color = "darkgrey"
p.title.text_color = "white"
# show the results
show(p)



# prepare some data
x = [1, 2, 3, 4, 5]
y1 = [6, 7, 2, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [4, 5, 5, 7, 2]

# create a new plot with a title and axis labels
s = figure(title="Multiple line example", x_axis_label='x', y_axis_label='y')

# add multiple renderers
s.line(x, y1, legend_label="Temp.", color="blue", line_width=2)
# s.line(x, y2, legend_label="Rate", color="red", line_width=2)
s.line(x, y3, legend_label="Objects", color="green", line_width=2)
s.circle(x, y3, legend_label="Objects", color="yellow", size=12)
s.vbar(x=x, top=y2, legend_label="Rate", width=0.5, bottom=0, color="red")
show(s)


# box notation
from bokeh.models import BoxAnnotation
import random
# generate some data (1-50 for x, random values for y)
x = list(range(0, 51))
y = random.sample(range(0, 100), 51)

# create new plot
p = figure(title="Box annotation example")


# add line renderer
line = p.line(x, y, line_color="#000000", line_width=2)

low_box = BoxAnnotation(top=20, fill_alpha=0.2, fill_color="#F0E442")
mid_box = BoxAnnotation(bottom=20, top=80, fill_alpha=0.2, fill_color="#009E73")
high_box = BoxAnnotation(bottom=80, fill_alpha=0.2, fill_color="#F0E442")

p.add_layout(low_box)
p.add_layout(mid_box)
p.add_layout(high_box)

show(p)

# themes 
from bokeh.io import curdoc
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# apply theme to current document
curdoc().theme = "dark_minimal"

# create a plot
p = figure(sizing_mode="stretch_width", max_width=500, height=250)

# add a renderer
p.line(x, y)

# show the results
show(p)

from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with a specific size
p = figure(
    title="Plot sizing example",
    width=350,
    height=250,
    x_axis_label="x",
    y_axis_label="y",
)

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)

# show the results
show(p)

from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# create a new plot with a specific size
p = figure(
    title="Plot resizing example",
    width=350,
    height=250,
    x_axis_label="x",
    y_axis_label="y",
    y_range=(0, 25),
    sizing_mode="stretch_width",
    max_width=500,
)

# change plot size
p.width = 450
p.height = 150

# add circle renderer
circle = p.circle(x, y, fill_color="red", size=15)
# change some things about the x-axis
p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"

# change some things about the y-axis
p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

# change things on all axes
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6
# show the results
show(p)

from bokeh.plotting import figure, show

# prepare some data
x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y0 = [i**2 for i in x]
y1 = [10**i for i in x]
y2 = [10**(i**2) for i in x]

# create a new plot with a logarithmic axis type
p = figure(
    title="Logarithmic axis example",
    sizing_mode="stretch_width",
    height=300,
    max_width=500,
    y_axis_type="log",
    y_range=[0.001, 10 ** 11],
    x_axis_label="sections",
    y_axis_label="particles",
)

# add some renderers
p.line(x, x, legend_label="y=x")
p.circle(x, x, legend_label="y=x", fill_color="white", size=8)
p.line(x, y0, legend_label="y=x^2", line_width=3)
p.line(x, y1, legend_label="y=10^x", line_color="red")
p.circle(x, y1, legend_label="y=10^x", fill_color="red", line_color="red", size=6)
p.line(x, y2, legend_label="y=10^x^2", line_color="orange", line_dash="4 4")

# show the results
show(p)


import random
from datetime import datetime, timedelta

from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
from bokeh.plotting import figure, show

# generate list of dates (today's date in subsequent weeks)
dates = [(datetime.now() + timedelta(day * 7)) for day in range(0, 26)]

# generate 25 random data points
y = random.sample(range(0, 100), 26)

# create new plot
p = figure(
    title="datetime axis example",
    x_axis_type="datetime",
    sizing_mode="stretch_width",
    max_width=500,
    height=250,
)

# add renderers
p.circle(dates, y, size=8)
p.line(dates, y, color="navy", line_width=1)

# format axes ticks
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00")
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# show the results
show(p)

import random

from bokeh.plotting import figure, show

# generate some data (1-10 for x, random values for y)
x = list(range(0, 26))
y = random.sample(range(0, 100), 26)

# generate list of rgb hex colors in relation to y
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

# create new plot
p = figure(
    title="Vectorized colors example",
    sizing_mode="stretch_width",
    max_width=500,
    height=250,
)

# add circle and line renderers
line = p.line(x, y, line_color="blue", line_width=1)
circle = p.circle(x, y, fill_color=colors, line_color="blue", size=15)

# show the results
show(p)
'''''
import numpy as np

from bokeh.plotting import figure, show

# generate some data
N = 1000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100

# generate radii and colors based on data
radii = y / 100 * 2
colors = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]

# create a new plot with a specific size
p = figure(
    title="Vectorized colors and radii example",
    sizing_mode="stretch_width",
    max_width=500,
    height=250,
)

# add circle renderer
p.circle(
    x,
    y,
    radius=radii,
    fill_color=colors,
    fill_alpha=0.6,
    line_color="lightgrey",
)

# show the results
show(p)