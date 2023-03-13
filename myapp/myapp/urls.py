from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('welcome.urls')),
	path('portifolio/', include('blog.urls')),
    path('marketplace/', include('vendas.urls')),
    path('admin/', admin.site.urls),
]