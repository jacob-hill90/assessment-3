from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('hackazon_app.urls')),
]
