import requests
LANGUAGES = [
    'Javascript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C',
    'Go'
]


def count_vacancies_by_language(languages):
    vacancies_counters = {}
    url = 'https://api.hh.ru/vacancies'
    for language in languages:
        payload = {'text': 'программист {}'.format(language),
                   'area': '1',
                   'period': '30'
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        vacancies_counters[language] = response.json()['found']
    print(vacancies_counters)


def get_salaries_by_language(language):
    salaries = []
    url = 'https://api.hh.ru/vacancies'
    payload = {'text': 'программист {}'.format(language),
               'area': '1',
               'period': '30'
               }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    items = response.json()['items']
    for item in items:
        salaries.append(item['salary'])
    print(salaries)


#count_vacancies_by_language(LANGUAGES)
get_salaries_by_language(LANGUAGES[2])
