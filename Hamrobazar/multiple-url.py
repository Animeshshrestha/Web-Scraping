import csv
import requests
from pyquery import PyQuery as pq

def read_url(url, filename):
    print("filename:", filename)
    html = requests.get(url=url).content
    response = pq(html)
    rows = response.find('table.mainbody tr td table#lblue tr')
    text= rows.find('td#white')
    del text[20:23]# deleting common text that occurs on every page
    del text[46:]# deleting the comment or text spoken 
    new_text=text.text()
        
    with open(filename,"a") as f:
        f.write('{0}\n'.format(new_text))
        

          

def find_url():
    import csv
    import pandas as pd
    data = pd.read_csv('Popular_ads.csv', delimiter=',')
    data1 = data.url
    for row in data1:
        a = 'http://hamrobazar.com/'
        url = a + row
        print(url)
        filen = ("").join(a for a in row.split("."))
        read_url(url, filen[10:] + ".txt")

if __name__ == '__main__':
    find_url()
   
