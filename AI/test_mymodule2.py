import unittest

from mymodule2 import add


class TestAdd(unittest.TestCase):
    def test1(self):
        # test when 2 and 4 are given as input the output is 6.
        self.assertEqual(add(2, 4), 6)
        # test when 0 and 0 are given as input the output is 0.
        self.assertEqual(add(0, 0), 0)
        # test when 2.3 and 3.6 are given as input the output is 5.9.
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertNotEqual(add(-2, -2), 0)


unittest.main()
