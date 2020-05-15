from django.contrib import admin
from django.urls import path, include
from phonebook.views import *


urlpatterns = [
    path("phone/create/", PhoneCreateView.as_view()),
    path("mycontacts", PhoneListView.as_view()),
    path("phone/detail/<int:pk>", PhoneDetailView.as_view()),
]
