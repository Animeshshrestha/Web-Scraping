import csv
import requests
import lxml.html as html
from pyquery import PyQuery as pq

BASE_URL = "http://www.nepalstock.com"

def read_url(url) :
    html = requests.get(url).content
    return pq(html)

def get_page_rows(page) :
    response = read_url(page)
    rows = response.find('table.table tr')
    rows.pop(0)
    # collection of rows
    print("count >> ", rows.__len__())
    data = list()
    for row in rows.items():
        serial_no = row.find('td').eq(0).text()
        symbol = row.find('td').eq(1).text()
        LTP = row.find('td').eq(2).text()
        LTV = row.find('td').eq(3).text()
        Point_change = row.find('td').eq(4).text()
        changes = row.find('td').eq(5).text()
        Open = row.find('td').eq(6).text()
        High = row.find('td').eq(7).text()
        Low = row.find('td').eq(8).text()
        Volume = row.find('td').eq(9).text()
        Previous_closing = row.find('td').eq(10).text()
        

        if Previous_closing:
            data.append([serial_no,symbol,LTP,LTV,Point_change,changes,Open,High,Low,Volume,Previous_closing])
    return data

def write_csv(mydict) :
     with open('Budgetss.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["serial_no","symbol","LTP","LTV","Point_change","change%","Open","High","Low","Volume","Previous_closing"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)

if __name__ == '__main__': # main fucntion
    urls = ["http://www.nepalstock.com.np/stocklive"] # page url
    #print(urls)
    #quit()
    data = list()
    for url in urls:
        scrape_page = get_page_rows(url)
        print("Finding Page >> ", url)
        data.append(scrape_page)

    write_csv(data)
    print('Completed')

        
    
