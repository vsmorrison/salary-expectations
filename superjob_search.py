import requests
import salary_prediction
from itertools import count


def get_vacancies_by_lang(language, secret_key, town, catalogues):
    url = 'https://api.superjob.ru/2.0/vacancies'
    vacancies_by_lang = []
    headers = {
        'X-Api-App-Id': secret_key
    }
    payload = {
        'keyword': f'программист {language}',
        'town': town,
        'catalogues': catalogues,
        'count': 100
    }
    for page in count():
        payload['page'] = page
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        vacancies = response.json()
        vacancies_by_lang.extend(vacancies['objects'])
        if not vacancies['more']:
            break
    total = vacancies['total']
    return vacancies_by_lang, total


def count_sj_predicted_salary(vacancy):
    if vacancy['currency'] != 'rub':
        return None
    return salary_prediction.predict_rub_salary(
        vacancy['payment_from'], vacancy['payment_to']
    )


def make_sj_statistics(languages, secret_key, town, catalogues):
    statistics = {}
    for language in languages:
        raw_vacancies, total = get_vacancies_by_lang(
            language, secret_key, town, catalogues
        )
        avg_salary, vacancies_processed = \
            salary_prediction.count_avg_salaries(
                raw_vacancies, count_sj_predicted_salary
            )
        statistics[language] = {
            'total': total,
            'vacancies_processed': vacancies_processed,
            'avg_salary': avg_salary
        }
    return statistics
