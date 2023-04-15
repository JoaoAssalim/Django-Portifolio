from django.shortcuts import render
from django.http import HttpResponse

def marathon_participated(request):
	return render(request, 'marathons/marathons-participated/marathons.html')