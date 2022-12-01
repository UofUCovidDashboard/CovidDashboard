#Module for scraping website data

def scrape_country(country, website):
    import requests
    from bs4 import BeautifulSoup
    
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    return None