from subprocess import Popen, PIPE

test=open('ex1.html')
tidy=Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE)

tidy.stdin.write(text)
tidy.stdin.close()

html=tidy.stdout.read()

print html