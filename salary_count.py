# def count_avg_salaries(predicted_salaries):
#     vacancies_processed_values = []
#     avg_salaries = []
#     for salary in predicted_salaries:
#         avg_salary, vacancies_processed = count_avg_salary(salary)
#         avg_salaries.append(avg_salary)
#         vacancies_processed_values.append(vacancies_processed)
#     return avg_salaries, vacancies_processed_values

def count_avg_salaries(predicted_salaries):
    #vacancies_processed_values = {}
    avg_salaries = {}
    total_salary = 0
    vacancies_processed = 0
    for language in predicted_salaries:
        avg_salaries[language] = {}
        for value in predicted_salaries[language].values():
            if value:
                total_salary += value
                vacancies_processed += 1
            avg_salary = int(total_salary / vacancies_processed)
            avg_salaries[language]['avg_salary'] = avg_salary
            avg_salaries[language]['vacancies_processed'] = vacancies_processed
        total_salary = 0
        vacancies_processed = 0
    print(avg_salaries)
    return avg_salaries


def count_avg_salary(salaries):
    vacancies_processed = 0
    total_salary = 0
    for salary in salaries:
        if salary:
            vacancies_processed += 1
            total_salary += salary
    avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed


# def count_avg_salary(salaries):
#     vacancies_processed = 0
#     total_salary = 0
#     for salary in salaries:
#         if salary != 0:
#             vacancies_processed += 1
#             total_salary += salary
#     avg_salary = int(total_salary / vacancies_processed)
#     return avg_salary, vacancies_processed
