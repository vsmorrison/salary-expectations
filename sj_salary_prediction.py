def predict_sj_rub_salary(salaries):
    predicted_rub_salaries = []
    for salary in salaries:
        if not salary:
            predicted_rub_salaries.append(0)
        elif salary[-1] != 'rub':
            predicted_rub_salaries.append(0)
        elif not salary[0] and not salary[1]:
            predicted_rub_salaries.append(0)
        elif not salary[0] and salary[1] != 0:
            predicted_rub_salaries.append(salary[1] * 0.8)
        elif not salary[1] and salary[0] != 0:
            predicted_rub_salaries.append(salary[0] * 1.2)
        else:
            predicted_rub_salaries.append((salary[0] + salary[1]) / 2)
    return predicted_rub_salaries


def predict_sj_salaries(raw_salaries):
    predicted_salaries = []
    for salary in raw_salaries:
        predicted_salaries.append(predict_sj_rub_salary(salary))
    return predicted_salaries