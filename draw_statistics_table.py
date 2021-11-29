from terminaltables import AsciiTable
import statistics as stat


TABLE_DATA = [
    [
        'Язык программирования', 'Вакансий найдено',
        'Вакансий обработано', 'Средняя зарплата'
    ]
]


def draw_hh_table(table_data):
    title = 'HeadHunter Moscow'
    output_table = table_data.copy()
    for item in stat.make_hh_statistics():
        output_table.append(item)
    table_instance = AsciiTable(output_table, title)
    print(table_instance.table)


def draw_sj_table(table_data):
    title = 'SuperJob Moscow'
    output_table = table_data.copy()
    for item in stat.make_sj_statistics():
        output_table.append(item)
    table_instance = AsciiTable(output_table, title)
    print(table_instance.table)