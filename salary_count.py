def count_avg_salaries(predicted_salaries):
    vacancies_processed_values = []
    avg_salaries = []
    for salary in predicted_salaries:
        avg_salary, vacancies_processed = count_avg_salary(salary)
        avg_salaries.append(avg_salary)
        vacancies_processed_values.append(vacancies_processed)
    return avg_salaries, vacancies_processed_values


def count_avg_salary(salaries):
    vacancies_processed = 0
    total_salary = 0
    for salary in salaries:
        if salary != 0:
            vacancies_processed += 1
            total_salary += salary
    avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed
