import unittest
import random
from task import *


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_endian_null(self):
        self.assertEqual("00", conv_endian(0, "big"))


def hexify(num, endian_type):
    numInHex = hex(num)

    hexString = str(numInHex)

    cleanString = ""

    if endian_type == 0:
        if hexString[0] != "-":

            hexString = hexString[2:len(hexString) + 1]

            while len(hexString) > 0:

                if len(hexString) > 1:
                    curNybble = hexString[
                                len(hexString) - 2:len(hexString) + 1]
                    hexString = hexString[0:len(hexString) - 2]
                    upperFirst = curNybble[0].upper()
                    upperSecond = curNybble[1].upper()
                else:
                    upperFirst = "0"
                    upperSecond = hexString[0].upper()
                    hexString = ""

                cleanString = upperFirst + upperSecond + cleanString

                if len(hexString) > 0:
                    cleanString = " " + cleanString
        else:
            hexString = hexString[3:len(hexString) + 1]

            while len(hexString) > 0:

                if len(hexString) > 1:
                    curNybble = hexString[
                                len(hexString) - 2:len(hexString) + 1]
                    hexString = hexString[0:len(hexString) - 2]
                    upperFirst = curNybble[0].upper()
                    upperSecond = curNybble[1].upper()
                else:
                    upperFirst = "0"
                    upperSecond = hexString[0].upper()
                    hexString = ""

                cleanString = upperFirst + upperSecond + cleanString

                if len(hexString) > 0:
                    cleanString = " " + cleanString

            # Just need to prepend the negative sign now
            cleanString = "-" + cleanString
    elif endian_type == 1:
        if hexString[0] != "-":

            hexString = hexString[2:len(hexString) + 1]

            while len(hexString) > 0:

                if len(hexString) > 1:
                    curNybble = hexString[
                                len(hexString) - 2:len(hexString) + 1]
                    hexString = hexString[0:len(hexString) - 2]
                    upperFirst = curNybble[0].upper()
                    upperSecond = curNybble[1].upper()
                else:
                    upperFirst = "0"
                    upperSecond = hexString[0].upper()
                    hexString = ""

                cleanString = upperFirst + upperSecond + cleanString

                if len(hexString) > 0:
                    cleanString = " " + cleanString
        else:
            hexString = hexString[3:len(hexString) + 1]

            while len(hexString) > 0:

                if len(hexString) > 1:
                    curNybble = hexString[
                                len(hexString) - 2:len(hexString) + 1]
                    hexString = hexString[0:len(hexString) - 2]
                    upperFirst = curNybble[0].upper()
                    upperSecond = curNybble[1].upper()
                else:
                    upperFirst = "0"
                    upperSecond = hexString[0].upper()
                    hexString = ""

                cleanString = upperFirst + upperSecond + cleanString

                if len(hexString) > 0:
                    cleanString = " " + cleanString

            # Just need to prepend the negative sign now
            cleanString = "-" + cleanString

        result = cleanString
        bitString = ""

        if result[0] != "-":

            while len(result) > 0:
                curNybble = result[0:2]
                bitString = curNybble + bitString
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bitString = " " + bitString
        else:
            # Slice off the negative sign
            result = result[1:len(result) + 1]

            while len(result) > 0:
                curNybble = result[0:2]
                bitString = curNybble + bitString
                result = result[3:len(result) + 1]

                if len(result) != 0:
                    bitString = " " + bitString

            # Just need to prepend the negative sign now
            bitString = "-" + bitString

        # Set the string to the reversed string
        cleanString = bitString
    else:
        return None

    return cleanString


# CITATION: See OSU Course Contributors, Helmsworth, Works Cited at end
# CITATION: See Stevenson-Molnar, Works Cited at end
def build_test(test_func, number):
    def test(self):
        # Pick an endian type
        endian_type = random.randrange(0, 3)
        testOutput = hexify(number, endian_type)

        if endian_type == 0:
            endian_type = "big"
        elif endian_type == 1:
            endian_type = "little"
        elif endian_type == 2:
            endian_type = "small"

        # This is the function which will be attached to unittest
        output = test_func(number, endian_type)
        self.assertEqual(output, testOutput,
                         "conv_endian returned {},"
                         " hexify returned {}".format(output, testOutput))
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
