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


def predict_rub_salaries(filtered_vacancies):
    predicted_salaries = []
    prediction = 0
    for vacancy in filtered_vacancies:
        if vacancy:
            if vacancy[0] == 0:
                prediction = vacancy[1] * 0.8
            elif not vacancy[1]:
                prediction = vacancy[0] * 1.2
            else:
                prediction = (vacancy[0] + vacancy[1]) / 2
            predicted_salaries.append(prediction)
        else:
            predicted_salaries.append(vacancy)
    return predicted_salaries





def predict_hh_rub_salary(raw_salaries):
    predicted_rub_salaries = {}
    vacancy = {}
    prediction = 0
    for language in raw_salaries:
        predicted_rub_salaries[language] = {}
        for key, value in raw_salaries[language]['vacancies'].items():
            if not value['salary']:
                prediction = 0
            elif value['salary']['currency'] != 'RUR':
                prediction = 0
            elif not value['salary']['from']:
                prediction = value['salary']['to'] * 0.8
            elif not value['salary']['to']:
                prediction = value['salary']['from'] * 1.2
            else:
                prediction = (value['salary']['from'] + value['salary']['to']) / 2
            predicted_rub_salaries[language][key] = prediction
    return predicted_rub_salaries


def predict_sj_rub_salary(raw_salaries):
    predicted_rub_salaries = {}
    vacancy = {}
    prediction = 0
    for language in raw_salaries:
        predicted_rub_salaries[language] = {}
        for key, value in raw_salaries[language]['vacancies'].items():
            if not value:
                prediction = 0
            elif value['currency'] != 'rub':
                prediction = 0
            elif not value['from'] and not value['to']:
                prediction = 0
            elif not value['from'] and value['to'] != 0:
                prediction = value['to'] * 0.8
            elif not value['to'] and value['from'] != 0:
                prediction = value['from'] * 1.2
            else:
                prediction = (value['to'] + value['from']) / 2
            predicted_rub_salaries[language][key] = prediction
    return predicted_rub_salaries
