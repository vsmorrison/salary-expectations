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
    ],
    [
        10,
        10,
        10,
        10,
        10
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


def get_raw_salaries(url, languages):
    raw_salaries = []
    salaries_by_page = []
    for language in languages:
        payload = {
            'text': 'программист {}'.format(language),
            'area': '1',
            'period': '30'
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        items = response.json()['items']
        for item in items:
            salaries_by_page.append(item['salary'])
        raw_salaries.append(salaries_by_page)
    return raw_salaries


def predict_rub_salaries(raw_salaries):
    predicted_rub_salary = []
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_rub_salary.append(predict_rub_salary(salary))
        predicted_salaries.append(predicted_rub_salary)
        predicted_rub_salary = []
    #for salary in predicted_salaries:
    #avg_salary, vacancies_processed = count_avg_salary(predicted_salaries)
    #avg_salaries.append(avg_salary)
    #vacancies_processed_strg.append(vacancies_processed)
    #print(avg_salaries)
    print(predicted_salaries)
    print(len(predicted_salaries))
    #print(raw_salaries)
    #print(avg_salaries)'''
    return predicted_salaries


def predict_rub_salary(salaries):
    predicted_rub_salaries = []
    for salary in salaries:
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


def count_avg_salary(salaries):
    vacancies_processed = 0
    total_salary = 0
    for salary in salaries:
        if salary != 0:
            vacancies_processed += 1
            total_salary += salary
    avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed


def make_vacancies_stats(vacancies_found, vacancies_processed, avg_salaries):
    stats = {}
    for vacancy_num, vacancy in enumerate(vacancies_found):
        stats[vacancy] = {}
        stats[vacancy]['vacancies_found'] = vacancies_found[vacancy]
        stats[vacancy]['vacancies_processed'] = vacancies_processed[vacancy_num]
        stats[vacancy]['average_salary'] = avg_salaries[vacancy_num]
        #stats[vacancy]['vacanies_found'] = vacancies_found[vacancy]
    print(stats)
    return stats


if __name__ == '__main__':
    #print(count_vacancies_by_lang(URL, LANGUAGES))
    num_of_vacancies_by_lang = (count_vacancies_by_lang(URL, LANGUAGES))
    raw_salaries = get_raw_salaries(URL, LANGUAGES)
    predicted_salaries = predict_rub_salaries(raw_salaries)
    #stats = make_vacancies_stats(num_of_vacancies_by_lang, vacancies_processed, avg_salaries)
    #print(stats)
    #print(avg_salaries)
    #print(vacancies_processed)
    #for salary in salaries:
    #    print(salary)
    #predicted_salaries = (predict_rub_salary(salaries))
    #print(predicted_salaries)'''
    #vacancies_stats = make_vacancies_stats()
    #print(test(TEST))

    '''for i in range(len(TEST)):
        avg_salary, vacancies_processed = count_avg_salary(TEST[i])
        print(avg_salary)
        print(vacancies_processed)'''