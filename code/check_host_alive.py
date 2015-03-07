import os

for i in range(1,3):
    ip='127.0.0.' + str(i)
    status = os.popen('ping ' + str(ip))
    print status.read()
