import requests 

API_Key = '595d39bc8c5681fba199b98966a1da1d'

city = input("Enter a city: ")

base_url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}&lang=pt_br'

weather_data = requests.get(base_url).json()
temperatura = weather_data['main']['temp'] -273.15

print(f'{temperatura:.1f}°C')
