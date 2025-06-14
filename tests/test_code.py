import unittest
from unittest.mock import patch

from datetime import date, timedelta

from date_utils import count_days, add_days
from input_utils import input_start_date, input_num_days, input_titles, input_descriptions, input_manual


class TestCountDays(unittest.TestCase):
    def test_count_days(self):
        start_date = "2023-07-01"
        start_date_obj = date.fromisoformat(start_date)
        today = date.today()
        expected_result = (today - start_date_obj).days  # Replace with the expected result
        actual_result = count_days(start_date)
        self.assertEqual(actual_result, expected_result)

    def test_count_days_invalid_format(self):
        start_date = "2023/07/01"  # Invalid format
        expected_result = None
        actual_result = count_days(start_date)
        self.assertEqual(actual_result, expected_result)


class TestAddDays(unittest.TestCase):
    def test_add_positive_days(self):
        # Test adding positive number of days
        start_dates = ["2023-07-30"]  # Wrap start_dates in a list
        num_days_list = 90
        expected_result = (date.fromisoformat(start_dates[0]) + timedelta(days=num_days_list)).isoformat()
        self.assertEqual(add_days(start_dates, [num_days_list]),
                         [expected_result])  # Wrap num_days_list and expected_result in lists

    def test_add_negative_days(self):
        # Test adding negative number of days
        start_dates = ["2023-07-30"]
        num_days_list = -30
        expected_result = (date.fromisoformat(start_dates[0]) + timedelta(days=num_days_list)).isoformat()
        self.assertEqual(add_days(start_dates, [num_days_list]), [expected_result])

    def test_add_zero_days(self):
        # Test adding zero days
        start_dates = ["2023-07-30"]
        num_days_list = 0
        expected_result = (date.fromisoformat(start_dates[0]) + timedelta(days=num_days_list)).isoformat()
        self.assertEqual(add_days(start_dates, [num_days_list]), [expected_result])

    def test_invalid_start_date_format(self):
        # Test invalid start date format
        start_dates = "2023/07/30"
        num_days_list = 90
        self.assertIsNone(add_days(start_dates, [num_days_list]))

    def test_exceeding_date_value(self):
        # Test result exceeding maximum or minimum date value
        start_dates = "9999-12-31"
        num_days_list = 1
        self.assertIsNone(add_days(start_dates, [num_days_list]))


class MainTests(unittest.TestCase):

    # Test for adding several positive days:
    def test_add_multiple_positive_days(self):
        start_dates = ["2023-07-30", "2023-08-15", "2023-09-01"]  # Multiple start dates
        num_days_list = [30, 45, 60]  # Multiple num days
        expected_results = [(date.fromisoformat(start_dates[i]) + timedelta(days=num_days_list[i])).isoformat() for i in
                            range(len(start_dates))]
        self.assertEqual(add_days(start_dates, num_days_list), expected_results)

    # Test for adding negative days to multiple dates:
    def test_add_negative_days_multiple_dates(self):
        start_dates = ["2023-07-30", "2023-08-15", "2023-09-01"]  # Multiple start dates
        num_days_list = [-10, -20, -30]  # Multiple num days
        expected_results = [(date.fromisoformat(start_dates[i]) + timedelta(days=num_days_list[i])).isoformat() for i in
                            range(len(start_dates))]
        self.assertEqual(add_days(start_dates, num_days_list), expected_results)

    # Test for adding days to null dates:
    def test_add_days_to_empty_dates(self):
        start_dates = []  # Empty start dates list
        num_days_list = [10, 20, 30]  # Multiple num days
        expected_results = []  # Expecting an empty list as result
        self.assertEqual(add_days(start_dates, num_days_list), expected_results)


class TestInputFunctions(unittest.TestCase):
    def test_input_start_date(self):
        with patch('builtins.input', return_value='2022-01-01, 2022-02-01, 2022-03-01'):
            start_dates = input_start_date()
            expected_dates = ['2022-01-01', '2022-02-01', '2022-03-01']
            self.assertEqual(start_dates, expected_dates)

    def test_input_num_days(self):
        with patch('builtins.input', return_value='5, 10, 15'):
            num_days = input_num_days()
            expected_days = [5, 10, 15]
            self.assertEqual(num_days, expected_days)

    def test_input_titles(self):
        with patch('builtins.input', return_value='Title 1, Title 2, Title 3'):
            titles = input_titles()
            expected_titles = ['Title 1', 'Title 2', 'Title 3']
            self.assertEqual(titles, expected_titles)

    def test_input_descriptions_valid(self):
        with patch('builtins.input', return_value='Desc 1, Desc 2, Desc 3'):
            descriptions = input_descriptions()
            self.assertEqual(descriptions, ['Desc 1', 'Desc 2', 'Desc 3'])

    def test_input_manual(self):
        with patch('input_utils.input_start_date', return_value=['2022-01-01']):
            with patch('input_utils.input_num_days', return_value=[5]):
                with patch('input_utils.input_titles', return_value=['Title 1']):
                    with patch('input_utils.input_descriptions', return_value=['Test description']):
                        start_dates, num_days, titles, descriptions = input_manual()
                        expected_start_dates = ['2022-01-01']
                        expected_num_days = [5]
                        expected_titles = ['Title 1']
                        expected_description = ['Test description']

                        self.assertEqual(start_dates, expected_start_dates)
                        self.assertEqual(num_days, expected_num_days)
                        self.assertEqual(titles, expected_titles)
                        self.assertEqual(descriptions, expected_description)


if __name__ == '__main__':
    unittest.main()
