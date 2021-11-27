def predict_hh_salaries(raw_salaries):
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_salaries.append(predict_hh_rub_salary(salary))
    return predicted_salaries


def predict_hh_rub_salary(salaries):
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


def predict_sj_rub_salary(salaries):
    predicted_rub_salaries = []
    for salary in salaries:
        if salary is None:
            predicted_rub_salaries.append(0)
        elif salary[-1] != 'rub':
            predicted_rub_salaries.append(0)
        elif salary[0] == 0 and salary[1] == 0:
            predicted_rub_salaries.append(0)
        elif salary[0] == 0 and salary[1] != 0:
            predicted_rub_salaries.append(salary[1] * 0.8)
        elif salary[1] == 0 and salary[0] != 0:
            predicted_rub_salaries.append(salary[0] * 1.2)
        else:
            predicted_rub_salaries.append((salary[0] + salary[1]) / 2)
    return predicted_rub_salaries


def predict_sj_salaries(raw_salaries):
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_salaries.append(predict_sj_rub_salary(salary))
    return predicted_salaries


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


def make_vacancies_stats(vacancies_found, vacancies_processed, avg_salaries):
    stats = []
    stats_by_language = []
    for vacancy_num, vacancy in enumerate(vacancies_found):
        stats_by_language.append(vacancy)
        stats_by_language.append(vacancies_found[vacancy])
        stats_by_language.append(vacancies_processed[vacancy_num])
        stats_by_language.append(avg_salaries[vacancy_num])
        stats.append(stats_by_language)
        stats_by_language = []
    return stats
