def predict_rub_salary(salary_from, salary_to):
    if not salary_from and not salary_to:
        prediction = 0
    elif not salary_from:
        prediction = salary_to * 0.8
    elif not salary_to:
        prediction = salary_from * 1.2
    else:
        prediction = (salary_from + salary_to) / 2
    return prediction


def count_avg_salaries(raw_vacancies, count_salary):
    avg_salary = 0
    total_salary = 0
    vacancies_processed = 0
    for vacancy in raw_vacancies:
        predicted_salary = count_salary(vacancy)
        if predicted_salary:
            total_salary += predicted_salary
            vacancies_processed += 1
    if vacancies_processed:
        avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed
