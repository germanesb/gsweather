import requests
import math
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from datetime import datetime


def home(request):

    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=2e3a70bcb683210930038135bb0d8003"

    err_msg = ""
    message = "Add/Remove Cities As You Want"
    message_class = ""

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"]
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                resp = requests.get(url.format(new_city)).json()
                if resp["cod"] == 200:
                    form.save()
                else:
                    err_msg = "City does not exist in the World!!"
            else:
                err_msg = "The city already exist in the DataBase!!"

        if err_msg:
            message = err_msg
            message_class = "is-danger"
        else:
            message = "City added successfully.."
            message_class = "is-success"

    # print(err_msg)
    # print(request.POST)

    # form = CityForm()  # Form instantiated, to avoid a blank page refreshed
    form = CityForm()

    # cities = City.objects.all()
    cities = City.objects.all().order_by('-id')

    weather_data = []

    for city in cities:
        response = requests.get(url.format(city)).json()
        # print(response)
        # Create a dictionary to take the data
        city_weather = {
            "city": city.name,
            "temperature": math.trunc(response["main"]["temp"]),
            "Feels_Like": math.trunc(response["main"]["feels_like"]),
            "Description": response["weather"][0]["description"],
            "icon": response["weather"][0]["icon"],
            "country": response["sys"]["country"],
            "timezone": response["timezone"],
        }
        weather_data.append(city_weather)

    # print(weather_data)
    # Create a context variable, to pass variable to the template
    context = {
        "weather_data": weather_data,
        "form": form,
        "message": message,
        "message_class": message_class,
    }

    return render(request, "home.html", context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')


# def getTimeFromOffset(offset):

#     d = datetime.now()
#     localTime = datetime.time(datetime.now())
#     print(d)
#     print(localTime)

#     millis = 1288483950000
#     ts = millis * 1e-3
#     # local time == (utc time + utc offset)
#     localOffset = datetime.fromtimestamp(ts) - datetime.utcfromtimestamp(ts)
#     print(localOffset)
#     # localOffset = d.getTimezoneOffset() * 60000
#     # obtain UTC time in msec
#     utc = localTime + localOffset
#     # create new Date object for different city
#     # using supplied offset
#     nd = Date(utc + (3600000 * offset))
#     # nd = 3600000 + nd;
#     utc = Date(utc)
#     return utc.toLocaleString()
#     #     $("#local").html(nd.toLocaleString());
#     #     $("#utc").html(utc.toLocaleString());
