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