people={
    'hgf':{
        'phone':'13716112485',
        'addr':'beijing university of posts and telecommunications'
        },
    'jxn':{
        'phone':'1122313213',
        'addr':'baoding'
        }
    }

name = raw_input("name:")
phone='phone'
addr = 'addr'

if name in people:out = "%s's phone number is %s and address is %s" % (name, people[name][phone],people[name][addr])
else:out="%s is not in people" % name

print (out)
