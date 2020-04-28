import unittest
from bowling import Bowling


class ScoreTest(unittest.TestCase):

    def test_only_strike(self):
        b = Bowling('XXXXXXXXXX')
        result = b.get_score()
        self.assertEqual(result, 200)

    def test_only_spare(self):
        b = Bowling('1/1/1/1/1/1/1/1/1/1/')
        result = b.get_score()
        self.assertEqual(result, 150)

    def test_only_digits(self):
        b = Bowling('34127316123413145254')
        result = b.get_score()
        self.assertEqual(result, 62)

    def test_only_zero(self):
        b = Bowling('-11--55----1-2-3-4-5')
        result = b.get_score()
        self.assertEqual(result, 27)

    def test_all(self):
        b = Bowling('X-2344/4/--12X231-')
        result = b.get_score()
        self.assertEqual(result, 88)


if __name__ == '__main__':
    unittest.main()
