# ------------------------ FUNCTION 1 ---------------------------
ALL_DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
UPPER_CASE_HEX_ALPHAS = ['A', 'B', 'C', 'D', 'E', 'F']
LOWER_CASE_HEX_ALPHAS = ['a', 'b', 'c', 'd', 'e', 'f']


def is_hex(num_str):
    """Takes a string of digits as a parameter. Returns True if the string represents a hex number.
    Returns False otherwise.
    """
    if num_str[0:2].lower() == '0x':
        return True
    else:
        return False


def is_float(num_str):
    """Takes a string of digits as a parameter. Returns True if the string represents a float number.
    Returns False otherwise.
    """
    for char in num_str:
        if char == '.':
            return True
    return False


def process_int(num_str):
    """Takes a string representation of an integer as a parameter. Converts the the string to an int and
    returns the int. If the string contains non-numeric characters the function returns None.
    """
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
    """Takes a string representation of a float as a parameter. Converts the string to
    a float and returns the float. If the string contains multiple decimal points the function
    returns None. If the string contains any non-numeric characters the function returns None.
    """
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

    places = len(after_decimal)
    number = round(number, places)
    return number


def process_hex(num_str):
    """Takes a string representation of a hexadecimal number as a parameter. Converts the string to an integer
    of equal value and returns the integer. If the string contains any non-numeric or non-hex-alpha digits
    the function returns None.
    """
    number = 0
    place = 1
    for char in reversed(num_str):
        if char in ALL_DIGITS:
            digit = ord(char) - 48
        elif char in UPPER_CASE_HEX_ALPHAS:
            digit = ord(char) - 55
        elif char in LOWER_CASE_HEX_ALPHAS:
            digit = ord(char) - 87
        else:
            return None

        number += digit * place
        place *= 16

    return number


def conv_num(num_str):
    """Takes a string representation of a number as a parameter. The number can be either an
    integer, float, or hexadecimal. The function converts the string to an int or float and returns it.
    If the number is an int or hex, the function returns an int. If the number is a float the function returns
    a float.
    """
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

    if number is not None and not positive:
        number = -number

    return number


# ------------------------ FUNCTION 2 ---------------------------
def my_datetime(num_sec):
    # convert seconds to days, 86400 seconds in a day
    days = num_sec // 86400

    # create array that represents the amount of days in a month in a yearly
    # calendar
    days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # initialize leap_year_counter to 2 since we start at 1970
    leap_year_counter = 2
    # initialize normal_year days to 365 and leap_year_days to 366
    normal_year_days = 365
    leap_year_days = 366

    # initialize current_year to 1970, current_month to 1
    current_year = 1970
    current_month = 1

    # convert days to years, update current_year
    while ((leap_year_counter == 4 and days > 366) or
            (leap_year_counter != 4 and days > 365)):
        # if we're in a leap year
        if ((current_year % 4 == 0 and current_year % 100 != 0) or
                (current_year % 400 == 0)):
            days = days - leap_year_days
            leap_year_counter = 1
        # not a leap year
        else:
            days = days - normal_year_days
            leap_year_counter += 1

        current_year += 1

    # if we landed on a leap year, set 2nd element in days_months to 29
    if ((current_year % 4 == 0 and current_year % 100 != 0) or
            (current_year % 400 == 0)):
        days_months[1] = 29

    for month in days_months:
        # break loop if we hit last month
        if days < month:
            break
        else:
            days = days - month
            current_month += 1

    # account for landing on january 1st edge case
    if current_month == 13:
        current_month = 1
        current_year += 1

    # finally, get our current_day
    current_day = days + 1

    # convert our integers into MM-DD-YYYY string format
    string_day = ""
    string_month = ""
    string_year = str(current_year)

    if current_day >= 1 and current_day < 10:
        string_day = "0" + str(current_day)
    else:
        string_day = str(current_day)

    if current_month >= 1 and current_month < 10:
        string_month = "0" + str(current_month)
    else:
        string_month = str(current_month)

    return (string_month + "-" +
            string_day + "-" + string_year)


# ------------------- FUNCTION 3 -----------------------
# CITATION: See PyCharm Contributors, Works Cited at end
def convert_dec_to_bin(number):
    # CITATION: See Brennan, Works Cited at end
    binary_string = ""

    result = number

    if number == 0:
        # If it's zero, we're done.
        binary_string = "0"
    elif number > 0:
        while result != 0:
            # CITATION: See Agrawal (Division Operators...),
            # Works Cited at end
            new_result = result // 2
            remainder = result % 2
            result = new_result
            string_remainder = ""

            if remainder == 0:
                string_remainder = "0"
            else:
                string_remainder = "1"

            # CITATION: See Byers, Works Cited at end
            binary_string = string_remainder + binary_string

        # CITATION: See Wikipedia Contributors, Works Cited at end
        # Pad the nybble if needed
        while len(binary_string) % 4 != 0:
            binary_string = "0" + binary_string

    elif number < 0:

        # Get the positive version
        positive_number = 0 - number
        result = positive_number

        # Do the same calcs as above for the positive version
        while result != 0:
            # CITATION: See Agrawal (Division Operators...),
            # Works Cited at end
            new_result = result // 2
            remainder = result % 2
            result = new_result
            string_remainder = ""

            if remainder == 0:
                string_remainder = "0"
            else:
                string_remainder = "1"

            # CITATION: See Byers, Works Cited at end
            binary_string = string_remainder + binary_string

        # CITATION: See Wikipedia Contributors, Works Cited at end
        # Pad the nybble if needed
        while len(binary_string) % 4 != 0:
            binary_string = "0" + binary_string

        # CITATION: See RapidTables.com Contributors, Works Cited at end
        # Now we just need to prepend the negative sign
        binary_string = "-" + binary_string

    return binary_string


def convert_bin_to_hex(number):
    # CITATION: See Brennan, RapidTables Contributors, Thakur,
    # Works Cited at end

    # CITATION: See Kumar, Mishra (Gullu), Works Cited at end
    bit_dictionary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    bit_string = ""

    result = number

    if number == "0":
        return "00"

    if number[0] != "-":

        first_nybble = True

        while len(result) > 0:
            cur_nybble = result[len(result) - 4:(len(result) + 1)]

            # CITATION: See Wikipedia Contributors, Byers,
            # Mishra (Gullu) Works Cited
            hexadecimal_digit = bit_dictionary.get(cur_nybble)

            # Slice this nybble off the result
            result = result[0:len(result) - 4]

            # CITATION: See PyCharm Contributors, Works Cited at end
            if first_nybble:
                first_nybble = False
                bit_string = hexadecimal_digit + bit_string
            elif not first_nybble and len(result) > 0:
                first_nybble = True
                bit_string = " " + hexadecimal_digit + bit_string
            else:
                bit_string = hexadecimal_digit + bit_string

            if len(result) == 0 and (len(bit_string) % 3) - 2 != 0:
                # We're at the last byte and need to pad
                bit_string = "0" + bit_string

    else:
        bit_string = convert_bin_to_hex_negative(result)

    return bit_string


def convert_bin_to_hex_negative(result):
    # CITATION: See Kumar, Mishra (Gullu), Works Cited at end
    bit_dictionary = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    bit_string = ""

    first_nybble = True
    # Slice off the negative sign
    result = result[1:len(result) + 1]

    while len(result) > 0:
        cur_nybble = result[len(result) - 4:(len(result) + 1)]

        # CITATION: See Wikipedia Contributors, Byers,
        # Mishra (Gullu) Works Cited
        hexadecimal_digit = bit_dictionary.get(cur_nybble)

        # Slice this nybble off the result
        result = result[0:len(result) - 4]

        # CITATION: See PyCharm Contributors, Works Cited at end
        if first_nybble:
            first_nybble = False
            bit_string = hexadecimal_digit + bit_string
        elif not first_nybble and len(result) > 0:
            first_nybble = True
            bit_string = " " + hexadecimal_digit + bit_string
        else:
            bit_string = hexadecimal_digit + bit_string

        if len(result) == 0 and (len(bit_string) % 3) - 2 != 0:
            # theNumber = len(bit_string) % 3 - 2
            # We're at the last byte and need to pad
            bit_string = "0" + bit_string

    # Just need to prepend the negative sign now
    bit_string = "-" + bit_string

    return bit_string


def conv_endian(num, endian="big"):

    num = convert_bin_to_hex(convert_dec_to_bin(num))

    # If it's big, we're done
    if endian == "big":
        return num
    elif endian == "little":
        result = num
        bit_string = ""

        if result[0] != "-":

            while len(result) > 0:
                cur_nybble = result[0:2]
                bit_string = cur_nybble + bit_string
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bit_string = " " + bit_string
        else:
            # Slice off the negative sign
            result = result[1:len(result) + 1]

            while len(result) > 0:
                cur_nybble = result[0:2]
                bit_string = cur_nybble + bit_string
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bit_string = " " + bit_string

            # Just need to prepend the negative sign now
            bit_string = "-" + bit_string

        return bit_string
    else:
        # CITATION: See OSU Course Contributors, Works Cited at end
        # Some invalid endianness was passed
        return None


"""
WORKS CITED

Agrawal, Arpit. "Division Operators in Python." GeeksForGeeks,
https://www.geeksforgeeks.org/division-operator-in-python/.

Brennan, Eugene. "How to Convert Hex to Binary and Binary to Hexadecimal."
 Owlcation.com, https://owlcation.com/stem/
 How-to-Convert-Hex-to-Binary-and-Binary-to-Hexadecimal.

Brennan, Eugene. "How to Convert Decimal to Binary and Binary to Decimal."
 Owlcation.com, https://owlcation.com/stem/
 How-to-Convert-Decimal-to-Binary-and-Binary-to-Decimal.

Byers, Mark <StackOverflow username>. "inserting characters at the start
 and end of a string." StackOverflow,
 https://stackoverflow.com/questions/10059554/
 inserting-characters-at-the-start-and-end-of-a-string.

Mishra (Gullu), Shashank. "Switch Case in Python (Replacement)."
 GeeksForGeeks.com,
 https://www.geeksforgeeks.org/switch-case-in-python-replacement/.

Kumar, Prashant <StackOverflow username>. "What is the Python equivalent
 for a case/switch statement? [duplicate]." StackOverflow.com,
 https://stackoverflow.com/questions/11479816/
 what-is-the-python-equivalent-for-a-case-switch-statement.

OSU Course Contributors. "Group Project: Part 2." Canvas,
 https://oregonstate.instructure.com/courses/1810943/
 assignments/8334612?module_item_id=20728375.

PyCharm Contributors. "Show quick fixes." PyCharm Software Feature,
https://www.jetbrains.com/pycharm/.

RapidTables.com Contributors. "Decimal to Binary converter."
 RapidTables.com,
 https://www.rapidtables.com/convert/number/decimal-to-binary.html.

RapidTables.com Contributors. "How to convert binary to hex."
 Rapidtables.com,
 https://www.rapidtables.com/convert/number/how-binary-to-hex.html.

Shah, Nirmi. "What does the if __name__ == “__main__”: do?"
 GeeksForGeeks.com,
 https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/.

Thakur, Arjun. "How to Convert Binary to Hexadecimal?" TutorialsPoint.com,
https://www.tutorialspoint.com/how-to-convert-binary-to-hexadecimal.

Wikipedia Contributors. "Nibble." En.Wikipedia.org,
https://en.wikipedia.org/wiki/Nibble.

Wikipedia Contributors. "Hexadecimal." Simple.Wikipedia.org,
https://simple.wikipedia.org/wiki/Hexadecimal

"""
