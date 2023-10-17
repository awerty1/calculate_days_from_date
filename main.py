from colorama import Fore, Style

import date_utils
import date_calculation
import date_calculation_example


if __name__ == '__main__':
    # 4 github
    start_dates = date_calculation_example.start_dates
    num_days_list = date_calculation_example.num_days_list
    titles = date_calculation_example.titles

    # start_dates = date_calculation.start_dates
    # num_days_list = date_calculation.num_days_list
    # titles = date_calculation.titles

    # 4 hash
    mult = 2
    mult_hash = 22
    hash_symbol_top = Style.BRIGHT + Fore.WHITE + "#" * mult_hash + Style.RESET_ALL

    # You can use it to the console
    # start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    # num_days = int(input("Enter the number of days: "))

    result_dates = date_utils.add_days(start_dates, num_days_list)
    if result_dates is not None:
        for start_date_str, result_date, num_day, title in zip(start_dates, result_dates, num_days_list, titles):
            days_passed = date_utils.count_days(start_date_str)
            days_remaining = num_day - days_passed
            # algorithm for count #
            length = len(title)+2
            hash_symbol_title = Style.BRIGHT + Fore.WHITE + "#" * length + Style.RESET_ALL
            hash_symbol_bot = Style.BRIGHT + Fore.WHITE + "#" * (mult_hash * mult) + hash_symbol_title + Style.RESET_ALL

            if days_passed is not None:
                print(f"\n{hash_symbol_top} {title} {hash_symbol_top}")
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
