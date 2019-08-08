# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
from datetime import datetime, timedelta

from dateutil import parser


def get_yesterday():
    yesterday = datetime.now() - timedelta(days=1)
    return f'Yesterday: {yesterday}'


def get_today():
    today = datetime.now()
    return f'Today: {today}'


def get_last_month():
    month_with_31_day = [1, 3, 5, 7, 8, 10, 12]
    month_with_30_day = [4, 6, 9, 11]
    if datetime.today().month in month_with_31_day:
        days_in_month = 31
    elif datetime.today().month in month_with_30_day:
        days_in_month = 30
    else:
        days_in_month = 28
    last_month = datetime.now() - timedelta(days=days_in_month)
    return f'Last month:{last_month}'


def change_string_to_date(string_line):
    a = parser.parse(string_line)
    return type(a)


def main():
    print(get_today())
    print(get_yesterday())
    print(get_last_month())
    print(change_string_to_date('01/01/17 12:10:03.234567'))


if __name__ == '__main__':
    main()
