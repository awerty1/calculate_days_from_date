from datetime import date, timedelta

from colorama import Fore, Style


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
    for start_date_str in start_dates:
        start_date = validate_date(start_date_str)

        if not start_date:
            return None

        for num_days in days_to_add:
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


if __name__ == '__main__':
    # Set your start date in YYYY, MM, DD format
    start_dates = ["2023-07-30", "2023-07-09", "2023-07-20"]
    # Number of days to calculate from the current date
    # num_days = 90
    # List with multiple values
    num_days_list = [88, 88, 15]
    titles = ["phone 1", "phone 2", "court"]
    mult = 2
    mult_hash = 22
    hash_symbol_top = Style.BRIGHT + Fore.WHITE + "#" * mult_hash + Style.RESET_ALL

    # You can use it to the console
    # start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    # num_days = int(input("Enter the number of days: "))

    result_dates = add_days(start_dates, num_days_list)
    if result_dates is not None:
        for start_date_str, result_date, num_day, title in zip(start_dates, result_dates, num_days_list, titles):
            days_passed = count_days(start_date_str)
            days_remaining = num_day - days_passed
            # algorithm for count #
            length = len(title)+2
            hash_symbol_title = Style.BRIGHT + Fore.WHITE + "#" * length + Style.RESET_ALL
            hash_symbol_bot = Style.BRIGHT + Fore.WHITE + "#" * (mult_hash * mult) + hash_symbol_title + Style.RESET_ALL

            if days_passed is not None:
                print(f"{hash_symbol_top} {title} {hash_symbol_top}")
                print(f"You have chosen a date: {Fore.GREEN}{start_date_str}{Fore.RESET}")
                print(f"Next payment date {Fore.RED}{result_date}{Fore.RESET} , "
                      f"{Fore.RED}{days_passed}{Fore.RESET} days have passed!")
                if days_remaining is not None and 0 <= days_remaining <= 5:
                    print(f"Until the date {Fore.RED}{result_date}{Fore.RESET} "
                          f"left {Fore.RED}{days_remaining}{Fore.RESET} days!!!")
                elif days_remaining is not None and days_remaining < 0:
                    print(f"After the date {Fore.RED}{result_date}{Fore.RESET} "
                          f"has passed {Fore.RED}{abs(days_remaining)}{Fore.RESET} days!!!")
                elif days_remaining is None:
                    print(f"{Fore.RED}Error, days_remaining: {days_remaining}{Fore.RESET}")
                else:
                    print(f"More than 5 days left before the date")
                print(f"Don't forget to pay, otherwise you'll become poorer")
                print(f"{hash_symbol_bot}\n")
