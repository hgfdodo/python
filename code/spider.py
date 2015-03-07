import urllib,urllib2
url='http://127.0.0.1:8000/login/'
value={'name':'hgf','age':'21','gender':'man'}

data=urllib.urlencode(value)
req=urllib2.Request(url,data)
html=urllib2.urlopen(req)
f=open('e:\\x.html','w')
f.write(html.read())
f.close()

