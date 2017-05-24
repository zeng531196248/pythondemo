#coding=utf-8
import   urllib.request
import  re
url="http://www.qqyou.com/zipai/nvsheng/"
print(url)
f=urllib.request.urlopen(url)
htmlcode=f.read()
html=htmlcode.decode('utf-8')
imageList=re.findall('src="(.*\.(jpg|png)")',html)
j=1
for i in imageList :
    imgUrl=i[0]
    print(imgUrl)
    urllib.request.urlretrieve(imgUrl,'D:/images/%d.jpg'%j)
    j+=1