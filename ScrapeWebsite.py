#Module for scraping website data

#scrape_country takes a string country, the country of interest, and a string url, the web address of the website to scrape data from
#A dictionary is returned with the name of the country, the total deaths normalized by 1M, and the daily deaths
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
    
    countryDict = {}
    
    #The following website was used as a reference in writing this code: https://towardsdatascience.com/web-scraping-scraping-table-data-1665b6b2271c
    for row_num in range(len(body_rows)): #Loop through each row
        row = [] # this will hold entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            #Use regex to clean up data
            data = re.sub("(\xa0)|(\n)|,|/+","",row_item.text)
            row.append(data)
        # Check if current row corresponds to country of interest
        if country.lower() in row[1].lower():
            #print("Country: ", row[1])
            countryName = row[1]
            #print("Total Deaths (normalized by 1000000): ", str(int(row[4].strip())/1000000))
            totalDeaths = str(int(row[4].strip())/1000000)
            #print("Daily Deaths: ", row[5][1:])
            #If daily deaths is empty, there were 0 daily deaths
            if row[5][1:].strip() == "":
                dailyDeaths = "0"
            else:
                dailyDeaths = row[5][1:].strip()
                
            countryDict = {"name": countryName, "totaldeaths": totalDeaths, "dailydeaths": dailyDeaths}
            return countryDict
    #This point will not be hit it the country is found. If it is not, countryDict will be an empty dictionary
    return countryDict