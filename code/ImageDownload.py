from HTMLParser import HTMLParser
from urllib import urlopen,urlretrieve

class ImageURL(HTMLParser):
	path=''
	links=[]
	codes=['jpg','png','gif']

	def handle_starttag(self,tag,attrs)	:
		attr=dict(attrs)
		if tag=='img' and 'src' in attr:
			self.links.append(attr['src'])

	def clean_GetLinks(self):
		for link in self.links:
			if link.split(".")[-1] not in self.codes:
				self.links.remove(link)
		return self.links,len(self.links)

	def down(self,path):
		self.path=path
		i=0
		for link in self.links:
			urlretrieve(link,self.path + "\\" + str(i) + '.'+link.split('.')[-1])
			i+=1


if __name__=='__main__':
	test=urlopen("http://image.baidu.com/i?word=ak").read()
	imgDown=ImageURL()
	imgDown.feed(test)
	print imgDown.clean_GetLinks()
	imgDown.down(r'e:\\image')
	imgDown.close()
	print "OK"