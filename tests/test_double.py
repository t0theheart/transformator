from app import Double
import unittest


class TestDouble(unittest.TestCase):

    def test_double_case_1(self):
        app = Double('', '')
        app._data = '11  gg wp gl hf 24!../ ='
        app._transform()
        self.assertEqual(app._data, '1111  gggg wwpp ggll hhff 2244!!....// ==')

    def test_double_case_2(self):
        app = Double('', '')
        app._data = ''
        app._transform()
        self.assertEqual(app._data, '')

    def test_double_case_3(self):
        app = Double('', '')
        app._data = 'Hello World!'
        app._transform()
        self.assertEqual(app._data, 'HHeelllloo WWoorrlldd!!')
