import superjob_search
import headhunter_search
import utilities
from settings import SECRET_KEY
from terminaltables import AsciiTable

LANGUAGES = [
    'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
]
SJ_URL = 'https://api.superjob.ru/2.0/vacancies/'
HH_URL = 'https://api.hh.ru/vacancies'
TABLE_DATA = [
    [
        'Язык программирования', 'Вакансий найдено',
        'Вакансий обработано', 'Средняя зарплата'
    ]
]


def draw_hh_table(table_data):
    title = 'HeadHunter Moscow'
    output_table = table_data.copy()
    for item in make_hh_statistics():
        output_table.append(item)
    table_instance = AsciiTable(output_table, title)
    print(table_instance.table)


def draw_sj_table(table_data):
    title = 'SuperJob Moscow'
    output_table = table_data.copy()
    for item in make_sj_statistics():
        output_table.append(item)
    table_instance = AsciiTable(output_table, title)
    print(table_instance.table)


def make_hh_statistics():
    num_of_vacancies = headhunter_search.count_vacancies(HH_URL, LANGUAGES)
    raw_salaries = headhunter_search.get_raw_salaries(HH_URL, LANGUAGES)
    predicted_salaries = utilities.predict_hh_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    return stats


def make_sj_statistics():
    num_of_vacancies = superjob_search.count_vacancies(SJ_URL, SECRET_KEY,
                                                       LANGUAGES
                                                       )
    raw_salaries = superjob_search.get_raw_salaries(SJ_URL, LANGUAGES,
                                                    SECRET_KEY
                                                    )
    predicted_salaries = utilities.predict_sj_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    return stats


if __name__ == '__main__':
    draw_hh_table(TABLE_DATA)
    draw_sj_table(TABLE_DATA)
