import unittest
from hello_world import *


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_input_number(self):
        self.assertEqual(input_number('two'), 11)
