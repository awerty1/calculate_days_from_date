from datetime import datetime

from colorama import Fore


def input_start_date():
    start_date_input = input(f"Enter a list of start dates {Fore.GREEN}(YYYY-MM-DD){Fore.RESET}, "
                             f"separated by a comma{Fore.GREEN}(,){Fore.RESET} "
                             f"(or '{Fore.RED}Q{Fore.RESET}' to quit): ")

    # Check for exit
    if start_date_input.upper() == 'Q':
        return None

    start_dates = [date.strip() for date in start_date_input.split(",")]

    # Validate input
    valid_dates = []
    for date in start_dates:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            valid_dates.append(date)
        except ValueError:
            print(f"{Fore.RED}Invalid date format: {Fore.BLUE}{date}{Fore.RESET}. "
                  f"Please enter dates in the correct format {Fore.BLUE}(YYYY-MM-DD){Fore.RESET}.")
            return input_start_date()  # Recursively call the function to prompt for valid input

    return start_dates


def input_num_days():
    num_days_input = input(f"Enter a list of numbers of days, separated by a comma{Fore.GREEN}(,){Fore.RESET} "
                           f"(or '{Fore.RED}Q{Fore.RESET}' to quit): ")

    # Check for exit
    if num_days_input.upper() == 'Q':
        return None

    try:
        num_days = [int(days.strip()) for days in num_days_input.split(",")]
    except ValueError as ex:
        print(f"{Fore.RED}Invalid input format: {Fore.BLUE}{ex}{Fore.RESET}. Please enter numbers only.{Fore.RESET}")
        return input_num_days()  # Recursively call the function to prompt for valid input

    return num_days


def input_titles():
    titles_input = input(f"Enter a list of titles, separated by a comma(,) (or '{Fore.RED}Q{Fore.RESET}' to quit): ")

    # Check for exit
    if titles_input.upper() == 'Q':
        return None

    titles = [title.strip() for title in titles_input.split(",")]

    # Validate input
    if all(titles):
        return titles
    else:
        print(f"{Fore.RED}Invalid input: {Fore.BLUE}{titles}{Fore.RESET}{Fore.RED}. "
              f"Please enter non-empty titles.{Fore.RESET}")
        return input_titles()  # Recursively call the function to prompt for valid input


def input_manual():
    print(f"{Fore.YELLOW}Enter 'Q' at any time to quit.{Fore.RESET}")

    start_dates = input_start_date()
    if start_dates is None:
        return None, None, None, None

    num_days = input_num_days()
    if num_days is None:
        return None, None, None, None

    titles = input_titles()
    if titles is None:
        return None, None, None, None

    descriptions = input_descriptions()
    if descriptions is None:
        return None, None, None, None

    # Validate input lengths
    if len(start_dates) == len(num_days) == len(titles) == len(descriptions):
        return start_dates, num_days, titles, descriptions
    else:
        print(
            f"{Fore.RED}Invalid input, length of start_dates:{Fore.RESET}{Fore.BLUE}{len(start_dates)}{Fore.RESET}"
            f"{Fore.RED}, num_days:{Fore.RESET}{Fore.BLUE}{len(num_days)}{Fore.RESET}"
            f"{Fore.RED}, titles:{Fore.RESET}{Fore.BLUE}{len(titles)}{Fore.RESET}"
            f"{Fore.RED}, descriptions:{Fore.RESET}{Fore.BLUE}{len(descriptions)}{Fore.RESET}"
            f"{Fore.RED}. Number of elements in each list must be equal.{Fore.RESET}")
        return input_manual()  # Recursively call the function to prompt for valid input


def input_descriptions():
    descriptions_input = input(f"Enter a list of descriptions, separated by a comma(,) "
                               f"(or '{Fore.RED}Q{Fore.RESET}' to quit): ")

    # Check for exit
    if descriptions_input.upper() == 'Q':
        return None

    descriptions = [desc.strip() for desc in descriptions_input.split(",")]
    return descriptions
