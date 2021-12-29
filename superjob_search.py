import requests


def get_salaries_by_lang(url, language, secret_key):
    input_data = {'Moscow_id': 4, 'SPb_id': 14, 'SW_Development_id': 48}
    page = 0
    pages_number = 1
    salaries_by_lang = []
    while page < pages_number:
        headers = {
            'X-Api-App-Id': secret_key
        }
        payload = {
            'keyword': f'программист {language}',
            'town': f'{input_data["SPb_id"]}',
            'catalogues': f'{input_data["SW_Development_id"]}',
            'count': 100
        }
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        items = response.json()
        page += 1
    salaries_by_lang = items['objects']
    total = items['total']
    return salaries_by_lang, total
