import json

#Test reading in JSON files

days = [2, 3, 5, 6, 7, 8]
data = []
for i in range(len(days)):
    filename = "12-" + str(days[i]) + "-22.json"
    with open(filename) as file:
        data.append(json.load(file))
        
#Resulting data structure is a list of lists of dictionaries. Each list of dictionaries corresponds
#to a different day of data, and each dictionary corresponds to a different country