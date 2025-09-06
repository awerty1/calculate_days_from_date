from colorama import init, Fore, Style
init(autoreset=True)

import date_utils
import file_utils
import date_calculation
import date_calculation_example
from input_utils import input_manual
from messages import MessageFormatter


def main():
    # Initialize the msg formatter
    msg = MessageFormatter()

    # Check if the user wants to input manually or from a file
    input_choice = ""
    while input_choice.upper() not in ["M", "F", "Q"]:
        print(msg.manual_input_warning())
        input_choice = input(msg.mode_selection_prompt())

    # Check for quit
    if input_choice.upper() == "Q":
        print(f"{Fore.YELLOW}Exiting program...{Fore.RESET}")
        return

    if input_choice.upper() == "M":
        print(msg.manual_mode_notice())
        start_dates, num_days_list, titles, descriptions = input_manual()

        # Check for quit
        if start_dates is None:
            print(f"{Fore.YELLOW}Exiting program...{Fore.RESET}")
            return

    elif input_choice.upper() == "F":
        # 4 github
        start_dates = date_calculation_example.start_dates
        num_days_list = date_calculation_example.num_days_list
        titles = date_calculation_example.titles
        descriptions = date_calculation_example.descriptions

        # You can delete this code
        # start_dates = date_calculation.start_dates
        # num_days_list = date_calculation.num_days_list
        # titles = date_calculation.titles
        # descriptions = date_calculation.descriptions
    else:
        print(msg.invalid_input(input_choice))
        return

    # Create the output filename
    output_filename = file_utils.create_output_filename()

    # Open the file for writing
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        result_dates = date_utils.add_days(start_dates, num_days_list)

        if result_dates is not None:
            for start_date_str, result_date, num_day, title, description in zip(
                    start_dates, result_dates, num_days_list, titles, descriptions):

                days_passed = date_utils.count_days(start_date_str)
                days_remaining = num_day - days_passed
                hash_symbols = msg.create_hash_symbols(title)

                if days_passed is not None:
                    print(msg.event_header(title, hash_symbols['console']['top']))
                    print(msg.event_description(description))  # new output 4 description
                    print(msg.event_details(num_day, start_date_str, result_date, days_passed))

                    # Write to file
                    output_file.write(f"\n{hash_symbols['file']['top']} {title} {hash_symbols['file']['top']}\n")
                    output_file.write(f"Description: {description}\n")  # description to file
                    output_file.write(msg.event_datails_file(num_day, start_date_str, result_date, days_passed))

                    if days_remaining is not None and 0 <= days_remaining <= 5:
                        console_msg, file_msg = msg.days_remaining_soon(result_date, days_remaining)
                    elif days_remaining is not None and days_remaining < 0:
                        console_msg, file_msg = msg.days_passed(result_date, days_remaining)
                    elif days_remaining is None:
                        console_msg, file_msg = msg.days_remaining_error(days_remaining)
                    else:
                        console_msg, file_msg = msg.days_remaining_long()

                    print(console_msg)
                    output_file.write(f"{file_msg}\n")

                    print(msg.payment_reminder())
                    print(msg.event_footer(hash_symbols['console']['bottom']))
                    output_file.write(msg.payment_reminder("\n"))
                    output_file.write(f"{hash_symbols['file']['bottom']}\n")


if __name__ == '__main__':
    main()
    input(f"Press {Fore.GREEN}\"Enter\"{Fore.RESET} for exit...")
