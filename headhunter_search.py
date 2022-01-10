import requests
import salary_prediction


def get_salaries_by_lang(url, language):
    input_data = {'Moscow_id': 1, 'SPb_id': 2}
    page = 0
    pages_number = 1
    salaries_by_lang = []
    while page < pages_number:
        payload = {
            'text': f'{language}',
            'area': f'{input_data["SPb_id"]}',
            'period': '30',
            'page': page
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        items = response.json()
        pages_number = items['pages']
        print(language, page)
        page += 1
        salaries_by_lang.append(items['items'])
    total = items['found']
    return salaries_by_lang, total


def filter_hh_vacancies(raw_salaries):
    filtered_hh_vacancies = []
    salary = []
    filtered_salary = []
    for page in raw_salaries:
        for vacancy in page:
            salary.append(vacancy['salary'])
    for item in salary:
        if not item:
            item = 0
            filtered_hh_vacancies.append(item)
        elif item['currency'] != 'RUR':
            item = 0
            filtered_hh_vacancies.append(item)
        else:
            if not item['from']:
                filtered_salary = [0, item['to']]
            elif not item['to']:
                filtered_salary = [item['from'], 0]
            else:
                filtered_salary = [item['from'], item['to']]
            filtered_hh_vacancies.append(filtered_salary)
    return filtered_hh_vacancies


def make_hh_statistics(languages):
    statistics = {}
    hh_url = 'https://api.hh.ru/vacancies'
    for language in languages:
        raw_salaries, total = get_salaries_by_lang(hh_url, language)
        filtered_hh_vacancies = salary_prediction.filter_hh_vacancies(raw_salaries)
        predicted_salaries = salary_prediction.predict_rub_salaries(filtered_hh_vacancies)
        avg_salary, vacancies_processed = salary_prediction.count_avg_salaries(predicted_salaries)
        statistics[language] = {}
        statistics[language]['total'] = total
        statistics[language]['vacancies_processed'] = vacancies_processed
        statistics[language]['avg_salary'] = avg_salary
    return statistics
