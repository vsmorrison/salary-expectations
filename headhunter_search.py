import requests

HH_LANGUAGES = [
    'C++',
    'Python'
]

# LANGUAGES = [
#     'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
# ]
HH_URL = 'https://api.hh.ru/vacancies'


def count_vacancies(url, languages):
    num_of_vacancies = {}
    for language in languages:
        payload = {
            'text': f'программист {language}',
            'area': '1',
            'period': '30'
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        num_of_vacancies[language] = response.json()['found']
    return num_of_vacancies


def get_raw_salaries(url, languages):
    page = 0
    pages_number = 1
    raw_salaries = []
    salaries_by_language = []
    for language in languages:
        while page < pages_number:
            payload = {
                'text': f'{language}',
                'area': '1',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            items = response.json()['items']
            pages_number = response.json()['pages']
            print(language, page)
            page += 1
            for item in items:
                salaries_by_language.append(item['salary'])
        page = 0
        raw_salaries.append(salaries_by_language)
        salaries_by_language = []
    return raw_salaries


# if __name__ == '__main__':
#     num_of_vacancies = count_vacancies(HH_URL, HH_LANGUAGES)
#     raw_salaries = get_raw_salaries(HH_URL, HH_LANGUAGES)
#     print(raw_salaries)
