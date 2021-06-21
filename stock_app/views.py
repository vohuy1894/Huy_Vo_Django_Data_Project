from django.shortcuts import render
from django.http import HttpResponse
import requests
from newsapi import NewsApiClient

API_KEY = '0d2cba56edc44da9b9abad218c8b31e9'

def home(request):
	newsapi = NewsApiClient(api_key='0d2cba56edc44da9b9abad218c8b31e9')
	top_headlines = newsapi.get_top_headlines(q='stock',
                                          category='business',
                                          language='en',
										  )

	articles = top_headlines['articles']
	context = {
		'articles':articles
	}
	return render(request, 'stock_app/index.html', context)

def about(request):
	return render(request, 'stock_app/about.html')

def contact(request):
	return render(request, 'stock_app/contact.html')
