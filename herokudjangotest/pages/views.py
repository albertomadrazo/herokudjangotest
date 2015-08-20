from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context_dict = {'message': 'Greetings from planet mars, earthlings.'}
	return render(request, 'pages/index.html', context_dict)
	