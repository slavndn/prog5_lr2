Славный Даниил Михайлович - Лабораторная работа 2

1. Скачал zip с файлами
2. Открыл в редакторе кода Visual Studio Code
3. Выполняю импорт библиотек
```
from owm_key import owm_api_key
import json
import requests
import os
```
4. Определяю функцию **get_weather_data**, которая принимает два параметра: **place и api_key**
5. Если **api_key** не задан или **place** пустой, функция сразу возвращает **None**
```
def get_weather_data(place, api_key=None):
    if api_key is None:
        return None

    if not place:
        return None
```
6. Формирую URL для запроса к API OpenWeatherMap, где передаются название города, ключ API и единицы измерения
7. Выполняю GET-запрос на указанный URL, и результат сохраняется в переменной **response**
```
    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    response = requests.get(url)
```
8. Выполняю проверку статуса (кода). Если он не равен 200 (успешный запрос), функция возвращает **None**
```
    if response.status_code != 200:
        return None
```
9. Извлекают необходимые данные о погоде
```
city_name # название города
country_code # код страны
coordinates # координаты города (широта и долгота)
feels_like # температура (по ощущениям)
timezone_offset # смещение часового пояса в секундах, которое переводится в часы
```
10. Форматируется строка с часовым поясом, указывая на UTC и смещение в часах
```
timezone = f"UTC{'+' if timezone_offset >= 0 else '-'}{abs(timezone_offset)}"
```
11. Функция возвращает строку в формате JSON, содержащую информацию о городе, координатах, стране, температуре по ощущениям и часовом поясе
```
    return json.dumps({
        "name": city_name,
        "coord": {"lon": longitude, "lat": latitude},
        "country": country_code,
        "feels_like": feels_like,
        "timezone": timezone
    })
```
12. Вызываются три раза функция **get_weather_data** с названиями городов: Москва, Санкт-Петербург и Дакка. Результаты сохраняются в соответствующих переменных
```
moscow_weather = (get_weather_data('Moscow', api_key=owm_api_key))
spb_weather = (get_weather_data('Saint Petersburg', api_key=owm_api_key))
dhaka_weather = (get_weather_data('Dhaka', api_key=owm_api_key))
```
13. Получаю размеры терминального окна для дальнейшего использования при выводе данных
```
    term_size = os.get_terminal_size()
```
14. Непосредственно вывод результатов
```
    print()
    print()
    print('-' * term_size.columns)
    print(moscow_weather)
    print('-' * term_size.columns)
    print(spb_weather)
    print('-' * term_size.columns)
    print(dhaka_weather)
    print('-' * term_size.columns)
    print()
    print()
```
**API ключ лежит в отдельном файле. На момент выгрузки ЛР, API ключ уже деактивирован! Файл с тестами выгружен в данный репозиторий под названием **getweatherdata_test.py****
**Все файлы лежат в репозитории**

**Скриншоты**
![image](https://github.com/user-attachments/assets/7ea56f02-06d5-46dc-b62a-508e686fa791)
![image](https://github.com/user-attachments/assets/34e81217-3436-483e-ae56-a25c52eaa909)

```
-----------------------------------------------------------------------------------------------------------------------------------------------------
{"name": "Moscow", "coord": {"lon": 37.6156, "lat": 55.7522}, "country": "RU", "feels_like": 15.92, "timezone": "UTC+3"}
-----------------------------------------------------------------------------------------------------------------------------------------------------
{"name": "Saint Petersburg", "coord": {"lon": 30.2642, "lat": 59.8944}, "country": "RU", "feels_like": 13.68, "timezone": "UTC+3"}
-----------------------------------------------------------------------------------------------------------------------------------------------------
{"name": "Dhaka", "coord": {"lon": 90.4074, "lat": 23.7104}, "country": "BD", "feels_like": 35.99, "timezone": "UTC+6"}
-----------------------------------------------------------------------------------------------------------------------------------------------------
```
