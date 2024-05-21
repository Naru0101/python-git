import os  # Импортируем модуль для работы с операционной системой
import subprocess  # Импортируем модуль для выполнения внешних команд
import requests  # Импортируем модуль для отправки HTTP-запросов

# Функция для выполнения команды в командной строке
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)  # Запускаем команду в командной строке
    except subprocess.CalledProcessError as e:  # Обрабатываем ошибку, если команда завершается с ненулевым кодом
        return f"Error executing command: {e}"  # Возвращаем сообщение об ошибке
    return "Command executed successfully."  # Возвращаем сообщение об успешном выполнении команды

# Функция для выполнения поиска информации.
def google_search(query):
    url = f"https://www.google.com/search?q={query}"  # Формируем URL для поискового запроса аделы где есть информция.
    response = requests.get(url)  # Отправляем GET-запрос по указанному URL
    if response.status_code == 200:  # Проверяем успешность запроса
        return response.text  # Возвращаем HTML-код страницы с результатами поиска
    else:
        return f"Error accessing : Status info code {response.status_code}"  # Возвращаем сообщение об ошибке, если запрос неудачен

# Основная функция программы
def main():
    while True:  # Запускаем бесконечный цикл для ввода команд
        user_input = input("Enter a command: ")  # Получаем ввод от пользователя
        if user_input.lower() == "exit":  # Если пользователь ввел "exit", выходим из цикла
            break
        elif user_input.lower().startswith("start pc+ Runi"):  # Если пользователь ввел команду для выполнения в командной строке
            command = user_input[7:]  # Получаем саму команду
            result = execute_command(command)  # Выполняем команду
            print(result)  # Выводим результат выполнения команды
        elif user_input.lower().startswith("start st Runi"):  # Если пользователь ввел команду для поиска в Google
            query = user_input[9:]  # Получаем строку для поиска
            result = google_search(query)  # Выполняем поиск в Google
            print(result)  # Выводим результат поиска
        else:
            print("Command not recognized.")  # Если команда не распознана, выводим сообщение об ошибке

# Проверяем, является ли данный скрипт основным модулем программы
if __name__ == "__main__":
    main()  # Вызываем основную функцию программы
