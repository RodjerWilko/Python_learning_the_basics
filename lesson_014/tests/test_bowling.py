import unittest
from bowling import get_score


class ScoreTest(unittest.TestCase):

    def test_only_strike(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_only_spare(self):
        result = get_score('1/1/1/1/1/1/1/1/1/1/')
        self.assertEqual(result, 150)

    def test_only_digits(self):
        result = get_score('34127316123413145254')
        self.assertEqual(result, 62)

    def test_only_zero(self):
        result = get_score('-11--55----1-2-3-4-5')
        self.assertEqual(result, 27)

    def test_all(self):
        result = get_score('X-2344/4/--12X231-')
        self.assertEqual(result, 88)


if __name__ == '__main__':
    unittest.main()
