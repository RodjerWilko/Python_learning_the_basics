import unittest

from bowling import Bowling


class ScoreTest(unittest.TestCase):

    def test_wrong_throws(self):
        with self.assertRaises(Exception) as exc:
            bowling = Bowling('1')
            # TODO Если не используете result,
            #  не нужно создавать переменную, можно просто вызвать функцию.
            result = bowling.get_score()
        expected_msg = 'Некорректное число бросков'
        self.assertEqual(exc.exception.args[0], expected_msg)

    def test_less_ten_frames(self):
        with self.assertRaises(Exception) as exc:
            bowling = Bowling('12-536')
            result = bowling.get_score()
        expected_msg = 'Сыграно меньше 10 фреймов'
        self.assertEqual(exc.exception.args[0], expected_msg)

    def test_more_ten_in_frame_or_not_spare(self):
        with self.assertRaises(Exception) as exc:
            bowling = Bowling('1165')
            result = bowling.get_score()
        expected_msg = 'Больше 10 в одном фрейме или не указан Spare'
        self.assertEqual(exc.exception.args[0], expected_msg)

    def test_spare_only_second(self):
        with self.assertRaises(Exception) as exc:
            bowling = Bowling('25/-')
            result = bowling.get_score()
        expected_msg = 'Спэир может быть только вторым броском'
        self.assertEqual(exc.exception.args[0], expected_msg)

    def strike_only_first(self):
        with self.assertRaises(Exception) as exc:
            bowling = Bowling('12-X')
            result = bowling.get_score()
        expected_msg = 'Страйк может быть только первым броском'
        self.assertEqual(exc.exception.args[0], expected_msg)

    def test_only_strike(self):
        b = Bowling('XXXXXXXXXX')
        result = b.get_score()
        self.assertEqual(result, 200)

    def test_only_digits(self):
        b = Bowling('34126316123413145254')
        result = b.get_score()
        self.assertEqual(result, 61)

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

# TODO Исправьте ошибки оформления.
