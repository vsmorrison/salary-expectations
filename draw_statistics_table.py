from terminaltables import AsciiTable


def draw_table(statistics, table_name):
    table_rows = [
        [
            'Язык программирования', 'Вакансий найдено',
            'Вакансий обработано', 'Средняя зарплата'
        ]
    ]
    for language, stats in statistics.items():
        table_row = [
            language, stats['total'],
            stats['vacancies_processed'],
            stats['avg_salary']
        ]
        table_rows.append(table_row)
    table_instance = AsciiTable(table_rows, table_name)
    return table_instance
