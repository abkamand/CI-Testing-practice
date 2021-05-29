import random
import unittest
import datetime
from task import my_datetime
from task import conv_endian
from task import conv_num


# CITATION: Refactoring and other IDE features
# provided by PyCharm Contributors. Linting assessments provided by
# Bryukhanov (PEP8Online.com) Works Cited at end
class TestCase(unittest.TestCase):
    """This class is used to run unit tests on task.py"""

    def test1(self):
        """This is the base test, used to validate test suite is working."""
        self.assertTrue(True)

    # ------------------------ Function 1 Tests
    # -----Integer Tests-----
    def test1_func1(self):
        self.assertEqual(1, conv_num('1'))

    def test2_func1(self):
        self.assertEqual(-1, conv_num('-1'))

    def test3_func1(self):
        self.assertEqual(0, conv_num('0'))

    def test4_func1(self):
        self.assertEqual(None, conv_num('A55'))

    def test5_func1(self):
        self.assertEqual(None, conv_num('5A5'))

    def test6_func1(self):
        self.assertEqual(None, conv_num('55A'))

    def test7_func1(self):
        self.assertEqual(None, conv_num('Z55'))

    def test8_func1(self):
        self.assertEqual(None, conv_num('5Z5'))

    def test9_func1(self):
        self.assertEqual(None, conv_num('55Z'))

    def test10_func1(self):
        self.assertEqual(None, conv_num('!55'))

    def test11_func1(self):
        self.assertEqual(None, conv_num('5!5'))

    def test12_func1(self):
        self.assertEqual(None, conv_num('55!'))

    def test13_func1(self):
        self.assertEqual(55, conv_num('055'))

    def test14_func1(self):
        self.assertEqual(505, conv_num('505'))

    def test15_func1(self):
        self.assertEqual(550, conv_num('550'))

    def test16_func1(self):
        self.assertEqual(None, conv_num('-A55'))

    def test17_func1(self):
        self.assertEqual(None, conv_num('-5A5'))

    def test18_func1(self):
        self.assertEqual(None, conv_num('-55A'))

    def test19_func1(self):
        self.assertEqual(None, conv_num('-Z55'))

    def test20_func1(self):
        self.assertEqual(None, conv_num('-5Z5'))

    def test21_func1(self):
        self.assertEqual(None, conv_num('-55Z'))

    def test22_func1(self):
        self.assertEqual(None, conv_num('-!55'))

    def test23_func1(self):
        self.assertEqual(None, conv_num('-5!5'))

    def test24_func1(self):
        self.assertEqual(None, conv_num('-55!'))

    def test25_func1(self):
        self.assertEqual(-55, conv_num('-055'))

    def test26_func1(self):
        self.assertEqual(-505, conv_num('-505'))

    def test27_func1(self):
        self.assertEqual(-550, conv_num('-550'))

    # -----Float Tests-----

    def test28_func1(self):
        self.assertEqual(5.5, conv_num('5.5'))

    def test29_func1(self):
        self.assertEqual(-5.5, conv_num('-5.5'))

    def test30_func1(self):
        self.assertEqual(0.0, conv_num('0.0'))

    def test31_func1(self):
        self.assertEqual(0.0, conv_num('0.'))

    def test32_func1(self):
        self.assertEqual(None, conv_num('.5.'))

    def test33_func1(self):
        self.assertEqual(None, conv_num('.5.5'))

    def test34_func1(self):
        self.assertEqual(None, conv_num('.5.5.'))

    def test35_func1(self):
        self.assertEqual(None, conv_num('5.5.'))

    def test36_func1(self):
        self.assertEqual(None, conv_num('5.5.'))

    def test37_func1(self):
        self.assertEqual(None, conv_num('5.5.5'))

    def test38_func1(self):
        self.assertEqual(None, conv_num('A5.55'))

    def test39_func1(self):
        self.assertEqual(None, conv_num('5A5.5'))

    def test40_func1(self):
        self.assertEqual(None, conv_num('55.5A'))

    def test41_func1(self):
        self.assertEqual(None, conv_num('Z55.5'))

    def test42_func1(self):
        self.assertEqual(None, conv_num('5Z5.5'))

    def test43_func1(self):
        self.assertEqual(None, conv_num('55.5Z'))

    def test44_func1(self):
        self.assertEqual(None, conv_num('!55.5'))

    def test45_func1(self):
        self.assertEqual(None, conv_num('55.5!'))

    def test46_func1(self):
        self.assertEqual(None, conv_num('55.!5'))

    def test47_func1(self):
        self.assertEqual(None, conv_num('-.5.'))

    def test48_func1(self):
        self.assertEqual(None, conv_num('-.5.5'))

    def test49_func1(self):
        self.assertEqual(None, conv_num('-.5.5.'))

    def test50_func1(self):
        self.assertEqual(None, conv_num('-5.5.'))

    def test51_func1(self):
        self.assertEqual(None, conv_num('-5.5.'))

    def test52_func1(self):
        self.assertEqual(None, conv_num('-5.5.5'))

    def test53_func1(self):
        self.assertEqual(None, conv_num('-A5.55'))

    def test54_func1(self):
        self.assertEqual(None, conv_num('-5A5.5'))

    def test55_func1(self):
        self.assertEqual(None, conv_num('-55.5A'))

    def test56_func1(self):
        self.assertEqual(None, conv_num('-Z55.5'))

    def test57_func1(self):
        self.assertEqual(None, conv_num('-5Z5.5'))

    def test58_func1(self):
        self.assertEqual(None, conv_num('-55.5Z'))

    def test59_func1(self):
        self.assertEqual(None, conv_num('-!55.5'))

    def test60_func1(self):
        self.assertEqual(None, conv_num('-55.5!'))

    def test61_func1(self):
        self.assertEqual(None, conv_num('-55.!5'))

    def test62_func1(self):
        self.assertEqual(0.55, conv_num('0.55'))

    def test63_func1(self):
        self.assertEqual(0.55, conv_num('0000.55'))

    def test64_func1(self):
        self.assertEqual(0.55, conv_num('0000.550000'))

    def test65_func1(self):
        self.assertEqual(0.55, conv_num('.550000'))

    def test66_func1(self):
        self.assertEqual(0.55, conv_num('.550'))

    # -----Hex Tests-----
    def test67_func1(self):
        self.assertEqual(int("0xAD4", 16), conv_num('0xad4'))

    def test68_func1(self):
        self.assertEqual(int("-0xAD4", 16), conv_num('-0xad4'))

    def test69_func1(self):
        self.assertEqual(int("0xAD4", 16), conv_num('0XAD4'))

    def test70_func1(self):
        self.assertEqual(int("-0xAD4", 16), conv_num('-0XAD4'))

    def test71_func1(self):
        self.assertEqual(None, conv_num('0XAZ4'))

    def test72_func1(self):
        self.assertEqual(None, conv_num('0XAz4'))

    def test73_func1(self):
        self.assertEqual(None, conv_num('0XA.4'))

    def test74_func1(self):
        self.assertEqual(None, conv_num('0XA.4.4'))

    def test75_func1(self):
        self.assertEqual(None, conv_num('0XA.4!4'))

    def test76_func1(self):
        self.assertEqual(None, conv_num('-0XAZ4'))

    def test77_func1(self):
        self.assertEqual(None, conv_num('-0XAz4'))

    def test78_func1(self):
        self.assertEqual(None, conv_num('-0XA.4'))

    def test79_func1(self):
        self.assertEqual(None, conv_num('-0XA.4.4'))

    def test80_func1(self):
        self.assertEqual(None, conv_num('-0XA.4!4'))

    def test81_func1(self):
        self.assertEqual(int("0x0AD4", 16), conv_num('0x0AD4'))

    def test82_func1(self):
        self.assertEqual(int("0xAD40", 16), conv_num('0xAD40'))

    # non-string input
    def test83_func1(self):
        self.assertEqual(None, conv_num(123))

    # empty string
    def test84_func1(self):
        self.assertEqual(None, conv_num(""))

    # ------------------------ Function 2 Tests
    def test_rand_func2(self):
        """Test function that generates 100000 random timestamps to run through
        comparison calculator helper function to test function2"""
        for i in range(0, 100000):
            num = random.randint(0, 32535143990)
            func2_comp(num)

    # ------------------------ Function 3 Tests
    def test_endian_null(self):
        """Testing that conv_endian handles 0 correctly."""
        self.assertEqual("00", conv_endian(0, "big"))


# ------------------------ Function 1 Random Testing
def create_int_str(str_len):
    int_str = ''

    pos_neg = random.randint(0, 1)
    if pos_neg == 1:
        int_str += '-'

    for i in range(str_len):
        int_str += str(random.randint(0, 9))

    return int_str


def create_float_str(str_len):
    float_str = ''
    decimal_place = random.randint(0, str_len)

    pos_neg = random.randint(0, 1)
    if pos_neg == 1:
        float_str += '-'

    for i in range(decimal_place):
        float_str += str(random.randint(0, 9))

    float_str += '.'

    for i in range(str_len - decimal_place):
        float_str += str(random.randint(0, 9))

    return float_str


def create_hex_str(str_len):
    POSSIBLE_DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                       'A', 'B', 'C', 'D', 'E',
                       'F', 'a', 'b', 'c', 'd', 'e', 'f']
    hex_str = ''

    pos_neg = random.randint(0, 1)
    if pos_neg == 1:
        hex_str += '-'

    upper_lower = random.randint(0, 1)
    if upper_lower == 0:
        hex_str += '0x'
    else:
        hex_str += '0X'

    for i in range(str_len):
        random_digit = random.randint(0, 21)
        hex_str += POSSIBLE_DIGITS[random_digit]

    return hex_str


def build_conv_num_test(expected, test_case):
    def test(self):
        result = conv_num(test_case)
        places = str(expected)[::-1].find('.')
        if places == -1:
            places = 4

        self.assertAlmostEqual(expected, result, places)
    return test


def generate_conv_num_testcases():
    for i in range(10000):
        num_type = random.randint(0, 2)

        if num_type == 0:
            num_type = 'INT'
        elif num_type == 1:
            num_type = 'FLOAT'
        else:
            num_type = 'HEX'

        strlen = random.randint(1, 10)

        if num_type == 'INT':
            num_str = create_int_str(strlen)
            expected = int(num_str)
            new_test = build_conv_num_test(expected, num_str)
        elif num_type == 'FLOAT':
            num_str = create_float_str(strlen)
            expected = float(num_str)
            new_test = build_conv_num_test(expected, num_str)
        else:
            num_str = create_hex_str(strlen)
            expected = int(num_str, 16)
            new_test = build_conv_num_test(expected, num_str)

        setattr(TestCase, 'test_{}'.format(num_str), new_test)


# ------------------------ Function 2 Random Testing Helper Functions
def refrm(s):
    """convert datetime output to match my_datetime format"""
    s2 = s[5:10] + s[4] + s[0:4]
    return s2


def func2_comp(num):
    """compare passed random num between my_datetime and python's built in
    datetime, if they differ, output an error found message"""
    if (my_datetime(num) != refrm
       (str(datetime.datetime.utcfromtimestamp(num)))):
        print("My: ", my_datetime(num), " != ", refrm(
            str(datetime.datetime.utcfromtimestamp(num))))
        print("Error Found: timestamp == {}".format(num))


# ------------------------ Function 3 Random Testing
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
def build_endian_test(test_func, number):
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
        test = build_endian_test(conv_endian, num)
        # CITATION: See OSU Course Contributors, Works Cited
        setattr(TestCase, "test_endian_{}".format(x), test)


# CITATION: See Shah, Works Cited at end
# CITATION: See Python Docs Contributors, Works Cited at end
if __name__ == '__main__':
    # Seed the random
    random.seed()
    generate_conv_num_testcases()
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
