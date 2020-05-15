import requests
from django.shortcuts import render
from weather.models import City
from weather.forms import CityForm


def weaterview(request):
    key = "d52fbaedd1ca6f5f423a54a5a5e7374d"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&units=metric&appid=" + key

    if(request.method=="POST"):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    citys = City.objects.all().order_by('-id')[:1]
    info=[]
    for city in citys:
        response = requests.get(url.format(city.name)).json()
        weather_ihfo = {
            "name": city.name,
            "temp": response["main"]["temp"],
            "wind": response["wind"]["speed"],
            "description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
        }
        info.append(weather_ihfo)
    context = {"allinfo":info, "form":form}
    return render(request, "start.html", context)
