import requests
import salary_prediction
from itertools import count


def get_salaries_by_lang(url, language):
    input_data = {'Moscow_id': 1, 'SPb_id': 2}
    salaries_by_lang = []
    for page in count():
        payload = {
            'text': f'программист {language}',
            'area': input_data["Moscow_id"],
            'period': '30',
            'page': page
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        items = response.json()
        pages_number = items['pages']
        print(language, page)
        salaries_by_lang.extend(items['items'])
        if page >= pages_number:
            break
    total = items['found']
    return salaries_by_lang, total


def count_hh_salaries(raw_salaries):
    total_salary = 0
    vacancies_processed = 0
    for vacancy in raw_salaries:
        if vacancy['salary']:
            if vacancy['salary']['currency'] == 'RUR':
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
            else:
                salary_from = 0
                salary_to = 0
        else:
            salary_from = 0
            salary_to = 0
        predicted_salary = salary_prediction.predict_rub_salaries(salary_from, salary_to)
        if predicted_salary:
            total_salary += predicted_salary
            vacancies_processed += 1
    if vacancies_processed:
        avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed


def make_hh_statistics(languages, url):
    statistics = {}
    for language in languages:
        raw_salaries, total = get_salaries_by_lang(url, language)
        avg_salary, vacancies_processed = count_hh_salaries(raw_salaries)
        statistics[language] = {
            'total': total,
            'vacancies_processed': vacancies_processed,
            'avg_salary': avg_salary
        }
    return statistics
