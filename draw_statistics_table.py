from terminaltables import AsciiTable
import statistics as stat


TABLE_DATA = [
    [
        'Язык программирования', 'Вакансий найдено',
        'Вакансий обработано', 'Средняя зарплата'
    ]
]

#
# def draw_hh_table(table_data):
#     title = 'HeadHunter Moscow'
#     output_table = table_data.copy()
#     for item in stat.make_hh_statistics():
#         output_table.append(item)
#     table_instance = AsciiTable(output_table, title)
#     print(table_instance.table)


# def draw_sj_table(table_data):
#     title = 'SuperJob Moscow'
#     output_table = table_data.copy()
#     for item in stat.make_sj_statistics():
#         output_table.append(item)
#     table_instance = AsciiTable(output_table, title)
#     print(table_instance.table)


def draw_tables(table_data):
    title_hh = 'HeadHunter Moscow'
    title_sj = 'SuperJob Moscow'
    hh_table = table_data.copy()
    sj_table = table_data.copy()
    for item in stat.make_hh_statistics():
        hh_table.append(item)
    hh_table_instance = AsciiTable(hh_table, title_hh)
    print(hh_table_instance.table)
    for item in stat.make_sj_statistics():
        sj_table.append(item)
    sj_table_instance = AsciiTable(sj_table, title_sj)
    print(sj_table_instance.table)
