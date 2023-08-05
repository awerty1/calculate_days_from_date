import unittest

from datetime import date, timedelta

from main import count_days, add_days


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
        self.assertEqual(add_days(start_dates, [num_days_list]), [expected_result])  # Wrap num_days_list and expected_result in lists

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
        self.assertIsNone(add_days(start_dates, num_days_list))

    def test_exceeding_date_value(self):
        # Test result exceeding maximum or minimum date value
        start_dates = "9999-12-31"
        num_days_list = 1
        self.assertIsNone(add_days(start_dates, num_days_list))


if __name__ == '__main__':
    unittest.main()
