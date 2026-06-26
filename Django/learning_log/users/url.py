#Define URL  patterns for accounts.
from django.urls import path, include
app_name = 'users'
urlpattern = [
    #Include default auth urls.
    path('', include('django.contrib.auth.urls')),
]