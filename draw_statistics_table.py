from terminaltables import AsciiTable


def draw_tables(statistics, name):
    table_data = [
        [
            'Язык программирования', 'Вакансий найдено',
            'Вакансий обработано', 'Средняя зарплата'
        ]
    ]
    row = []
    table = table_data
    for key, value in statistics.items():
        row = [key, value['total'], value['vacancies_processed'],
               value['avg_salary']]
        table.append(row)
        row = []
    table_instance = AsciiTable(table, name)
    return table_instance
