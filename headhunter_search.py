import requests
import salary_prediction
from itertools import count


def get_vacancies_by_lang(language, area, period):
    url = 'https://api.hh.ru/vacancies'
    vacancies_by_lang = []
    payload = {
        'text': f'программист {language}',
        'area': area,
        'period': period,
        'per_page': 100,
    }
    for page in count():
        payload['page'] = page
        response = requests.get(url, params=payload)
        response.raise_for_status()
        vacancies = response.json()
        pages_number = vacancies['pages']
        vacancies_by_lang.extend(vacancies['items'])
        if page >= pages_number-1:
            break
    total = vacancies['found']
    return vacancies_by_lang, total


def count_hh_predicted_salary(vacancy):
    if not vacancy['salary'] or vacancy['salary']['currency'] != 'RUR':
        return None
    return salary_prediction.predict_rub_salary(
        vacancy['salary']['from'], vacancy['salary']['to']
    )


def make_hh_statistics(languages, area, period):
    statistics = {}
    for language in languages:
        raw_vacancies, total = get_vacancies_by_lang(language, area, period)
        avg_salary, vacancies_processed = \
            salary_prediction.count_avg_salary(
                raw_vacancies, count_hh_predicted_salary
            )
        statistics[language] = {
            'total': total,
            'vacancies_processed': vacancies_processed,
            'avg_salary': avg_salary
        }
    return statistics
