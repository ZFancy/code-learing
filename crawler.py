#coding:utf-8
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

url = "https://xkcd.com/1883/"
get = get_html(url)

print("\n\nResponse Headers : \n\n",urllib.request.urlopen(url).headers)
print("\n\n.....开始下载网页内容.....\n\n")
print(get.decode('utf-8'))

url = "https://xkcd.com/1884/"
get = get_html(url)
print("\n\nResponse Headers : \n\n",urllib.request.urlopen(url).headers)
print("\n\n.....开始下载网页内容.....\n\n")
print(get.decode('utf-8'))

print("\n\n.....开始解析过程.....\n\n")
soup = BeautifulSoup(get,'html.parser',from_encoding='utf-8')
print(soup.prettify())

print("\n\n.....记录图片title如下.....\n\n")
print(soup.find(id="ctitle").string)

