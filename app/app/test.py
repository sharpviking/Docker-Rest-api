"""
sample tests
"""

from django.test import SimpleTestCase


from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(26, 11)

        self.assertEqual(res, 37)

    def test_subtract_numbers(self):

        res = calc.subtract(26, 11)

        self.assertEqual(res, 15)
