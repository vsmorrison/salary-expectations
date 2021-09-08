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
    sj_vacancies = response.json()['objects']
    for vacancy in sj_vacancies:
        print(f"{vacancy['profession']}, {vacancy['town']['title']}")
    return vacancies


if __name__ == '__main__':
    vacancies = get_vacancies(URL, SECRET_KEY)
