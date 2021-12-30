def count_avg_salaries(predicted_salaries):
    avg_salary = 0
    total_salary = 0
    vacancies_processed = 0
    for salary in predicted_salaries:
        if salary:
            total_salary += salary
            vacancies_processed += 1
    if not vacancies_processed:
        avg_salary = total_salary
        vacancies_processed = vacancies_processed
    else:
        avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed
