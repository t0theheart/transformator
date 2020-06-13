from app import SumAscii
import unittest


class TestSumAscii(unittest.TestCase):

    def test_sum_ascii_case_1(self):
        app = SumAscii('', '')
        app._data = '11  gg wp gl hf 24!../ ='
        app._transform()
        self.assertEqual(app._data, '1511')

    def test_sum_ascii_case_2(self):
        app = SumAscii('', '')
        app._data = ''
        app._transform()
        self.assertEqual(app._data, '0')

    def test_sum_ascii_case_3(self):
        app = SumAscii('', '')
        app._data = 'Hello World!'
        app._transform()
        self.assertEqual(app._data, '1085')
