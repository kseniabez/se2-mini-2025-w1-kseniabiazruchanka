import pytest
from calculator import calculate_string

def test_empty_string_returns_zero():
    # Given
    input_string = ""
    expected_result = 0

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_single_number_returns_value():
    # Given
    input_string = "1"
    expected_result = 1

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_two_numbers_comma_delimited_returns_sum():
    # Given
    input_string = "22,8"
    expected_result = 30

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_two_numbers_newline_delimited_returns_sum():
    # Given
    input_string = "22\n8"
    expected_result = 30

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_three_numbers_delimited_returns_sum():
    # Given
    input_string = "21\n8,1"
    expected_result = 30

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_negative_numbers_throw_exception():
    # Given
    input_string = "1,-2,3"

    # When/Then
    with pytest.raises(ValueError) as context:
        calculate_string(input_string)

    assert "Negative numbers are not allowed." in str(context.value)

def test_numbers_greater_than_1000_are_ignored():
    # Given
    input_string = "2,1001,3"
    expected_result = 5

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_custom_delimiter():
    # Given
    input_string = "//#\n1#2#3"
    expected_result = 6

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_custom_multichar_delimiter():
    # Given
    input_string = "//[###]\n1###2###3"
    expected_result = 6

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result

def test_multiple_custom_delimiters():
    # Given
    input_string = "//[#][###]\n1#2###3"
    expected_result = 6

    # When
    result = calculate_string(input_string)

    # Then
    assert result == expected_result
