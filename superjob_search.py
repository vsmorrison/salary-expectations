import requests
from settings import SECRET_KEY

LANGUAGES = [
    'Javascript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C',
    'Go'
]
URL = 'https://api.superjob.ru/2.0/vacancies/'


def get_vacancies(url, secret_key):
    headers = {
        'X-Api-App-Id': secret_key
    }
    payload = {
        'town': 4,
        'catalogues': 48
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()['objects']
    for vacancy in vacancies:
        print('{}, {}'.format(vacancy['profession'], vacancy['town']['title']))
    return


if __name__ == '__main__':
    vacancies = get_vacancies(URL, SECRET_KEY)
    print(vacancies)

