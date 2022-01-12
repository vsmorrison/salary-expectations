from terminaltables import AsciiTable


def draw_table(statistics, table_name):
    table_header = [
        [
            'Язык программирования', 'Вакансий найдено',
            'Вакансий обработано', 'Средняя зарплата'
        ]
    ]
    table_row = []
    table = table_header
    for language, stats_value in statistics.items():
        table_row = [
            language, stats_value['total'],
            stats_value['vacancies_processed'],
            stats_value['avg_salary']
        ]
        table.append(table_row)
        table_row = []
    table_instance = AsciiTable(table, table_name)
    return table_instance
