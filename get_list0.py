import urllib.request
import requests
from bs4 import BeautifulSoup

url = "https://dblp.uni-trier.de/db/journals/tvt/tvt67.html"
res = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')
soup2=soup.find_all('li', {"class": "entry article"})


fp = open('list0678.txt', 'w')
for i in soup2:
    s =i.find('a')['href']+'\n';
    fp.write(s)
fp.close()


fp.close()





print();

