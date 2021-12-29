import os
from dotenv import load_dotenv
import draw_statistics_table as dst


def main():
    load_dotenv()
    sj_secret_key = os.getenv('SJ_SECRET_KEY')
    dst.draw_tables(dst.TABLE_DATA)


if __name__ == '__main__':
    main()
