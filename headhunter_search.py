import requests


def get_salaries_by_lang(url, language):
    input_data = {'Moscow_id': 1, 'SPb_id': 2}
    page = 0
    pages_number = 1
    salaries_by_lang = []
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
        page += 1
        salaries_by_lang.append(items['items'])
    total = items['found']
    return salaries_by_lang, total
