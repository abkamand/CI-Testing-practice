def conv_num(num_str):

    ALL_DIGITS = ['1','2','3','4','5','6','7','8','9','0']
    UPPER_CASE_HEX_ALPHAS = ['A','B','C','D','E','F']
    LOWER_CASE_HEX_ALPHAS = ['a','b','c','d','e','f']

    num_type = None
    positive = True
    number = None

    # Confirm input is string
    if not isinstance(num_str, str):
        return None

    # Check for empty string
    if num_str == '':
        return None

    # Determine Positive or Negative, if negative strip off minus sign
    if num_str[0] == '-':
        positive = False
        num_str = num_str[1:]

    # Determine if Hex, if hex strip off 0x
    if num_str[0:2].lower() == '0x':
        num_type = 'HEX'
        num_str = num_str[2:]
    else:
        # Determine if Float
        for char in num_str:
            if char == '.':
                num_type = 'FLOAT'

    # Otherwise its an Int
    if num_type is None:
        num_type = 'INT'

    # Processing for INT
    if num_type == 'INT':
        number = 0
        place = 1
        for char in reversed(num_str):
            # Check for non-numeric character
            if char not in ALL_DIGITS:
                return None

            digit = ord(char) - 48
            number += digit * place
            place *= 10

    # Processing for FLOAT
    if num_type == 'FLOAT':
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

    # Processing for HEX
    if num_type == 'HEX':
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

    if positive:
        return number
    else:
        return -number



