import unittest
from calculator import calculate_string

class TestCalculateString(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        # Given
        input_string = ""
        expected_result = 0

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_single_number_returns_value(self):
        # Given
        input_string = "1"
        expected_result = 1

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_two_numbers_comma_delimited_returns_sum(self):
        # Given
        input_string = "22,8"
        expected_result = 30

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_two_numbers_newline_delimited_returns_sum(self):
        # Given
        input_string = "22\n8"
        expected_result = 30

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_three_numbers_delimited_returns_sum(self):
        # Given
        input_string = "21\n8,1"
        expected_result = 30

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_negative_numbers_throw_exception(self):
        # Given
        input_string = "1,-2,3"

        # When/Then:
        with self.assertRaises(ValueError) as context:
            calculate_string(input_string)

        self.assertIn("Negative numbers are not allowed.", str(context.exception))

    def test_numbers_greater_than_1000_are_ignored(self):
        # Given
        input_string = "2,1001,3"
        expected_result = 5

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_custom_delimiter(self):
        # Given
        input_string = "//#\n1#2#3"
        expected_result = 6

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_custom_multichar_delimiter(self):
        # Given
        input_string = "//[###]\n1###2###3"
        expected_result = 6

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

    def test_multiple_custom_delimiters(self):
        # Given
        input_string = "//[#][###]\n1#2###3"
        expected_result = 6

        # When
        result = calculate_string(input_string)

        # Then
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()