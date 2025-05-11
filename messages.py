from colorama import Fore, Style

""" File for functions with MSGs frm main.py """

# sep_gl = "="
# sep_m = "-"
# newline = "\n"
# sep_count_gl = 68
# sep_count_m = 48
#
# def get_manual_input_warning():
#     return (
#         f"{Fore.YELLOW}{newline}{sep_gl * sep_count_gl}{newline}"
#         f" IMPORTANT: Manual input data WILL NOT be saved to the source file!{newline}"
#         f" Data will only be written to a separate report file.{newline}"
#         f"{sep_gl * sep_count_gl}{newline}{Style.RESET_ALL}"
#     )
#
# def get_manual_mode_notice():
#     return (
#         f"{Fore.YELLOW}{newline}{sep_m * sep_count_m}{newline}"
#         f" Notice: Manual input mode selected.{newline}"
#         f" Results will only be saved to the report file.{newline}"
#         f" For permanent data storage, use file mode (F).{newline}"
#         f"{sep_m * sep_count_m}{newline}{Style.RESET_ALL}"
#     )
#TODO add tests

class MessageFormatter:
    def __init__(self):
        # Constants for formatting
        self.sep_gl = "="
        self.sep_m = "-"
        self.newline = "\n"
        self.sep_count_gl = 68
        self.sep_count_m = 48

    def manual_input_warning(self):
        """Warning about manual data entry"""
        return (
            f"{Fore.YELLOW}{self.newline}{self.sep_gl * self.sep_count_gl}{self.newline}"
            f" IMPORTANT: Manual input data WILL NOT be saved to the source file!{self.newline}"
            f" Data will only be written to a separate report file.{self.newline}"
            f"{self.sep_gl * self.sep_count_gl}{self.newline}{Style.RESET_ALL}"
        )

    def manual_mode_notice(self):
        """Manual mode selection notification"""
        return (
            f"{Fore.YELLOW}{self.newline}{self.sep_m * self.sep_count_m}{self.newline}"
            f" Notice: Manual input mode selected.{self.newline}"
            f" Results will only be saved to the report file.{self.newline}"
            f" For permanent data storage, use file mode (F).{self.newline}"
            f"{self.sep_m * self.sep_count_m}{self.newline}{Style.RESET_ALL}"
        )

    def invalid_input(self, input_choice):
        """Message about incorrect input"""
        return f"{Fore.RED}Invalid input choice({input_choice}). Please enter M or F.{Style.RESET_ALL}"

    def mode_selection_prompt(self):
        """Mode selection message"""
        return "Do you want to input manually (M) or from a file (F)? "

    def event_header(self, title, hash_symbol_top):
        """Event Title"""
        return f"\n{hash_symbol_top} {title} {hash_symbol_top}"

    def event_details(self, num_day, start_date_str, result_date, days_passed):
        """Event details"""
        return (
            f"You selected {Fore.RED}{num_day}{Fore.RESET} "
            f"days from the date {Fore.GREEN}{start_date_str}{Fore.RESET}{self.newline}"
            f"Next payment date {Fore.RED}{result_date}{Fore.RESET} , "
            f"{Fore.RED}{days_passed}{Fore.RESET} days have passed!"
        )

    def payment_reminder(self):
        """Payment reminder"""
        return "Don't forget to pay, otherwise you'll become poorer"

    def event_footer(self, hash_symbol_bot):
        """Event Footer"""
        return f"{hash_symbol_bot}{self.newline}"