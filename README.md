# Поиск и рассчет средней заработной платы по вакансиям программистов

## Краткое описание проекта

Написанная программа позволяет получить актуальные данные по количеству вакансий в Москве
для 9 самых популярных языков программироования: Javascript, Java, Python, Ruby, PHP, C++, C#, C, Go, а
также позволяет получить среднюю заработную плату по каждому языку.

## Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки 
зависимостей:
```
pip install -r requirements.txt
```

## Токен для Superjob

Для работы с API Superjob необходим персональный токен, в документации к API, в
разделе Getting Started описан процесс регистрации приложения и получения токена:
https://api.superjob.ru. После этого в директории приложения необходимо создать файл
`.env`, в который
необходимо поместить токен. Формат заполнения файла:

```
SJ_SECRET_KEY=токен
```

## Как запустить

Для запуска проекта в консоли необходимо выполнить команду:

```
python3 main.py
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков 
[dvmn.org](https://dvmn.org/).