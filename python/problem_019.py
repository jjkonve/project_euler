import datetime


def count_sundays_on_first_of_month(start_date, end_date):
    sundays = 0
    i_date = start_date
    while i_date < end_date:
        if i_date.day == 1 and i_date.weekday() == 6:
            sundays += 1
        i_date += datetime.timedelta(days=1)
    return sundays


def test_count_sundays_on_first_of_month():
    assert count_sundays_on_first_of_month(datetime.date(2019, 11, 15), datetime.date(2019, 12, 15)) == 1


print(count_sundays_on_first_of_month(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31)))
