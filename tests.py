import unittest
import random
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_endian_null(self):
        self.assertEqual("00", conv_endian(0, "big"))


def hexify(num, endian_type):
    if endian_type == 0:
        clean_string = parse_hex_big_endian(num)
    elif endian_type == 1:
        clean_string = parse_hex_little_endian(num)
    else:
        return None

    return clean_string


# CITATION: See Google Dictionary, Works Cited at end
def parse_hex_big_endian(num):
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

    result = clean_string
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

    # Set the string to the reversed string
    clean_string = bit_string

    return clean_string


# CITATION: See OSU Course Contributors, Helmsworth, Works Cited at end
# CITATION: See Stevenson-Molnar, Works Cited at end
def build_test(test_func, number):
    def test(self):
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
    # CITATION: See Python Docs Contributors, Works Cited at end
    # Generate a number of tests equal to the range set below
    for x in range(10000):
        # CITATION: See ReadTheDocs Python Reference
        # Contributors, Works Cited at end -2147483648
        num = random.randrange(-2147483648, 2147483648)
        print("Number for test{} was {}".format(x, num))
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