import ScrapeWebsite
import json

#Use this script to gather data using the scrape_country function
#IMPORTANT: Make sure to change the filename to the current date before running (line 14)
countryData = []
countries = ["usa", "india", "france", "germany", "brazil", "s. korea", "japan", "italy", "uk", "russia", "turkey", "spain", "vietnam", "australia", "argentina", "netherlands", "taiwan", "iran", "mexico", "indonesia", "poland", "colombia", "austria", "portugal", "greece"]

for country in countries:
    countryData.append(ScrapeWebsite.scrape_country(country, "https://www.worldometers.info/coronavirus/"))

json_object = json.dumps(countryData)

with open("12-6-22.json", "w") as outfile: #filename in the format month-day-year
    outfile.write(json_object)
