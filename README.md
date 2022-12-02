# CovidDashboard
Julia Gatto, Zach Lin, Aleks Vazquez
We were approved to use earthquake data for the project instead (approved by Dr. Balouek-Thomert), but we had issues
getting it to read in properly so for now we are using COVID data.

Instructions for running code:
From the ScrapeWebsite module, the scrape_country function is meant to be called with this link: https://www.worldometers.info/coronavirus/. If not, the scraping will not function properly. scrape_country returns a dictionary with the country name, total deaths (normalized by 1M), and the daily deaths (not normalized)
Use of this code requires the requests, BeautifulSoup, re, and json libraries.


Due Dec 3:
Part 1: Data scraping

[]  Commit scraping code

[]       ScrapeWebsite 
       []     collect raw Daily rates
       []     collect raw Cumulative rates
       []     normalize daily rate
       []     normalize cumulative rate 
       [] scrape_country(name_country,url)
           [] return country_data
       [] save data to JSON file

[]  JSON file for at least two consectuive days


Due Dec 11:
Part 2: Data display

In this phase, you will focus on the User Interface of your project. Bokeh is a data visualization library in Python.
It provides highly interactive graphs and plots. 
What makes it different from other Python plotting libraries is that the output from Bokeh will be on the web page, meaning if we run the code in python editor the resulting plot will be in the browser. 
This gives the advantage of embedding the Bokeh plot on any website. 
You are encouraged to use HTML features for creating pop-up and pull-down menus, value lists, input/output forms, labels and customized reports, and in the process come up with a system that caters to users with only limited computer knowledge. We don’t care about having a beautiful UI. It only has to work!

Part 3: Project delivery
Github is a platform used to host open source software development projects. The frontpage of your github project (README) should contain all the information necessary to install your project. You are encouraged to use github during the whole process, not just to push your final code. We'll use your github repository to evaluate the project as a whole, but also quantify and evaluate individual contributions.
