from django.urls import path
from . import views

urlpatterns = [
    path('', views.marathon_participated, name='marathons-page'),
]