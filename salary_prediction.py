def filter_sj_vacancies(raw_salaries):
    filtered_sj_vacancies = []
    salary = []
    for vacancy in raw_salaries:
        salary.append(vacancy['payment_from'])
        salary.append(vacancy['payment_to'])
        salary.append(vacancy['currency'])
        if not salary[0] and not salary[1] or salary[2] != 'rub':
            salary = 0
            filtered_sj_vacancies.append(salary)
        else:
            filtered_sj_vacancies.append(salary[0:2])
        salary = []
    return filtered_sj_vacancies


def filter_hh_vacancies(raw_salaries):
    filtered_hh_vacancies = []
    salary = []
    filtered_salary = []
    for page in raw_salaries:
        for vacancy in page:
            salary.append(vacancy['salary'])
    for item in salary:
        if not item:
            item = 0
            filtered_hh_vacancies.append(item)
        elif item['currency'] != 'RUR':
            item = 0
            filtered_hh_vacancies.append(item)
        else:
            if not item['from']:
                filtered_salary = [0, item['to']]
            elif not item['to']:
                filtered_salary = [item['from'], 0]
            else:
                filtered_salary = [item['from'], item['to']]
            filtered_hh_vacancies.append(filtered_salary)
    return filtered_hh_vacancies


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
