from datetime import date, timedelta

from colorama import Fore


def validate_date(date_str):
    try:
        # Converting a date string into a date object
        return date.fromisoformat(date_str)
    except ValueError:
        print(f"{Fore.RED}Invalid date format: {Fore.BLUE}{date_str}{Fore.RESET}. "
              f"{Fore.RED}Please provide a date in the format '{Fore.BLUE}YYYY-MM-DD{Fore.RED}'{Fore.RESET}")
        return None


def count_days(start_date_str):
    today = date.today()
    start_date = validate_date(start_date_str)

    if not start_date:
        return None

    delta = today - start_date
    return delta.days


def add_days(start_date_str, days_to_add):
    start_date = validate_date(start_date_str)

    if not start_date:
        return None

    try:
        # Adding the specified number of days to the initial date
        new_date = start_date + timedelta(days=days_to_add)
    except OverflowError:
        print(f"{Fore.RED}The result exceeds the maximum or minimum date value that can be represented "
              f"{Fore.BLUE}{start_date}{Fore.RESET}")
        return None

    # Converting the new date to a string and returning the result
    return new_date.isoformat()


if __name__ == '__main__':
    # Set your start date in YYYY, MM, DD format
    start_date_str = "2023-07-30"
    # Number of days to calculate from the current date
    num_days = 90

    # You can use it to the console
    # start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    # num_days = int(input("Enter the number of days: "))

    result_date = add_days(start_date_str, num_days)
    if result_date is not None:
        days_passed = count_days(start_date_str)
        if days_passed is not None:
            print(f"You have chosen a date: {Fore.GREEN}{start_date_str}{Fore.RESET}")
            print(f"Next payment date {Fore.RED}{result_date}{Fore.RESET}, "
                  f"{Fore.RED}{days_passed}{Fore.RESET} days have passed!")
            print(f"Don't forget to pay, otherwise you'll become poorer")
