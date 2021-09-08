def predict_salaries(raw_salaries):
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_salaries.append(predict_rub_salary(salary))
    return predicted_salaries


def count_avg_salaries(predicted_salaries):
    vacancies_processed_values = []
    avg_salaries = []
    for salary in predicted_salaries:
        avg_salary, vacancies_processed = count_avg_salary(salary)
        avg_salaries.append(avg_salary)
        vacancies_processed_values.append(vacancies_processed)
    return avg_salaries, vacancies_processed_values


def predict_rub_salary(salaries):
    predicted_rub_salaries = []
    for salary in salaries:
        if salary is None:
            predicted_rub_salaries.append(0)
        elif salary['currency'] != 'RUR':
            predicted_rub_salaries.append(0)
        elif salary['from'] is None:
            predicted_rub_salaries.append(salary['to'] * 0.8)
        elif salary['to'] is None:
            predicted_rub_salaries.append(salary['from'] * 1.2)
        else:
            predicted_rub_salaries.append((salary['from'] + salary['to']) / 2)
    return predicted_rub_salaries


def count_avg_salary(salaries):
    vacancies_processed = 0
    total_salary = 0
    for salary in salaries:
        if salary != 0:
            vacancies_processed += 1
            total_salary += salary
    avg_salary = int(total_salary / vacancies_processed)
    return avg_salary, vacancies_processed


def make_vacancies_stats(vacancies_found, vacancies_processed, avg_salaries):
    stats = {}
    for vacancy_num, vacancy in enumerate(vacancies_found):
        stats[vacancy] = {}
        stats[vacancy]['vacancies_found'] = vacancies_found[vacancy]
        stats[vacancy]['vacancies_processed'] = vacancies_processed[vacancy_num]
        stats[vacancy]['average_salary'] = avg_salaries[vacancy_num]
    return stats
