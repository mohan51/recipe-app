from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):

    def test_add_two_numbers(self):
        res = calc.add(5, 6)


        self.assertEqual(res, 11)