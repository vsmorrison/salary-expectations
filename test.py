import requests
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

TEST = [
    1,
    2,
    3,
    4
]
URL = 'https://api.hh.ru/vacancies'


def count_vacancies_by_lang(url, languages):
    num_of_vacancies = {}
    for language in languages:
        payload = {
            'text': 'программист {}'.format(language),
            'area': '1',
            'period': '30'
    }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        num_of_vacancies[language] = response.json()['found']
    return num_of_vacancies


def get_avg_salaries(url, languages):
    raw_salaries = []
    predicted_salaries = []
    avg_salaries = []
    vacancies_processed_strg = []
    for language in languages:
        payload = {
            'text': 'программист {}'.format(language),
            'area': '1',
            'period': '30'
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        language_vacancies = response.json()['items']
        for vacancy in language_vacancies:
            raw_salaries.append(vacancy['salary'])
        predicted_salaries.append(predict_rub_salary(raw_salaries))
        for salary in predicted_salaries:
            avg_salary, vacancies_processed = count_avg_salary(salary)
        avg_salaries.append(avg_salary)
        vacancies_processed_strg.append(vacancies_processed)
    return avg_salaries, vacancies_processed_strg


def count_avg_salary(salaries):
    vacancies_processed = len(salaries)
    total_salary = 0
    for salary in salaries:
        if salary == 0:
            vacancies_processed -= 1
        total_salary += salary
    avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed



def predict_rub_salary(python_salaries):
    predicted_rub_salaries = []
    for salary in python_salaries:
        if salary is None:
            predicted_rub_salaries.append(0)
        elif salary['currency'] != 'RUR':
            predicted_rub_salaries.append(0)
        elif salary['from'] is None:
            predicted_rub_salaries.append(salary['to'] * 0.8)
        elif salary['to'] is None:
            predicted_rub_salaries.append(salary['from'] * 1.2)
        else:
            predicted_rub_salaries.append((salary['from'] + salary['to']) / 2)
    return predicted_rub_salaries


def make_vacancies_stats(vacancies_found, vacancies_processed, avg_salaries):
    statistics = {}
    for

if __name__ == '__main__':
    #print(count_vacancies_by_lang(URL, LANGUAGES))
    num_of_vacancies_by_lang = (count_vacancies_by_lang(URL, LANGUAGES))
    salaries = (get_avg_salaries(URL, LANGUAGES))
    #print(count_avg_salary(TEST))
    #for salary in salaries:
    #    print(salary)
    #predicted_salaries = (predict_rub_salary(salaries))
    #print(predicted_salaries)'''
    #vacancies_stats = make_vacancies_stats()
