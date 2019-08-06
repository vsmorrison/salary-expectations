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


def count_vacancies_by_language(languages):
    vacancies_found = {}
    url = 'https://api.hh.ru/vacancies'
    for language in languages:
        payload = {'text': 'программист {}'.format(language),
                   'area': '1',
                   'period': '30'
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        vacancies_found[language] = response.json()['found']
    print(vacancies_found)
    return vacancies_found


def get_salaries_by_language(languages):
    salaries = []
    for language in languages:
        url = 'https://api.hh.ru/vacancies'
        payload = {'text': 'программист {}'.format(language),
                   'area': '1',
                   'period': '30'
                   }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        items = response.json()['items']
        for item in items:
            salaries.append(item['salary'])
    rub_salaries = predict_rub_salary(salaries)
    vacancies_processed, average_salary = count_average_salary(rub_salaries)
    print(vacancies_processed, average_salary)
    return vacancies_processed, (average_salary)


def predict_rub_salary(salaries):
    rub_salaries = []
    for salary in salaries:
        if salary is None:
            rub_salaries.append(None)
        elif salary['currency'] != 'RUR':
            rub_salaries.append(None)
        elif salary['from'] is None:
            rub_salaries.append(salary['to'] * 0.8)
        elif salary['to'] is None:
            rub_salaries.append(salary['from'] * 1.2)
        elif salary['from'] is not None and salary['to'] is not None:
            rub_salaries.append((salary['from'] + salary['to']) / 2)
    return rub_salaries


def count_average_salary(rub_salaries):
    average_salary = 0
    vacancies_processed = len(rub_salaries)
    for salary in rub_salaries:
        if salary is None:
            vacancies_processed -= 1
            salary = 0
        average_salary += int(salary)
    average_salary /= vacancies_processed
    return vacancies_processed, int(average_salary)


def make_vacancies_statistics(vacancies_found):#, vacancies_processed, average_salaries
    statistics = {}
    for vacancy in vacancies_found:
        statistics[vacancy] = {}
        statistics[vacancy]['vacancies_found'] = vacancies_found[vacancy]
    print(statistics)



vacancies_found = count_vacancies_by_language(LANGUAGES)
#make_vacancies_statistics(vacancies_found)
salaries = get_salaries_by_language(LANGUAGES[0])
print(salaries)
#rub_salaries = predict_rub_salary(salaries)
#vacancies_processed, average_salary = count_average_salary(rub_salaries)
#print(vacancies_processed, average_salary)
