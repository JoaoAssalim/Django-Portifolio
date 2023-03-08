from django.contrib import admin
from django.urls import include, path, re_path
from page.views import *

app_name = 'dash'
namespace = app_name

urlpatterns = [
    re_path('test/$', test , name="test"),
]