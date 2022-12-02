#Module for scraping website data

def scrape_country(country, url):
    import requests
    from bs4 import BeautifulSoup
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    tbls = soup.find_all("table")
    print("Number of tables on site: ", len(tbls))
    
    table1 = tbls[0]
    body = table1.find_all("tr")
    head = body[0]
    body_rows = body[1:]
    
    headings = []
    for item in head.find_all("th"):
        item = (item.text).rstrip("\n")
        headings.append(item)
    print(headings)
    
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