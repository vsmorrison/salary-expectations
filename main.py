import os
from dotenv import load_dotenv
import superjob_search
import headhunter_search
import draw_statistics_table


def main():
    load_dotenv()
    sj_secret_key = os.getenv('SJ_SECRET_KEY')
    api_urls = {
        'SuperJob': 'https://api.superjob.ru/2.0/vacancies/',
        'HeadHunter': 'https://api.hh.ru/vacancies'
    }
    languages = [
        'Ruby', 'Go'
    ]
    # languages = [
    #     'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
    # ]
    hh_stat = headhunter_search.make_hh_statistics(languages, api_urls['HeadHunter'])
    hh_table = draw_statistics_table.draw_tables(hh_stat, 'HeadHunter Moscow')
    sj_stat = superjob_search.make_sj_statistics(languages, sj_secret_key, api_urls['SuperJob'])
    sj_table = draw_statistics_table.draw_tables(sj_stat, 'SuperJob Moscow')
    print(hh_table.table)
    print(sj_table.table)


if __name__ == '__main__':
    main()
