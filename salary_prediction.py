def predict_rub_salaries(filtered_vacancies):
    predicted_salaries = []
    prediction = 0
    for vacancy in filtered_vacancies:
        if vacancy:
            if not vacancy[0]:
                prediction = vacancy[1] * 0.8
            elif not vacancy[1]:
                prediction = vacancy[0] * 1.2
            else:
                prediction = (vacancy[0] + vacancy[1]) / 2
            predicted_salaries.append(prediction)
        else:
            predicted_salaries.append(vacancy)
    return predicted_salaries


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
