from colorama import Fore, Style

import date_utils
import file_utils
import date_calculation
import date_calculation_example
from input_utils import input_manual


def main():
    # Check if the user wants to input manually or from a file
    input_choice = ""
    while input_choice.upper() not in ["M", "F"]:
        input_choice = input("Do you want to input manually (M) or from a file (F)? ")

    if input_choice.upper() == "M":
        start_dates, num_days_list, titles = input_manual()
    elif input_choice.upper() == "F":
        # 4 github
        start_dates = date_calculation_example.start_dates
        num_days_list = date_calculation_example.num_days_list
        titles = date_calculation_example.titles

        # start_dates = date_calculation.start_dates
        # num_days_list = date_calculation.num_days_list
        # titles = date_calculation.titles
    else:
        print("Invalid input choice. Exiting.")
        exit()

    # Set up hash symbols
    mult = 2
    mult_hash = 22
    hash_symbol_top = Style.BRIGHT + Fore.WHITE + "#" * mult_hash + Style.RESET_ALL
    hash_symbol_top_to_file = "#" * mult_hash

    # Create the output filename
    output_filename = file_utils.create_output_filename()

    # Open the file for writing
    with open(output_filename, 'w') as output_file:

        result_dates = date_utils.add_days(start_dates, num_days_list)
        if result_dates is not None:
            for start_date_str, result_date, num_day, title in zip(start_dates, result_dates, num_days_list, titles):
                days_passed = date_utils.count_days(start_date_str)
                days_remaining = num_day - days_passed
                # algorithm for count #
                length = len(title) + 2
                hash_symbol_title = Style.BRIGHT + Fore.WHITE + "#" * length + Style.RESET_ALL
                hash_symbol_bot = Style.BRIGHT + Fore.WHITE + "#" * (
                            mult_hash * mult) + hash_symbol_title + Style.RESET_ALL
                # for save to file
                hash_symbol_title_to_file = "#" * length
                hash_symbol_bot_to_file = "#" * (mult_hash * mult) + hash_symbol_title_to_file

                if days_passed is not None:
                    print(f"\n{hash_symbol_top} {title} {hash_symbol_top}")
                    print(f"You selected {Fore.RED}{num_day}{Fore.RESET} "
                          f"days from the date {Fore.GREEN}{start_date_str}{Fore.RESET}")
                    print(f"Next payment date {Fore.RED}{result_date}{Fore.RESET} , "
                          f"{Fore.RED}{days_passed}{Fore.RESET} days have passed!")
                    # Write to file
                    output_file.write(f"\n{hash_symbol_top_to_file} {title} {hash_symbol_top_to_file}\n")
                    output_file.write(f"You selected {num_day} days from the date {start_date_str}\n")
                    output_file.write(f"Next payment date {result_date}, {days_passed} days have passed!\n")
                    if days_remaining is not None and 0 <= days_remaining <= 5:
                        print(f"Until the date {Fore.RED}{result_date}{Fore.RESET} "
                              f"left {Fore.RED}{days_remaining}{Fore.RESET} days!!!")
                        output_file.write(f"Until the date {result_date} left {days_remaining} days!!!\n")
                    elif days_remaining is not None and days_remaining < 0:
                        print(f"After the date {Fore.RED}{result_date}{Fore.RESET} "
                              f"has passed {Fore.RED}{abs(days_remaining)}{Fore.RESET} days!!!")
                        output_file.write(f"After the date {result_date} has passed {abs(days_remaining)} days!!!\n")
                    elif days_remaining is None:
                        print(f"{Fore.RED}Error, days_remaining: {days_remaining}{Fore.RESET}")
                        output_file.write(f"Error, days_remaining: {days_remaining}\n")
                    else:
                        print(f"More than 5 days left before the date")
                        output_file.write(f"More than 5 days left before the date\n")
                    print(f"Don't forget to pay, otherwise you'll become poorer")
                    print(f"{hash_symbol_bot}\n")
                    output_file.write("Don't forget to pay, otherwise you'll become poorer\n")
                    output_file.write(f"{hash_symbol_bot_to_file}\n")


if __name__ == '__main__':
    main()
