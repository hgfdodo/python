template='''
<html>

<head>
<title>%(title)s</title>
</head>

<body>
<p>%(p)s</p>
</body>

</html>
'''
dic = {'title':'hgf\'s home page','p':'i love jxn'}

print (template % dic)
