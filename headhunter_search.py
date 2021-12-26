import requests


def get_salaries_by_lang(url, languages):
    input_data = {'Moscow_id': 1, 'SPb_id': 2}
    page = 0
    pages_number = 1
    salaries_by_lang = {}
    vacancies = {}
    vacancy = {}
    index = 0
    for language in languages:
        salaries_by_lang[language] = {}
        while page < pages_number:
            payload = {
                'text': f'{language}',
                'area': f'{input_data["Moscow_id"]}',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            items = response.json()
            pages_number = items['pages']
            print(language, page)
            page += 1
            for item in items['items']:
                vacancy['salary'] = item['salary']
                vacancies[index] = vacancy
                index += 1
                vacancy = {}
            salaries_by_lang[language]['vacancies'] = vacancies
        salaries_by_lang[language]['total'] = items['found']
        index = 0
        vacancies = {}
        page = 0
    return salaries_by_lang
