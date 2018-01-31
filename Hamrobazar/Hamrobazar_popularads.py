import csv
import requests
import lxml.html as html
from pyquery import PyQuery as pq


def read_url(url) :
    html = requests.get(url).content
    return pq(html)

def table_rows(page) :
    response = read_url(page)
    rows = response.find('table.mainbody tr td table tr td table tr')# collection of rows
    del rows[0:48]
    del rows[36:]
    print("count >> ", rows.__len__())
    #print(rows)
    #quit()
    data = list()
    for row in rows.items():
        item = row.find('td').eq(2).find('font').find('b').text()
        user = row.find('td').eq(2).find('a').eq(1).text()
        location = row.find('td').eq(2).find('font').eq(2).text()
        location=location.replace('-','').strip()
        date = row.find('td').eq(3).text().strip()
        price = row.find('td').eq(4).find('b').text().strip()
        status = row.find('td').eq(4).find('font').text().strip()
        url = row.find('td').eq(2).find('a').attr('href')

        if item:
            data.append([item,user,location,date,price,status,url])
    return data

def write_csv(mydict) :
     with open('Popular_ads.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=["Item_Name", "User_Name", "User_Location", "Date","Price","Status","url"])
        writer.writeheader()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for list in mydict:
            writer.writerows(list)

if __name__ == '__main__': # main fucntion
    urls = ["http://hamrobazaar.com/mostviewed.php?&order=popularad&offset=60"] # page url
    #print(urls)
    #quit()
    data = list()
    for url in urls:
        scrape_page = table_rows(url)
        print("Finding Page >> ", url)
        data.append(scrape_page)

    write_csv(data)
    print('Completed')

        
    
