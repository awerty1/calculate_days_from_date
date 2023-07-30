import unittest

from datetime import date, timedelta

from main import count_days, add_days


class TestCountDays(unittest.TestCase):
    def test_count_days(self):
        start_date = "2023-07-01"
        expected_result = 29  # Replace with the expected result
        actual_result = count_days(start_date)
        self.assertEqual(actual_result, expected_result)

    def test_count_days_invalid_format(self):
        start_date = "2023/07/01"  # Invalid format
        expected_result = None
        actual_result = count_days(start_date)
        self.assertEqual(actual_result, expected_result)


class TestAddDays(unittest.TestCase):
    def test_add_days(self):
        # Test adding positive number of days
        start_date = "2023-07-30"
        num_days = 90
        expected_result = (date.fromisoformat(start_date) + timedelta(days=num_days)).isoformat()
        self.assertEqual(add_days(start_date, num_days), expected_result)

        # Test adding negative number of days
        start_date = "2023-07-30"
        num_days = -30
        expected_result = (date.fromisoformat(start_date) + timedelta(days=num_days)).isoformat()
        self.assertEqual(add_days(start_date, num_days), expected_result)

        # Test adding zero days
        start_date = "2023-07-30"
        num_days = 0
        expected_result = (date.fromisoformat(start_date) + timedelta(days=num_days)).isoformat()
        self.assertEqual(add_days(start_date, num_days), expected_result)

        # Test invalid start date format
        start_date = "2023/07/30"
        num_days = 90
        self.assertIsNone(add_days(start_date, num_days))

        # Test result exceeding maximum or minimum date value
        start_date = "9999-12-31"
        num_days = 1
        self.assertIsNone(add_days(start_date, num_days))


if __name__ == '__main__':
    unittest.main()
