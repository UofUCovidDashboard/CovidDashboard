import json
from bokeh.plotting import figure, show

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
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label="Temp.", line_width=2)
show(p)

