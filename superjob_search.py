import requests


def get_salaries_by_lang(url, languages, secret_key):
    page = 0
    pages_number = 1
    salaries_by_lang = {}
    vacancies = {}
    vacancy = {}
    for language in languages:
        salaries_by_lang[language] = {}
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
            items = response.json()
            #print(language, page)
            page += 1
            for index, item in enumerate(items['objects']):
                vacancy['from'] = item['payment_from']
                vacancy['to'] = item['payment_to']
                vacancy['currency'] = item['currency']
                vacancies[index] = vacancy
                vacancy = {}
            salaries_by_lang[language]['vacancies'] = vacancies
            vacancies = {}
        salaries_by_lang[language]['total'] = items['total']
        page = 0
    print(salaries_by_lang)
    return salaries_by_lang
