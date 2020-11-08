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
    [
        1,
        2,
        3,
        4
    ],
    [
        5,
        6,
        7,
        8
    ]
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
    vacancies_processed = 0
    total_salary = 0
    for salary in salaries:
        if salary != 0:
            vacancies_processed += 1
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
    stats = {}
    for vacancy_num, vacancy in enumerate(vacancies_found):
        stats[vacancy] = {}
        stats[vacancy]['vacancies_found'] = vacancies_found[vacancy]
        stats[vacancy]['vacancies_processed'] = vacancies_processed[vacancy_num]
        stats[vacancy]['average_salary'] = avg_salaries[vacancy_num]
        #stats[vacancy]['vacanies_found'] = vacancies_found[vacancy]
    #print(stats)'''
    return stats


if __name__ == '__main__':
    #print(count_vacancies_by_lang(URL, LANGUAGES))
    num_of_vacancies_by_lang = (count_vacancies_by_lang(URL, LANGUAGES))
    avg_salaries, vacancies_processed = (get_avg_salaries(URL, LANGUAGES))
    stats = make_vacancies_stats(num_of_vacancies_by_lang, vacancies_processed, avg_salaries)
    #print(stats)
    print(avg_salaries)
    print(vacancies_processed)
    #print(count_avg_salary(TEST))
    #for salary in salaries:
    #    print(salary)
    #predicted_salaries = (predict_rub_salary(salaries))
    #print(predicted_salaries)'''
    #vacancies_stats = make_vacancies_stats()
    #print(test(TEST))