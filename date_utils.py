from datetime import date, timedelta

from colorama import Fore


def validate_date(date_str):
    try:
        # Converting a date string into a date object
        return date.fromisoformat(date_str)
    except ValueError:
        print(f"{Fore.RED}Invalid date format: {Fore.BLUE}{date_str}{Fore.RED}.{Fore.RESET} "
              f"{Fore.RED}Please provide a date in the format '{Fore.BLUE}YYYY-MM-DD{Fore.RED}'{Fore.RESET}")
        return None


def count_days(start_date_str):
    today = date.today()
    start_date = validate_date(start_date_str)

    if not start_date:
        return None

    delta = today - start_date
    return delta.days


def add_days(start_dates, days_to_add):
    result_dates = []
    for start_date_str, num_days in zip(start_dates, days_to_add):
        start_date = validate_date(start_date_str)

        if not start_date:
            return None

        try:
            # Adding the specified number of days to the initial date
            new_date = start_date + timedelta(days=num_days)
            result_dates.append(new_date.isoformat())
        except OverflowError:
            print(f"{Fore.RED}The result exceeds the maximum or minimum date value that can be represented "
                  f"{Fore.BLUE}{start_date}{Fore.RESET}")
            return None

    # Converting the new date to a string and returning the result
    return result_dates
