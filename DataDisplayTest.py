import json
from bokeh.plotting import figure, show

from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner

#Test reading in JSON files

# days = [2, 3, 5, 6, 7, 8]
# data = []
# for i in range(len(days)):
#     filename = "12-" + str(days[i]) + "-22.json"
#     with open(filename) as file:
#         data.append(json.load(file))
        
#Resulting data structure is a list of lists of dictionaries. Each list of dictionaries corresponds
#to a different day of data, and each dictionary corresponds to a different country

#Testing Bokeh
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
# p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
# p.line(x, y, legend_label="Temp.", line_width=2)
# show(p)

# prepare some data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

# create plot with circle glyphs
p = figure(x_range=(1, 9), width=500, height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# set up textarea (div)
div = Div(
    text="""
          <p>Select the circle's size using this control element:</p>
          """,
    width=200,
    height=30,
)

# set up spinner
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,
    width=200,
)
spinner.js_link("value", points.glyph, "size")

# set up RangeSlider
range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
   
)
range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# create layout
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ]
)

# show result
show(layout)

#Use layout() to set up page
#Use Div() for text
#Use Multichoice() for selecting countries to display
#Use Dropdown() for selecting number of days? or Select()?
#Use Line() to display plot

