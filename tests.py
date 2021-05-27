import random
import unittest
import datetime
from task import my_datetime
from task import conv_endian


def refrm(s):
    """convert datetime output to match my_datetime format"""
    s2 = s[5:10] + s[4] + s[0:4]
    return s2


def func2_comp(num):
    if (my_datetime(num) != refrm
       (str(datetime.datetime.utcfromtimestamp(num)))):
        print("My: ", my_datetime(num), " != ", refrm(
            str(datetime.datetime.utcfromtimestamp(num))))
        print("Error Found: timestamp == {}".format(num))


# CITATION: Refactoring and other IDE features
# provided by PyCharm Contributors. Linting assessments provided by
# Bryukhanov (PEP8Online.com) Works Cited at end
class TestCase(unittest.TestCase):
    """This class is used to run unit tests on task.py"""

    def test1(self):
        """This is the base test, used to validate test suite is working."""
        self.assertTrue(True)

    # random testing function 2
    def func2_random_test(self):
        for i in range(0, 100000):
            num = random.randint(0, 32535143990)
            func2_comp(num)

    def test_endian_null(self):
        """Testing that conv_endian handles 0 correctly."""
        self.assertEqual("00", conv_endian(0, "big"))


def hexify(num, endian_type):
    """Converts a number in hex to a string"""
    if endian_type == 0:
        clean_string = parse_hex_big_endian(num)
    elif endian_type == 1:
        clean_string = parse_hex_little_endian(num)
    else:
        return None

    return clean_string


# CITATION: See Google Dictionary, Works Cited at end
def parse_hex_big_endian(num):
    """Parses a hex value into a string, using big-endian byte order"""
    num_in_hex = hex(num)

    hex_string = str(num_in_hex)

    clean_string = ""

    if hex_string[0] != "-":

        hex_string = hex_string[2:len(hex_string) + 1]

        while len(hex_string) > 0:

            if len(hex_string) > 1:
                cur_nybble = hex_string[
                            len(hex_string) - 2:len(hex_string) + 1]
                hex_string = hex_string[0:len(hex_string) - 2]
                upper_first = cur_nybble[0].upper()
                upper_second = cur_nybble[1].upper()
            else:
                upper_first = "0"
                upper_second = hex_string[0].upper()
                hex_string = ""

            clean_string = upper_first + upper_second + clean_string

            if len(hex_string) > 0:
                clean_string = " " + clean_string
    else:
        hex_string = hex_string[3:len(hex_string) + 1]

        while len(hex_string) > 0:

            if len(hex_string) > 1:
                cur_nybble = hex_string[
                            len(hex_string) - 2:len(hex_string) + 1]
                hex_string = hex_string[0:len(hex_string) - 2]
                upper_first = cur_nybble[0].upper()
                upper_second = cur_nybble[1].upper()
            else:
                upper_first = "0"
                upper_second = hex_string[0].upper()
                hex_string = ""

            clean_string = upper_first + upper_second + clean_string

            if len(hex_string) > 0:
                clean_string = " " + clean_string

        # Just need to prepend the negative sign now
        clean_string = "-" + clean_string

    return clean_string


# CITATION: See Google Dictionary, Works Cited at end
def parse_hex_little_endian(num):
    """Parses a hex value into a string, using little-endian byte order"""
    num_in_hex = hex(num)

    hex_string = str(num_in_hex)

    clean_string = ""

    if hex_string[0] != "-":
        clean_string = parse_hex_little_endian_positive(hex_string)
    else:
        clean_string = parse_hex_little_endian_negative(hex_string)

    result = clean_string
    bit_string = ""

    if result[0] != "-":
        bit_string = reverse_byte_order_positive(result)
    else:
        bit_string = reverse_byte_order_negative(result)
    # Set the string to the reversed string
    clean_string = bit_string

    return clean_string


def parse_hex_little_endian_positive(hex_string):
    """Parses a hex string of a positive number into a string in
    little-endian byte order"""
    hex_string = hex_string[2:len(hex_string) + 1]
    clean_string = ""

    while len(hex_string) > 0:

        if len(hex_string) > 1:
            cur_nybble = hex_string[
                         len(hex_string) - 2:len(hex_string) + 1]
            hex_string = hex_string[0:len(hex_string) - 2]
            upper_first = cur_nybble[0].upper()
            upper_second = cur_nybble[1].upper()
        else:
            upper_first = "0"
            upper_second = hex_string[0].upper()
            hex_string = ""

        clean_string = upper_first + upper_second + clean_string

        if len(hex_string) > 0:
            clean_string = " " + clean_string
    return clean_string


def parse_hex_little_endian_negative(hex_string):
    """Parses a hex string of a negative number into a string in
        little-endian byte order"""
    hex_string = hex_string[3:len(hex_string) + 1]
    clean_string = ""
    while len(hex_string) > 0:

        if len(hex_string) > 1:
            cur_nybble = hex_string[
                         len(hex_string) - 2:len(hex_string) + 1]
            hex_string = hex_string[0:len(hex_string) - 2]
            upper_first = cur_nybble[0].upper()
            upper_second = cur_nybble[1].upper()
        else:
            upper_first = "0"
            upper_second = hex_string[0].upper()
            hex_string = ""

        clean_string = upper_first + upper_second + clean_string

        if len(hex_string) > 0:
            clean_string = " " + clean_string

    # Just need to prepend the negative sign now
    clean_string = "-" + clean_string
    return clean_string


def reverse_byte_order_positive(result):
    """Reverses the byte order of a positive hex string."""
    bit_string = ""
    while len(result) > 0:
        cur_nybble = result[0:2]
        bit_string = cur_nybble + bit_string
        result = result[3:len(result) + 1]

        if len(result) != 0:
            bit_string = " " + bit_string

    return bit_string


def reverse_byte_order_negative(result):
    """Reverses the byte order of a negative hex string."""
    bit_string = ""

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


# CITATION: See OSU Course Contributors, Helmsworth, Works Cited at end
# CITATION: See Stevenson-Molnar, Works Cited at end
def build_test(test_func, number):
    """Builds tests for random testing."""
    def test(self):
        """This is the function that will be returned by
        the test builder function"""
        # Pick an endian type
        endian_type = random.randrange(0, 3)
        test_output = hexify(number, endian_type)

        if endian_type == 0:
            endian_type = "big"
        elif endian_type == 1:
            endian_type = "little"
        elif endian_type == 2:
            endian_type = "small"

        # This is the function which will be attached to unittest
        output = test_func(number, endian_type)
        self.assertEqual(output, test_output,
                         "conv_endian returned {},"
                         " hexify returned {}".format(output, test_output))
    return test


def generate_endian_tests(self):
    """Generates a series of random tests for function3"""
    # CITATION: See Python Docs Contributors, Works Cited at end
    # Generate a number of tests equal to the range set below
    for x in range(10000):
        # CITATION: See ReadTheDocs Python Reference
        # Contributors, Works Cited at end -2147483648
        num = random.randrange(-2147483648, 2147483648)
        # print("Number for test{} was {}".format(x, num))
        test = build_test(conv_endian, num)
        # CITATION: See OSU Course Contributors, Works Cited
        setattr(self, "test_endian_{}".format(x), test)


# CITATION: See Shah, Works Cited at end
# CITATION: See Python Docs Contributors, Works Cited at end
if __name__ == '__main__':
    # Seed the random
    random.seed()
    generate_endian_tests(TestCase)
    unittest.main()

"""
WORKS CITED
Bryukhanov, Valentin. "PEP8 Online." Pep8Online.com,
http://pep8online.com/.

Helmsworth, Andrew (self). "random_cc." Github.com,
https://github.com/andershelmsworth/random_cc.

OSU Course Contributors. "Exploration: Dynamically Adding Tests." Canvas,
https://oregonstate.instructure.com/courses/1810943/pages/
exploration-dynamically-adding-tests?module_item_id=20728351.

OSU Course Contributors. "Exploration: Random Testing." Canvas,
https://oregonstate.instructure.com/courses/1810943/pages/
exploration-random-testing?module_item_id=20728349.

OSU Course Contributors. "HW3: Random Testing Hands On." Canvas,
https://oregonstate.instructure.com/courses/1810943/
assignments/8334620?module_item_id=20728353.

Python Documentation Contributors.
"random — Generate pseudo-random numbers."
Python.org, https://docs.python.org/3/library/random.html.

ReadTheDocs Python Reference Contributors. "int." ReadTheDocs.io,
https://python-reference.readthedocs.io/en/latest/docs/ints/.

Shah, Nirmi. "What does the if __name__ == “__main__”: do?" GeeksForGeeks,
https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
"""
