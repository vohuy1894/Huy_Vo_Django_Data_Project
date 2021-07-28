from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
import random
import requests
import styvio

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created for {username}!')
			return redirect('stock-home')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, *args, **kwargs):
	context = {}
    # #  search bar logic  # #
	stockList = ["MSFT", "FB", "AAPL", "AMZN", "NFLX", "GOOG", "BABA", "NVDA", "TSLA"]
	randomStock = (random.choice(stockList))
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
	if(search_query is None):
		search_query = randomStock
	tickerText = search_query.upper()

	try:
		out = (requests.get("https://www.styvio.com/api/" + str(tickerText))).json()
	except:
		out = (requests.get("https://www.styvio.com/api/" + str(randomStock))).json()
    # # end search bar logic  # #    

	# #  API logic  # #
	ticker = out['ticker']
	currentPrice = out['currentPrice']
	weekly_prices = out['weeklyPrices']
	context['ticker'] = ticker
	context['currentPrice'] = currentPrice
	context['weekly_prices'] = weekly_prices
	return render(request, 'users/profile.html', context)