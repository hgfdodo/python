from django.shortcuts import render ,render_to_response
from models import User
from django.http import HttpResponse

def login(req):
	if req.method == 'POST':
		a=User(req.POST)
		if a.is_valid():
			print a.cleaned_data
			return HttpResponse('ooooo')
	else:
		a=User()
	return render_to_response('login.html',{'form':a})
