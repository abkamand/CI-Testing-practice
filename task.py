ALL_DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
UPPER_CASE_HEX_ALPHAS = ['A', 'B', 'C', 'D', 'E', 'F']
LOWER_CASE_HEX_ALPHAS = ['a', 'b', 'c', 'd', 'e', 'f']


def is_hex(num_str):
    if num_str[0:2].lower() == '0x':
        return True
    else:
        return False


def is_float(num_str):
    for char in num_str:
        if char == '.':
            return True
    return False


def process_int(num_str):
    number = 0
    place = 1

    for char in reversed(num_str):
        # Check for non-numeric character
        if char not in ALL_DIGITS:
            return None
        digit = ord(char) - 48
        number += digit * place
        place *= 10

    return number


def process_float(num_str):
    num_str = num_str.split('.')

    # Check for multiple decimal points
    if len(num_str) > 2:
        return None

    before_decimal = num_str[0]
    after_decimal = num_str[1]

    number = 0.
    place = 1

    for char in reversed(before_decimal):
        # Check for non-numeric character
        if char not in ALL_DIGITS:
            return None

        digit = ord(char) - 48
        number += digit * place
        place *= 10

    place = .1
    for char in after_decimal:
        # Check for non-numeric character
        if char not in ALL_DIGITS:
            return None

        digit = ord(char) - 48
        number += digit * place
        place *= .1

    return number


def process_hex(num_str):
    number = 0
    place = 1
    for char in reversed(num_str):
        if char in ALL_DIGITS:
            digit = ord(char) - 48
        elif char in UPPER_CASE_HEX_ALPHAS:
            digit = ord(char) - 55
        elif char in LOWER_CASE_HEX_ALPHAS:
            digit = - 87
        else:
            return None

        number += digit * place
        place *= 16

    return number


def conv_num(num_str):
    positive = True
    number = None

    # Confirm input is string
    if not isinstance(num_str, str):
        return None

    # Check for an empty string
    if num_str == '':
        return None

    # Determine Positive or Negative, if negative strip off minus sign
    if num_str[0] == '-':
        positive = False
        num_str = num_str[1:]

    # Determine num_type, if hex strip off 0x
    if is_hex(num_str):
        num_type = 'HEX'
        num_str = num_str[2:]
    elif is_float(num_str):
        num_type = 'FLOAT'
    else:
        num_type = 'INT'

    # process number based on type
    if num_type == 'INT':
        number = process_int(num_str)
    elif num_type == 'FLOAT':
        number = process_float(num_str)
    elif num_type == 'HEX':
        number = process_hex(num_str)

    if positive:
        return number
    else:
        return -number
