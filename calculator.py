import re

def calculate_string(s: str) -> int:
    if s == "":
        return 0

    if s.startswith("//"):
        delimiter_line, s = s.split("\n", 1)

        match = re.match(r"//\[(.*)]", delimiter_line)
        if match:
            delimiters = re.findall(r"\[(.*?)]", delimiter_line)
            delimiters.sort(key=len, reverse=True)
        else:
            delimiters = delimiter_line[2:]
    else:
        delimiters = ","

    numbers_string = s.replace("\n", ',')

    for delimiter in delimiters:
        numbers_string = numbers_string.replace(delimiter, ",")

    numbers = list(map(int, numbers_string.split(",")))

    negative_numbers = [num for num in numbers if num < 0]
    if negative_numbers:
        raise ValueError("Negative numbers are not allowed.")

    numbers = [num for num in numbers if num <= 1000]

    return sum(numbers)