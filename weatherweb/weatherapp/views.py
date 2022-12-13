from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):

    if request.method == "POST":

        try:
        # city name taken from form
            city = request.POST['city']

            # Api from openweather site
            source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&units=metric&appid=a06a83a6227d33f64ee1833322842b99').read()

            # Data extracted from openweather using api
            website_data = json.loads(source)

            # context to show on our website
            data = {
                "city": city,
                "country_code": str(website_data['sys']['country']),
                "coordinate": str(website_data['coord']['lon']) + ', '
                + str(website_data['coord']['lat']),
                "temp": str(website_data['main']['temp']) + ' °C',
                "pressure": str(website_data['main']['pressure']),
                "humidity": str(website_data['main']['humidity']),
                'main': str(website_data['weather'][0]['main']),
                'description': str(website_data['weather'][0]['description']),
                'icon': website_data['weather'][0]['icon'],
            }
        except:
            data = {}
            return render(request,'weatherapp/index.html',data)
        # print(data)
    else:
        data = {}

    return render(request,'weatherapp/index.html',data)
