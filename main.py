import os
from dotenv import load_dotenv
import statistics as s
import draw_statistics_table as dst


def main():
    load_dotenv()
    sj_secret_key = os.getenv('SJ_SECRET_KEY')
    languages = [
        'Javascript', 'Java', 'Python', 'Ruby', 'PHP', 'C++', 'C#', 'C', 'Go'
    ]
    hh_stat = s.make_hh_statistics(languages)
    hh_table = dst.draw_tables(hh_stat, 'HeadHunter Moscow')
    sj_stat = s.make_sj_statistics(languages, sj_secret_key)
    sj_table = dst.draw_tables(sj_stat, 'SuperJob Moscow')
    print(sj_table.table)
    print(hh_table.table)


if __name__ == '__main__':
    main()
