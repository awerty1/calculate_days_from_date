from colorama import Fore, Style

""" File for functions with MSGs frm main.py """

#TODO add tests

class MessageFormatter:
    def __init__(self):
        # Constants for formatting
        self.sep_gl = "="
        self.sep_m = "-"
        self.newline = "\n"
        self.sep_count_gl = 68
        self.sep_count_m = 48
        # Set up hash symbols
        self.mult_hash = 23
        self.mult = 2

    def create_hash_symbols(self, title):
        """Generates all hash symbols for formatting with dynamic length"""
        title_length = len(title) + self.mult
        style_br_fore_wt = Style.BRIGHT + Fore.WHITE + "#"
        return {
            'console': {
                'top': style_br_fore_wt * self.mult_hash + Style.RESET_ALL,
                'title': style_br_fore_wt * title_length + Style.RESET_ALL,
                'bottom': style_br_fore_wt * (self.mult_hash * self.mult)
                          + ("#" * title_length) + Style.RESET_ALL
            },
            'file': {
                'top': "#" * self.mult_hash,
                'title': "#" * title_length,
                'bottom': "#" * (self.mult_hash * self.mult) + ("#" * title_length)
            }
        }

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
        return "Do you want to input manually (M) or from a file (F)? (or 'Q' to quit): "

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

    def event_datails_file(self, num_day, start_date_str, result_date, days_passed):
        """Event details 4 file"""
        return (
            f"You selected {num_day} days from the date {start_date_str}{self.newline}"
            f"Next payment date {result_date}, {days_passed} days have passed!{self.newline}"
        )

    def payment_reminder(self, new_line = None):
        """Payment reminder"""
        dont_forget_msg = f"Don't forget to pay, otherwise you'll become poorer"
        if new_line == '\n':
            return dont_forget_msg + f"{self.newline}"
        return dont_forget_msg

    def event_footer(self, hash_symbol_bot):
        """Event Footer"""
        return f"{hash_symbol_bot}{self.newline}"

    def days_remaining_soon(self, result_date, days_remaining):
        """Message when 0-5 days remain"""
        msg = (
            f"Until the date {Fore.RED}{result_date}{Fore.RESET} "
            f"left {Fore.RED}{days_remaining}{Fore.RESET} days!!!"
        )
        file_msg = f"Until the date {result_date} left {days_remaining} days!!!"
        return msg, file_msg

    def days_passed(self, result_date, days_passed):
        """Message when the date has already passed"""
        msg = (
            f"After the date {Fore.RED}{result_date}{Fore.RESET} "
            f"has passed {Fore.RED}{abs(days_passed)}{Fore.RESET} days!!!"
        )
        file_msg = f"After the date {result_date} has passed {abs(days_passed)} days!!!"
        return msg, file_msg

    def days_remaining_long(self):
        """Message when more than 5 days remain"""
        msg = "More than 5 days left before the date"
        file_msg = msg  # 4 file same msg
        return msg, file_msg

    def days_remaining_error(self, days_remaining):
        """Error message in calculations"""
        msg = f"{Fore.RED}Error, days_remaining: {Fore.BLUE}{days_remaining}{Fore.RESET}"
        file_msg = f"Error, days_remaining: {days_remaining}"
        return msg, file_msg

    # OLD VERSION OF event_description
    # def event_description(self, description):
    #     """Format event description"""
    #     return f"{Fore.YELLOW}Description: {Fore.RESET}{description}"

    # NEW VERSION OF event_description
    def event_description(self, description):
        """Format event description with proper sentence splitting and indentation"""
        if not description:
            return f"{Fore.YELLOW}Description: NONE{Fore.RESET}"

        # Split sentences while preserving original dots
        sentences = []
        current_sentence = []
        for i, char in enumerate(description):
            current_sentence.append(char)
            # Check for sentence end (dot followed by space or end of string)
            if char == '.' and (i == len(description) - 1 or description[i + 1] == ' '):
                sentences.append(''.join(current_sentence).strip())
                current_sentence = []

        # Add any remaining text as last sentence
        if current_sentence:
            sentences.append(''.join(current_sentence).strip())

        # Format with indentation
        if not sentences:
            return f"{Fore.YELLOW}Description: NONE{Fore.RESET}"

        # First line
        formatted_description = f"{Fore.YELLOW}Description: {Fore.RESET}{sentences[0]}"

        # Subsequent lines with indentation
        indent = " " * (len("Description: "))
        for sentence in sentences[1:]:
            formatted_description += f"\n{indent}{sentence}"

        return formatted_description
