from app import Split
import unittest


class TestSplit(unittest.TestCase):

    def test_split_case_1(self):
        app = Split('', '')
        app._data = '11  gg wp gl hf 24!../ ='
        app._transform()
        self.assertEqual(app._data, '1-1-g-g-w-p-g-l-h-f-2-4-!-.-.-/-=')

    def test_split_case_2(self):
        app = Split('', '')
        app._data = ''
        app._transform()
        self.assertEqual(app._data, '')

    def test_split_case_3(self):
        app = Split('', '')
        app._data = 'Hello World!'
        app._transform()
        self.assertEqual(app._data, 'H-e-l-l-o-W-o-r-l-d-!')
