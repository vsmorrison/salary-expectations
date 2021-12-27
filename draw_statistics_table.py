from terminaltables import AsciiTable
import statistics as s


TABLE_DATA = [
    [
        'Язык программирования', 'Вакансий найдено',
        'Вакансий обработано', 'Средняя зарплата'
    ]
]


def draw_tables(table_data):
    row = []
    title_hh = 'HeadHunter Moscow'
    title_sj = 'SuperJob Moscow'
    hh_table = table_data.copy()
    sj_table = table_data.copy()
    for key, value in s.make_hh_statistics().items():
        row = [key, value['vacancies_found'], value['vacancies_processed'],
               value['avg_salary']]
        hh_table.append(row)
        row = []
    hh_table_instance = AsciiTable(hh_table, title_hh)
    print(hh_table_instance.table)
    for key, value in s.make_sj_statistics().items():
        row = [key, value['vacancies_found'], value['vacancies_processed'],
               value['avg_salary']]
        sj_table.append(row)
        row = []
    sj_table_instance = AsciiTable(sj_table, title_sj)
    print(sj_table_instance.table)
