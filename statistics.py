import superjob_search
import headhunter_search
import salary_count as sc
import salary_prediction as sp


def make_hh_statistics(languages):
    hh_url = 'https://api.hh.ru/vacancies'
    raw_salaries = headhunter_search.get_salaries_by_lang(hh_url, languages)
    predicted_salaries = sp.predict_hh_rub_salary(raw_salaries)
    avg_salaries = sc.count_avg_salaries(predicted_salaries)
    stats = make_vacancies_stats(raw_salaries, avg_salaries)
    return stats


def make_sj_statistics(languages, secret_key):
    statistics = {}
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'
    for language in languages:
        raw_salaries, total = superjob_search.get_salaries_by_lang(sj_url,
                                                                   language,
                                                                   secret_key
                                                                   )
        filtered_sj_vacancies = sp.filter_sj_vacancies(raw_salaries)
        predicted_salaries = sp.predict_rub_salaries(filtered_sj_vacancies)
        avg_salary, vacancies_processed = sc.count_avg_salaries(predicted_salaries)
        statistics[language] = {}
        statistics[language]['total'] = total
        statistics[language]['vacancies_processed'] = vacancies_processed
        statistics[language]['avg_salary'] = avg_salary
    print(statistics)
    return statistics


def make_vacancies_stats(raw_salaries, avg_salaries):
    statistics = {}
    for language in raw_salaries:
        statistics[language] = {}
        statistics[language]['vacancies_found'] = raw_salaries[language]['total']
        statistics[language]['vacancies_processed'] = avg_salaries[language]['vacancies_processed']
        statistics[language]['avg_salary'] = avg_salaries[language]['avg_salary']
    return statistics
