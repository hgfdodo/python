from django.db import models
from django import forms

class User(forms.Form):
	name=forms.CharField()
	age=forms.IntegerField()
	gender=forms.CharField()
