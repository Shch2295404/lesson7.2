import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов

# Задаем URL-адрес API, к которому будет выполняться запрос
url = "https://jsonplaceholder.typicode.com/posts"

# Определяем параметры запроса, в данном случае фильтруем записи по userId = 1
params = {
    "userId": 1
}

# Выполняем GET-запрос к указанному URL
response = requests.get(url, params=params)

# Выводим ответ сервера в формате JSON
print(f"Ответ - {response.json()}")
