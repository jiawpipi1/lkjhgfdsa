import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlretrieve
import os
import sys
ptt_url = 'https://www.ptt.cc'
'''
resp = requests.get(ptt_url + '/bbs/Beauty/index2620.html')
soup = BeautifulSoup(resp.text,'html.parser')

tag_name = 'div.title a'
articles = soup.select(tag_name)

for art in articles:
    print(art)
for art in articles:
    print(art['href'],art.text)

paging = soup.select('div.btn-group-paging a')
print(paging[1])
print(paging[1]['href'],paging[1].text)

new_page = paging[1]['href']
print(ptt_url + new_page)

resp = requests.get(ptt_url + new_page)
soup = BeautifulSoup(resp.text,'html.parser')

tag_name = 'div.title a'

articles = soup.select(tag_name)
for art in articles:
    print(art['href'],art.text)
'''
ptt_url = 'https://www.ptt.cc/bbs/Beauty/index.html'
re_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')

if not os.path.isdir('download'):
            os.mkdir('download')

page_number = int(sys.argv[1])
for count in range(3):
    resp = requests.get(ptt_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    articles = soup.select('div.title a')
    paging = soup.select('div.btn-group-paging a')
    new_page_url = 'https://www.ptt.cc' + paging[1]['href']
    url = new_page_url
    for art in articles:
        print(art.text,art['href'])
        #if not os.path.isdir(os.path.join('download',art.text)):
            #os.mkdir(os.path.join('download',art.text))
        resp = requests.get('https://www.ptt.cc' + art['href'])
        images = re_imgur_file.findall(resp.text)
        print(images)

        for image in set(images):
            name = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            urlretrieve(image,os.path.join('download',name))