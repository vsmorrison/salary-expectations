import superjob_search
import headhunter_search
import salary_count as sc
import salary_prediction as sp


LANGUAGES = [
    'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
]


def make_hh_statistics():
    hh_url = 'https://api.hh.ru/vacancies'
    raw_salaries = headhunter_search.get_salaries_by_lang(hh_url, LANGUAGES)
    predicted_salaries = sp.predict_hh_rub_salary(raw_salaries)
    avg_salaries = sc.count_avg_salaries(predicted_salaries)
    stats = make_vacancies_stats(raw_salaries, avg_salaries)
    return stats


def make_sj_statistics():
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'
    raw_salaries = superjob_search.get_salaries_by_lang(sj_url, LANGUAGES,
                                                        SECRET_KEY
                                                        )
    predicted_salaries = sp.predict_sj_rub_salary(raw_salaries)
    avg_salaries = sc.count_avg_salaries(predicted_salaries)
    stats = make_vacancies_stats(raw_salaries, avg_salaries)
    return stats


def make_vacancies_stats(raw_salaries, avg_salaries):
    statistics = {}
    for language in raw_salaries:
        statistics[language] = {}
        statistics[language]['vacancies_found'] = raw_salaries[language]['total']
        statistics[language]['vacancies_processed'] = avg_salaries[language]['vacancies_processed']
        statistics[language]['avg_salary'] = avg_salaries[language]['avg_salary']
    return statistics
