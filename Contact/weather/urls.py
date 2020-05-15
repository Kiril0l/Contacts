from django.contrib import admin
from django.urls import path
from weather import views as weather


urlpatterns = [
    path('', weather.weaterview, name="weather"),
]