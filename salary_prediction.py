def predict_hh_rub_salary(salaries):
    predicted_rub_salaries = []
    for salary in salaries:
        if not salary:
            predicted_rub_salaries.append(0)
        elif salary['currency'] != 'RUR':
            predicted_rub_salaries.append(0)
        elif not salary['from']:
            predicted_rub_salaries.append(salary['to'] * 0.8)
        elif not salary['to']:
            predicted_rub_salaries.append(salary['from'] * 1.2)
        else:
            predicted_rub_salaries.append((salary['from'] + salary['to']) / 2)
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
    print(predicted_rub_salaries)
    return predicted_rub_salaries
