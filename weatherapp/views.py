from django.shortcuts import render,HttpResponse
import requests
import datetime

# Create your views here.
'''https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'''
def index(request):
    if request.method=="POST":

        if 'city' in request.POST:
            city=request.POST["city"]
        else:
            city='visakhapatnam'
        
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a2b8c37f9ec3577542b1f10ec508a63"
        params={'units':"metric"}

        data=requests.get(url,params).json()

        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        day=datetime.date.today()
        temp=data['main']['temp']
        humidity=data['main']['humidity']




        return render(request,"index.html",{'description':description,"icon":icon,"day":day,"temp":temp,"city":city.upper(),"humidity":humidity})
    else:
        return render(request,"index.html")
