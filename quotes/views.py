from django.shortcuts import render


def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_698bc25dbde34047a3dbc334b48a604f")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error.."
		return render(request,'home.html',{'api':api})
	
	else: 
		return render(request,'home.html',{'ticker':"Enter The Ticker symbol "})
	
	





def about(request):
	return render(request,'about.html',{})
