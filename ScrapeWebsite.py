#Module for scraping website data

def scrape_country(country, url):
    import requests
    from bs4 import BeautifulSoup
    import re
    import json
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    tbls = soup.find_all("table")
    
    table1 = tbls[0]
    body = table1.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    
    headings = []
    for item in head.find_all("th"):
        item = (item.text).rstrip("\n")
        headings.append(item)
    
    all_rows = [] # will be a list for list for all rows
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            # row_item.text removes the tags from the entries
            # the following regex is to remove \xa0 and \n and comma from row_item.text
            # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,|/+","",row_item.text)
            #append aa to row - note one row entry is being appended
            row.append(aa)
        # append one row to all_rows
        if country.lower() in row[1].lower():
            print("Country: ", row[1])
            countryName = row[1]
            print("Total Deaths (normalized by 1000000): ", str(int(row[4].strip())/1000000))
            totalDeaths = str(int(row[4].strip())/1000000)
            print("Daily Deaths: ", row[5][1:])
            if row[5][1:].strip() == "":
                dailyDeaths = "0"
            else:
                dailyDeaths = row[5][1:].strip()
            
        all_rows.append(row)
        
    countryDict = {"name": countryName, "totaldeaths": totalDeaths, "dailydeaths": dailyDeaths}
    
    json_object = json.dumps(countryDict)
    print("Json string", json_object)
    
    filename = country + ".json"
    with open(filename, "w") as outfile:
        outfile.write(json_object)
    
    
    # usa = soup.find("td", class_="name align-left usa usa")
    # print(usa.text)
    # countries = soup.find_all("td", class_="name align-left usa usa")
    # country_elements = [a_element.parent.parent for a_element in countries]
    # for element in country_elements:
    #     name_element = element.find("a", class_="mt_a")
    #     print(name_element.text)
    #     # cases_element = element.find("td", class_="sorting_1")
    #     # print(cases_element.text)
    #     # print()
        
    

    return