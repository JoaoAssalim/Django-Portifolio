from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home-page'),
    path('about-me/', views.about, name='about-page'),
    path('projects/', views.projects, name='projects-page'),
    path('contact/', views.contact, name='contact-page'),
]