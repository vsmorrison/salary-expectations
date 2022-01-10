import requests
import salary_count as sc
import salary_prediction as sp

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


def make_hh_statistics(languages):
    statistics = {}
    hh_url = 'https://api.hh.ru/vacancies'
    for language in languages:
        raw_salaries, total = get_salaries_by_lang(hh_url, language)
        filtered_hh_vacancies = sp.filter_hh_vacancies(raw_salaries)
        predicted_salaries = sp.predict_rub_salaries(filtered_hh_vacancies)
        avg_salary, vacancies_processed = sc.count_avg_salaries(predicted_salaries)
        statistics[language] = {}
        statistics[language]['total'] = total
        statistics[language]['vacancies_processed'] = vacancies_processed
        statistics[language]['avg_salary'] = avg_salary
    return statistics
