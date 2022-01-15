import os
from dotenv import load_dotenv
import superjob_search
import headhunter_search
import draw_statistics_table


def main():
    load_dotenv()
    sj_secret_key = os.getenv('SJ_SECRET_KEY')
    sj_query_params = {'Moscow_id': 4, 'SPb_id': 14, 'SW_Development_id': 48}
    hh_query_params = {'Moscow_id': 1, 'SPb_id': 2, 'days_from_publishing': 30}

    languages = [
        'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
    ]
    hh_stat = headhunter_search.make_hh_statistics(
        languages, hh_query_params['Moscow_id'],
        hh_query_params['days_from_publishing']
    )
    hh_table = draw_statistics_table.draw_table(hh_stat, 'HeadHunter Moscow')
    sj_stat = superjob_search.make_sj_statistics(
        languages,
        sj_secret_key,
        sj_query_params['Moscow_id'],
        sj_query_params['SW_Development_id']
    )
    sj_table = draw_statistics_table.draw_table(sj_stat, 'SuperJob Moscow')
    print(hh_table.table)
    print(sj_table.table)


if __name__ == '__main__':
    main()
