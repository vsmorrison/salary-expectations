import requests


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


def get_salaries_by_lang(url, languages, secret_key):
    page = 0
    pages_number = 1
    salaries_by_lang = {}
    vacancies = {}
    for language in languages:
        salaries_by_lang[f'{language}'] = {}
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
            print(language, page)
            page += 1
            for index, item in enumerate(items):
                vacancies['from'] = item['payment_from']
                vacancies['to'] = item['payment_to']
                vacancies['currency'] = item['currency']
                salaries_by_lang[f'{language}'][index] = vacancies
                vacancies = {}
        page = 0
    return salaries_by_lang
