from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'stock_app/index.html')

def about(request):
	return render(request, 'stock_app/about.html')

def contact(request):
	return render(request, 'stock_app/contact.html')
