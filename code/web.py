from HTMLParser import HTMLParser
from urllib import urlopen

class scraper(HTMLParser):
	links=[]
	def handle_starttag(self,tag, attrs):
		attr=dict(attrs)
		if tag=='a' and 'href' in attr:
			self.links.append(attr['href'])

	def getLinks(self):
		return self.links

test = urlopen("http://www.baidu.com").read()
parser=scraper()
parser.feed(test)
print parser.getLinks()
parser.close()