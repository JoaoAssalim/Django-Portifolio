from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return render(request, 'blog/home-page/home.html')

def about(request):
	return render(request, 'blog/about-page/about_us.html')

def projects(request):
	return render(request, 'blog/projects-page/projects.html')

def contact(request):
	return render(request, 'blog/contact-page/contact.html')