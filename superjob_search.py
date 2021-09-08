import requests
import utilities
from settings import SECRET_KEY


LANGUAGES = [
    'Javascript',
    'Java',
    ]
# LANGUAGES = [
#     'Javascript',
#     'Java',
#     'Python',
#     'Ruby',
#     'PHP',
#     'C++',
#     'C#',
#     'C',
#     'Go'
# ]
URL = 'https://api.superjob.ru/2.0/vacancies/'


def get_vacancies(url, secret_key, languages):
    num_of_vacancies = {}
    for language in languages:
        headers = {
            'X-Api-App-Id': secret_key
        }
        payload = {
            'town': 4,
            'catalogues': 48,
            'count': 100
        }
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        num_of_vacancies[language] = response.json()['total']
    #sj_vacancies = response.json()['objects']
    #for vacancy in sj_vacancies:
        #print(f"{vacancy['profession']}, {vacancy['town']['title']}")
    return num_of_vacancies
# def count_vacancies(url, languages):
#     num_of_vacancies = {}
#     for language in languages:
#         payload = {
#             'text': f'программист {language}',
#             'area': '1',
#             'period': '30'
#         }
#         response = requests.get(url, params=payload)
#         response.raise_for_status()
#         num_of_vacancies[language] = response.json()['found']
#     return num_of_vacancies

def get_raw_salaries(url, languages, secret_key):
    page = 0
    pages_number = 1
    raw_salaries = []
    salaries_by_page = []
    for language in languages:
        while page < pages_number:
            headers = {
                'X-Api-App-Id': secret_key
            }
            payload = {
                'town': 4,
                'catalogues': 48,
                'count': 100
            }
            response = requests.get(url, params=payload, headers=headers)
            response.raise_for_status()
            items = response.json()['objects']
            pages_number = 5
            print(language, page)
            page += 1
            for item in items:
                salaries_by_page.append([item['payment_from'],
                                        item['payment_to'],
                                        item['currency']
                                         ])
        page = 0
        raw_salaries.append(salaries_by_page)
        salaries_by_page = []
    return raw_salaries


if __name__ == '__main__':
    num_of_vacancies = get_vacancies(URL, SECRET_KEY, LANGUAGES)
    raw_salaries = get_raw_salaries(URL, LANGUAGES, SECRET_KEY)
    predicted_salaries = utilities.predict_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    print(stats)