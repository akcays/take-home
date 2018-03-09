import math

NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

DIGITS = {
    10: "ten",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion"
} 

def number_in_english(number):
    """
    number: int
    return: str
    """
    assert type(number) == int

    if number in NUMBERS:
        output = NUMBERS[number]
    elif number < 100:
        number_in_digit = math.floor(number / 10)
        number_left = number % 10
        output = NUMBERS[number_in_digit * 10] + ' ' + number_in_english(number_left)
    else:
        if number < 1000:
            digit = 100
        else:
            digit = 1000
            while digit * 1000 <= number:
                digit *= 1000;

        number_in_digit = math.floor(number / digit)
        number_left = number % digit

        output = number_in_english(number_in_digit) + ' ' + DIGITS[digit]
        rest_of_string = number_in_english(number_left)

        if rest_of_string != "zero":
            output += ' ' + rest_of_string
    
    return output
