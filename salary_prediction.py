def predict_rub_salaries(salary_from, salary_to):
    if not salary_from:
        prediction = salary_to * 0.8
    elif not salary_to:
        prediction = salary_from * 1.2
    else:
        prediction = (salary_from + salary_to) / 2
    return prediction