import superjob_search
import headhunter_search
from headhunter_search import HH_URL, HH_LANGUAGES
import utilities


def main():
    num_of_vacancies = headhunter_search.count_vacancies(HH_URL, HH_LANGUAGES)
    raw_salaries = headhunter_search.get_raw_salaries(HH_URL, HH_LANGUAGES)
    predicted_salaries = utilities.predict_salaries(raw_salaries)
    avg_salaries, vacancies_processed_values = utilities.count_avg_salaries(
        predicted_salaries)
    stats = utilities.make_vacancies_stats(
        num_of_vacancies,
        vacancies_processed_values,
        avg_salaries
    )
    print(stats)


if __name__ == '__main__':
    main()
