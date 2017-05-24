#conding=utf-8
import  urllib.request
import  re
from  bs4 import  BeautifulSoup
url="http://www.qqyou.com/zipai/nvsheng/"
f=urllib.request.urlopen(url)
htmlcode=f.read()
html=htmlcode.decode('gbk')
soup = BeautifulSoup(html)

print(soup.a)