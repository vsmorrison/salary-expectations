import requests


def get_salaries_by_lang(url, languages):
    page = 0
    pages_number = 1
    salaries_by_lang = {}
    vacancies = {}
    vacancy = {}
    for language in languages:
        salaries_by_lang[language] = {}
        while page < pages_number:
            payload = {
                'text': f'{language}',
                'area': '1',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            items = response.json()
            pages_number = items['pages']
            print(language, page)
            page += 1
            for index, item in enumerate(items['items']):
                vacancy['salary'] = item['salary']
                vacancies[index] = vacancy
                vacancy = {}
            salaries_by_lang[language]['vacancies'] = vacancies
            vacancies = {}
        salaries_by_lang[language]['total'] = items['found']
        page = 0
    print(salaries_by_lang)
    return salaries_by_lang
