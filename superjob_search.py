import requests
import salary_prediction
from itertools import count


def get_salaries_by_lang(url, language, secret_key, town, catalogues):
    salaries_by_lang = []
    for page in count():
        headers = {
            'X-Api-App-Id': secret_key
        }
        payload = {
            'keyword': f'программист {language}',
            'town': town,
            'catalogues': catalogues,
            'page': page,
            'count': 100
        }
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        items = response.json()
        salaries_by_lang.extend(items['objects'])
        if not items['more']:
            break
    total = items['total']
    return salaries_by_lang, total


def count_sj_salaries(raw_salaries):
    total_salary = 0
    avg_salary = 0
    vacancies_processed = 0
    for vacancy in raw_salaries:
        if vacancy['currency'] == 'rub':
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
        else:
            salary_from = 0
            salary_to = 0
        predicted_salary = salary_prediction.predict_rub_salaries(
            salary_from, salary_to
        )
        if predicted_salary:
            total_salary += predicted_salary
            vacancies_processed += 1
    if vacancies_processed:
        avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed


def make_sj_statistics(languages, secret_key, url, town, catalogues):
    statistics = {}
    for language in languages:
        raw_salaries, total = get_salaries_by_lang(
            url, language, secret_key, town, catalogues
        )
        avg_salary, vacancies_processed = count_sj_salaries(raw_salaries)
        statistics[language] = {
            'total': total,
            'vacancies_processed': vacancies_processed,
            'avg_salary': avg_salary
        }
    return statistics
