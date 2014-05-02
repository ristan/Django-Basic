# coding - utf-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hola(request):
	return render('index.html',{'saludar':'hola mundo'}),

