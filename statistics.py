import superjob_search
import headhunter_search
import utilities
from settings import SECRET_KEY


LANGUAGES = [
    'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
]


def make_hh_statistics():
    hh_url = 'https://api.hh.ru/vacancies'
    num_of_vacancies = headhunter_search.count_vacancies(hh_url, LANGUAGES)
    raw_salaries = headhunter_search.get_raw_salaries(hh_url, LANGUAGES)
    predicted_salaries = utilities.predict_hh_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    return stats


def make_sj_statistics():
    sj_url = 'https://api.superjob.ru/2.0/vacancies/'
    num_of_vacancies = superjob_search.count_vacancies(sj_url, SECRET_KEY,
                                                       LANGUAGES
                                                       )
    raw_salaries = superjob_search.get_raw_salaries(sj_url, LANGUAGES,
                                                    SECRET_KEY
                                                    )
    predicted_salaries = utilities.predict_sj_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    return stats
