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
        for key, value in raw_salaries[language].items():
            if not raw_salaries[language]['total']:
                predicted_rub_salaries[language] = {0: 0}
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
