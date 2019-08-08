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


def get_pages(languages):
    page = 0
    page_count = 1
    url = 'https://api.hh.ru/vacancies'
    for language in languages:
        while page < page_count:
            payload = {
                'text': 'программист {}'.format(language),
                'area': '1',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            page += 1
            page_count = response.json()['pages']
            print(language, page)
        page = 0
    #print(languages, page)

def count_vacancies_by_language(languages):
    vacancies_found = {}
    url = 'https://api.hh.ru/vacancies'
    for language in languages:
        payload = {
            'text': 'программист {}'.format(language),
            'area': '1',
            'period': '30',
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        vacancies_found[language] = response.json()['found']
    return vacancies_found


def get_salaries_by_language(languages):
    raw_salaries = []
    rub_salaries = []
    vacancies_processed_storage = []
    average_salaries = []
    page = 0
    page_count = 1
    for language in languages:
        while page < page_count:
            url = 'https://api.hh.ru/vacancies'
            payload = {
                'text': 'программист {}'.format(language),
                'area': '1',
                'period': '30',
                'page': page
            }
            response = requests.get(url, params=payload)
            response.raise_for_status()
            items = response.json()['items']
            for item in items:
                raw_salaries.append(item['salary'])
            rub_salaries.append(predict_rub_salary(raw_salaries))
            raw_salaries = []
            page += 1
            page_count = response.json()['pages']
            print(language, page)
        page = 0
    for rub_salary in rub_salaries:
        vacancies_processed, average_salary = count_average_salary(rub_salary)
        vacancies_processed_storage.append(vacancies_processed)
        average_salaries.append(average_salary)
    return vacancies_processed_storage, average_salaries


def predict_rub_salary(salaries):
    rub_salaries = []
    for salary in salaries:
        if salary is None:
            rub_salaries.append(None)
        elif salary['currency'] != 'RUR':
            rub_salaries.append(None)
        elif salary['from'] is None:
            rub_salaries.append(salary['to'] * 0.8)
        elif salary['to'] is None:
            rub_salaries.append(salary['from'] * 1.2)
        elif salary['from'] is not None and salary['to'] is not None:
            rub_salaries.append((salary['from'] + salary['to']) / 2)
    return rub_salaries


def count_average_salary(rub_salaries):
    average_salary = 0
    vacancies_processed = len(rub_salaries)
    for salary in rub_salaries:
        if salary is None:
            vacancies_processed -= 1
            salary = 0
        average_salary += int(salary)
    average_salary /= vacancies_processed
    return vacancies_processed, int(average_salary)


def make_vacancies_statistics(vacancies_found, vacancies_processed, avg_salary):
    stats = {}
    for vacancy_num, vacancy in enumerate(vacancies_found):
        stats[vacancy] = {}
        stats[vacancy]['vacancies_found'] = vacancies_found[vacancy]
        stats[vacancy]['vacancies_processed'] = vacancies_processed[vacancy_num]
        stats[vacancy]['average_salary'] = avg_salary[vacancy_num]
    return stats


#if __name__ == '__main__':
#get_pages(LANGUAGES)
vacancies_found = count_vacancies_by_language(LANGUAGES)
vacancies_processed, average_salaries = get_salaries_by_language(LANGUAGES)
statistics = make_vacancies_statistics(
    vacancies_found,
    vacancies_processed,
    average_salaries
)
print(statistics)

