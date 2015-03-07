import re
import urllib

def getHtml(url):
	page=urllib.urlopen(url)
	return page.read()

def getImg(html):

	imgre = re.compile(r'<img.+src="(.+\.jpg)"',)
	imgList=re.findall(imgre,html)
	i=0

	for imgurl in imgList:
		urllib.urlretrieve(imgurl,"%s.jpg" % i)
		i+=1

getImg(getHtml("http://www.lofter.com/blog/hgfproject"))