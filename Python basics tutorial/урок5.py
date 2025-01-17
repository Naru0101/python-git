#Модули и пакеты

#Импорт модулей
#Создание собственных модулей
#Установка и использование пакетов с помощью pip

# Пример импорта модуля
import math
print("Квадратный корень из 16:", math.sqrt(16))

#Импорт модулей:
#Модуль - это файл с Python кодом, содержащий переменные, функции и другие объекты, которые могут быть использованы в других программах.

# Импорт модуля math
import math

# Использование функции sqrt из модуля math
print(math.sqrt(16))  # Выводит: 4.0

#Создание собственных модулей:

#Вы также можете создавать свои собственные модули, чтобы организовать свой код и повторно использовать его в различных программах.

# Создание файла my_module.py с функцией greet
# Содержимое my_module.py:
# def greet(name):
#     print("Hello, ", name)

# Импорт функции greet из созданного модуля
from list01 import greet

# Использование функции greet
greet("John")  # Выводит: Hello, John

#Установка и использование пакетов с помощью pip:
#pip - это инструмент управления пакетами Python, который позволяет устанавливать, обновлять и удалять пакеты из репозитория Python Package Index (PyPI).

# Установка пакета requests с помощью pip
#"pip install requests"

# Импорт пакета requests
import requests

# Использование функций из пакета requests
response = requests.get("https://www.example.com")
print(response.status_code)  # Выводит: 200

#В этом примере мы используем пакет requests для выполнения HTTP-запроса к веб-серверу и получения ответа.