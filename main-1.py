import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов
import pprint  # Импортируем библиотеку pprint для удобного форматирования вывода

# Определяем параметры запроса, в данном случае ключевое слово 'html'
params = {
    'q': 'html'
}

# Выполняем GET-запрос к API GitHub для поиска репозиториев с указанными параметрами
response = requests.get('https://api.github.com/search/repositories', params=params)

# Выводим статус-код ответа, чтобы убедиться, что запрос выполнен успешно (например, статус 200)
print(f"Статус-код ответа: {response.status_code}")

# Выводим содержимое ответа в формате JSON, чтобы увидеть результаты поиска
print(f"\nСодержимое ответа в формате JSON:\n")
response_json = response.json()  # Преобразуем содержимое ответа в Python-объект (словарь/список)
pprint.pprint(response_json)  # Удобно форматируем и выводим содержимое JSON
