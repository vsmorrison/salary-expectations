import requests
'''LANGUAGES = [
    'Javascript',
    'Java',
    'Python',
    'Ruby',
    'PHP',
    'C++',
    'C#',
    'C',
    'Go'
]'''
URL = 'https://api.hh.ru/vacancies'


def count_msk_vacancies(url, languages):
    number_of_vacancies = {}
    for language in languages:
        payload = {
            'text': 'программист {}'.format(language),
            'area': '1',
            'period': '30'
    }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        number_of_vacancies[language] = response.json()['found']
    return number_of_vacancies

def get_python_salaries(url):
    python_salaries = []
    payload = {
        'text': 'программист python',
        'area': '1',
        'period': '30'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    python_vacancies = response.json()['items']
    for vacancy in python_vacancies:
        python_salaries.append(vacancy['salary'])
    return python_salaries

def predict_rub_salary():




if __name__ == '__main__':
    #print(count_msk_vacancies(URL, LANGUAGES))
    print(get_python_salaries(URL))