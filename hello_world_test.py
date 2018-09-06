import unittest
from hello_world import *


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_input_number(self):
        self.assertRaises(Exception, input_number, "two")
    def test_yes(self):
        self.assertRaises(Exception, input_number, "Yes")
    def test___(self):
        self.assertRaises(Exception, input_number, "__")
    def test_right(self):
        self.assertEqual(input_number(2), 2)