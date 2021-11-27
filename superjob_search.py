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
