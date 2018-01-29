import csv
import sys
import requests
import lxml.html as html
from pyquery import PyQuery as pq

BASE_URL = "http://1337x.to"
# sys.setdefaultencoding('utf-8')


def read_url(url):
    html=requests.get(url).content
    return pq(html)


def get_page_rows(page):
    response = read_url(page)
    rows = response.find('div.featured-list div.table-list-wrap table.table-list tr')
    print("count >> ", rows.__len__()) 
    data = list()
    #count = 0
    for row in rows.items(): # pyquery function (items)
        name = row.find('td').eq(0).text()
        seeders = row.find('td').eq(4).find('span').text()
        leechers = row.find('td').eq(2).text()
        time = row.find('td').eq(3).text()
        size = row.find('td').eq(4).text()
        if name:
            data.append([name[0:15],seeders,leechers,time,str(size.split(" ")[0]+" "+size.split(" ")[1])])
            #count = count+1
            #if count>10:
              #  break

            
    return data


def write_csv(mydict):
    with open('details.csv', 'w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in mydict.items():
            if type(value) is not list:
                value = value.encode("UTF-8")
                writer.writerow([key, value])


def writeto_csv(mydict):
    with open('details.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Name","Seeders","Leechers","Time","Size"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)


if __name__ == '__main__': # main fucntion
    urls = ["http://1337x.to/home/"] # page url
    #print(urls)
    #quit()
    data = list()
    for url in urls:
        scrape_page = get_page_rows(url)
        print("Finding Page >> ", url)
        data.append(scrape_page)

    writeto_csv(data)
    print('Completed')
