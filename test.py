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
    page = 0
    pages_number = 1
    raw_salaries = []
    salaries_by_page = []
    for language in languages:
        while page < pages_number:
            payload = {
                'text': 'программист {}'.format(language),
                'area': '1',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            items = response.json()['items']
            pages_number = response.json()['pages']
            print(page, language)
            for item in items:
                salaries_by_page.append(item['salary'])
            raw_salaries.append(salaries_by_page)
            salaries_by_page = []
        page += 1
    return raw_salaries


def predict_salaries(raw_salaries):
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_salaries.append(predict_rub_salary(salary))
    return predicted_salaries


def count_avg_salaries(predicted_salaries):
    vacancies_processed_values = []
    avg_salaries = []
    for salary in predicted_salaries:
        avg_salary, vacancies_processed = count_avg_salary(salary)
        avg_salaries.append(avg_salary)
        vacancies_processed_values.append(vacancies_processed)
    return avg_salaries, vacancies_processed_values


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
    print(stats)
    return stats


def test_for_pages(url):
    page = 0
    pages_number = 1
    while page <= pages_number:
        payload = {
            'text': 'программист python',
            'area': '1',
            'period': '30',
            'page': page
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        pages_number = response.json()['pages']
        print(page)
        page += 1




if __name__ == '__main__':
    #test_for_pages(URL)
    num_of_vacancies_by_lang = (count_vacancies_by_lang(URL, LANGUAGES))
    raw_salaries = get_raw_salaries(URL, LANGUAGES)
    predicted_salaries = predict_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = count_avg_salaries(predicted_salaries)
    stats = make_vacancies_stats(
        num_of_vacancies_by_lang,
        vacancies_processed_values,
        avg_salaries
    )