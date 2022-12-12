# CovidDashboard
Julia Gatto, Zach Lin, Aleks Vazquez

Web Scraping script: ScrapeWebsiteTest.py
Dashboard script: FinalGo.py

Instructions for running web scraping code:
From the ScrapeWebsite module, the scrape_country function is meant to be called with this link: https://www.worldometers.info/coronavirus/. If not, the scraping will not function properly. scrape_country returns a dictionary with the country name, total deaths (normalized by 1M), and the daily deaths (not normalized)
Libraries that must be installed: requests, BeautifulSoup, re, json
The ScrapeWebsiteTest.py file collects data for the current day.

Instructions for running Covid dashboard:
Libraries that must be installed: json, bokeh, datetime
The dashboard code for creating and running the dashboard is in file FinalGo.py.
The dashboard contains four plots: 
	1: a zoomed out plot with average daily deathrates for 13 countries
	2: a plot of daily death rates with an adjustable historical data range
	3: a plot of daily death rates and normalized total deaths (by 1M) for 5 select countries
	4: a plot of daily death rates for 5 select countries where each country's data can be toggled on and off
