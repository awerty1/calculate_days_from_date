from datetime import date, timedelta

from colorama import Fore


def count_days(start_date):
    today = date.today()

    try:
        start_date = date.fromisoformat(start_date)
    except ValueError:
        print(f"{Fore.RED}Invalid start date format. Please provide a date in the format 'YYYY-MM-DD'{Fore.RESET}")
        return None

    delta = today - start_date
    return delta.days


def add_days(start_date, days_to_add):
    try:
        # Converting a date string into a date object
        start_date = date.fromisoformat(start_date)
    except ValueError:
        print(f"{Fore.RED}Invalid start date format. Please provide a date in the format 'YYYY-MM-DD'{Fore.RESET}")
        return None

    try:
        # Adding the specified number of days to the initial date
        new_date = start_date + timedelta(days=days_to_add)
    except OverflowError:
        print(f"{Fore.RED}The result exceeds the maximum or minimum date value that can be represented{Fore.RESET}")
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
            print(f"Next payment date {Fore.RED}{result_date}{Fore.RESET}, "
                  f"{Fore.RED}{days_passed}{Fore.RESET} days have passed!")
            print(f"Don't forget to pay, otherwise you'll become poorer")



