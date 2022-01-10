import requests
import salary_prediction


def get_salaries_by_lang(url, language, secret_key):
    input_data = {'Moscow_id': 4, 'SPb_id': 14, 'SW_Development_id': 48}
    page = 0
    pages_number = 1
    while page < pages_number:
        headers = {
            'X-Api-App-Id': secret_key
        }
        payload = {
            'keyword': f'программист {language}',
            'town': f'{input_data["SPb_id"]}',
            'catalogues': f'{input_data["SW_Development_id"]}',
            'count': 100
        }
        response = requests.get(url, params=payload, headers=headers)
        response.raise_for_status()
        items = response.json()
        page += 1
    salaries_by_lang = items['objects']
    total = items['total']
    return salaries_by_lang, total


def filter_sj_vacancies(raw_salaries):
    filtered_sj_vacancies = []
    salary = []
    for vacancy in raw_salaries:
        salary.append(vacancy['payment_from'])
        salary.append(vacancy['payment_to'])
        salary.append(vacancy['currency'])
        if not salary[0] and not salary[1] or salary[2] != 'rub':
            salary = 0
            filtered_sj_vacancies.append(salary)
        else:
            filtered_sj_vacancies.append(salary[0:2])
        salary = []
    return filtered_sj_vacancies


def make_sj_statistics(languages, secret_key):
    statistics = {}
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'
    for language in languages:
        raw_salaries, total = get_salaries_by_lang(sj_url, language, secret_key)
        filtered_sj_vacancies = salary_prediction.filter_sj_vacancies(raw_salaries)
        predicted_salaries = salary_prediction.predict_rub_salaries(filtered_sj_vacancies)
        avg_salary, vacancies_processed = salary_prediction.count_avg_salaries(predicted_salaries)
        statistics[language] = {}
        statistics[language]['total'] = total
        statistics[language]['vacancies_processed'] = vacancies_processed
        statistics[language]['avg_salary'] = avg_salary
    return statistics
