from django.test import TestCase

from .calc import add


class CalcTests(TestCase):

    def test_add_number(self):
        """Test that two numbers are added"""
        self.assertEqual(add(3, 9), 11)
