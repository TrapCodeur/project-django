
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('soccer.urls')),
    path('', include('store.urls')),
    path('', include('classement.urls')),
   
]
