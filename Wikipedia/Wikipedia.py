import csv
import requests
import lxml.html as html
from pyquery import PyQuery as pq

BASE_URL = "https://en.wikipedia.org"

def read_url(url) :
    html = requests.get(url).content
    return pq(html)

def get_page_rows(page) :
    response = read_url(page)
    rows = response.find('table.wikitable tr') # collection of rows
    print("count >> ", rows.__len__())
    quit()
    data = list()
    for row in rows.items():
        ranking = row.find('td').eq(0).text()
        country = row.find('td').eq(1).text()
        countryUrl = row.find('td').eq(1).find('a').attr('href') # gives the link of country
        revenues = row.find('td').eq(2).text().strip()

        if country:
            data.append([ranking,country,countryUrl,revenues])
    return data

def write_csv(mydict) :
     with open('Budget.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Rank", "Country", "CountryUrl" "Revenue"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)

if __name__ == '__main__': # main fucntion
    urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_government_budget"] # page url
    #print(urls)
    #quit()
    data = list()
    for url in urls:
        scrape_page = get_page_rows(url)
        print("Finding Page >> ", url)
        data.append(scrape_page)

    write_csv(data)
    print('Completed')

        
    
