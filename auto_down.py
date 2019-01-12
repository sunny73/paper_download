import urllib.request
import requests
import wget as wget

from bs4 import BeautifulSoup

lines = open('list0678.txt').readlines()
fp = open('list.txt', 'w')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

data = {
    'poster': 'test',
    'syntax': 'cpp',
    'content': 'test',
}

for s in lines:
    res = requests.post(url=s, headers=headers, data=data, allow_redirects=False)
    fp.write(res.headers['location']+'\n')
    print(res.headers['location'])  # 获取其他的也是一样的

fp.close()


lines = open('list.txt').readlines()
fp = open('list2.txt', 'w')
for s in lines:
    s = s[:-2]
    s.replace("document/", "stamp/stamp.jsp?tp=&arnumber=") # replace 不会改变原来的内容
    fp.write(s.replace("document/", "stamp/stamp.jsp?tp=&arnumber=")+'\n')
fp.close()

lines = open('list2.txt').readlines()
f = open('list2.txt')
i=0
for line in f:
    line=line[:-1]
    i=i+1
    res = requests.get(line)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.select('iframe')
    pdf = news[0]['src']
    out_fname = str(i)+'.pdf'
    r = requests.get(pdf)
    with open(out_fname,'wb') as f2:
        f2.write(r.content)

f.close()
