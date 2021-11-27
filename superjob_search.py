import requests
import hh_utilities
from settings import SECRET_KEY

LANGUAGES = [
    'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
]
SJ_URL = 'https://api.superjob.ru/2.0/vacancies/'


def count_vacancies(url, secret_key, languages):
    num_of_vacancies = {}
    for language in languages:
        headers = {
            'X-Api-App-Id': secret_key
        }
        payload = {
            'keyword': f'программист {language}',
            'town': 4,
            'catalogues': 48,
            'count': 100
        }
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        num_of_vacancies[language] = response.json()['total']
    return num_of_vacancies


def get_raw_salaries(url, languages, secret_key):
    page = 0
    pages_number = 1
    raw_salaries = []
    salaries_by_language = []
    for language in languages:
        while page < pages_number:
            headers = {
                'X-Api-App-Id': secret_key
            }
            payload = {
                'keyword': f'программист {language}',
                'town': 4,
                'catalogues': 48,
                'count': 100
            }
            response = requests.get(url, params=payload, headers=headers)
            response.raise_for_status()
            items = response.json()['objects']
            #print(language, page)
            page += 1
            for item in items:
                salaries_by_language.append([item['payment_from'],
                                        item['payment_to'],
                                        item['currency']
                                         ])
        page = 0
        raw_salaries.append(salaries_by_language)
        salaries_by_language = []
    return raw_salaries


# if __name__ == '__main__':
#     num_of_vacancies = count_vacancies(SJ_URL, SECRET_KEY, LANGUAGES)
#     #print(num_of_vacancies)
#     raw_salaries = get_raw_salaries(SJ_URL, LANGUAGES, SECRET_KEY)
#     print(raw_salaries)
    # predicted_salaries = utilities.predict_salaries(raw_salaries)
    # avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
    # #    predicted_salaries)
    # stats = utilities.make_vacancies_stats(
    #     num_of_vacancies,
    #     vacancies_processed_values,
    #     avg_salaries
    # )
    # stats = utilities.make_vacancies_stats(
    #     num_of_vacancies,
    #     vacancies_processed_values,
    #     avg_salaries
    # )
    # print(stats)
