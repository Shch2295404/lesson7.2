# lesson7.2
Basics of working with the Requests library / Основы работы с библиотекой Requests

---

Этот проект содержит учебные задания, демонстрирующие базовые операции с HTTP-запросами с использованием библиотеки `requests`. Каждое задание выполнено в отдельном Python-файле.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Установите библиотеку `requests`, если она ещё не установлена:
   ```bash
   pip install requests
   ```

## Содержание заданий

### Задание 1: Получение данных

В файле `main-1.py` представлен пример отправки GET-запроса к открытому API GitHub с параметром для поиска репозиториев с кодом `html`.

**Основные действия:**
- Импортируем библиотеку `requests`.
- Отправляем GET-запрос с параметром поиска.
- Выводим статус-код ответа.
- Форматируем и выводим содержимое ответа в формате JSON.

**Запуск:**
```bash
python main-1.py
```

### Задание 2: Параметры запроса

Файл `main-2.py` демонстрирует использование URL-параметров для фильтрации данных через GET-запрос к API `https://jsonplaceholder.typicode.com/posts`.

**Основные действия:**
- Задаём параметры запроса (`userId=1`).
- Отправляем GET-запрос.
- Выводим ответ в формате JSON.

**Запуск:**
```bash
python main-2.py
```

### Задание 3: Отправка данных

В файле `main-3.py` выполнен пример отправки POST-запроса к API `https://jsonplaceholder.typicode.com/posts` для создания новой записи.

**Основные действия:**
- Формируем данные для отправки.
- Отправляем POST-запрос с передачей данных в теле запроса.
- Выводим статус-код и содержимое ответа.

**Запуск:**
```bash
python main-3.py
```

## Результаты

Результаты выполнения каждого задания выводятся в консоль. Для проверки работы выполните команды выше и сравните результаты с ожидаемыми.

## Ссылки

- [Документация библиотеки Requests](https://docs.python-requests.org)
- [API GitHub](https://api.github.com)
- [JSONPlaceholder](https://jsonplaceholder.typicode.com)

## Примечание

Этот проект является учебным и предназначен исключительно для освоения основ работы с библиотекой `requests`.

