from django.shortcuts import render
import requests


def weather_forecast(request):
    if request.method == 'GET':
        city = request.GET.get('city', '')
        if city:
            api_key = 'cebcd482eda57fa9a6714c1c2ba91885'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br&units=metric"

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                # Extrair os campos relevantes
                temperature_min = data['main']['temp_min']
                temperature_max = data['main']['temp_max']
                city_name = data['name']
                description = data['weather'][0]['description']

                # Criar um dicionário com os dados formatados
                forecast_data = {
                    'temperature_min': temperature_min,
                    'temperature_max': temperature_max,
                    'city_name': city_name,
                    'description': description
                }

                return render(request, 'weather.html', forecast_data)

    return render(request, 'weather.html')
