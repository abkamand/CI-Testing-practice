import random
import unittest
import datetime
from task import my_datetime


def refrm(s):
    """convert datetime output to match my_datetime format"""
    s2 = s[5:10] + s[4] + s[0:4]
    return s2


def test_func(num):
    if (my_datetime(num) != refrm
       (str(datetime.datetime.utcfromtimestamp(num)))):
        print("My: ", my_datetime(num), " != ", refrm(
            str(datetime.datetime.utcfromtimestamp(num))))
        print("Error Found: timestamp == {}".format(num))


class TestCase(unittest.TestCase):
    def test1(self):
        for i in range(0, 100000):
            num = random.randint(0, 32535143990)
            test_func(num)


if __name__ == '__main__':
    unittest.main()
