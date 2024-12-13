import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы с данными о безработице
URL = 'https://tradingeconomics.com/united-states/unemployment-rate'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск таблицы с данными
table = soup.find('table', {'class': 'table table-hover'})

# Извлечение заголовков
headers = [header.text for header in table.find_all('th')]

# Извлечение данных
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    data.append([col.text.strip() for col in cols])

# Преобразование в DataFrame
df_unemployment = pd.DataFrame(data, columns=headers)
print(df_unemployment)
