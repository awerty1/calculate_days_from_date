def input_start_date():
    start_date_input = input("Enter a list of start dates (YYYY-MM-DD), separated by a comma(,): ")
    start_dates = [date.strip() for date in start_date_input.split(",")]
    return start_dates


def input_num_days():
    num_days_input = input("Enter a list of numbers of days, separated by a comma(,): ")
    num_days = [int(days.strip()) for days in num_days_input.split(",")]
    return num_days


def input_titles():
    titles_input = input("Enter a list of titles, separated by a comma(,): ")
    titles = [title.strip() for title in titles_input.split(",")]
    return titles


def input_manual():
    start_dates = input_start_date()
    num_days = input_num_days()
    titles = input_titles()
    return start_dates, num_days, titles

