import requests
import pandas as pd

# Замените 'your_api_key', 'your_city' на ваш ключ API от OpenWeatherMap и необходимый город
API_KEY = 'your_api_key'
CITY = 'your_city'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

# Извлечение необходимых данных
weather_data = {
    'city': data['name'],
    'temperature': data['main']['temp'],
    'humidity': data['main']['humidity'],
    'weather': data['weather'][0]['description'],
}

# Преобразование в DataFrame
df_weather = pd.DataFrame([weather_data])
print(df_weather)
