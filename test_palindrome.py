import unittest

from palindrome import find_max_palindrome, is_palindrome, prepare_string


class TestFindMaxPalindrome(unittest.TestCase):
    def test_find_max_palindrome(self):
        data = [
            ('1', '1'),
            ('банан', 'ана'),
            ('', None),
            ('abcba', 'bcb'),
            ('lallal', 'alla'),
            ('KaLam,mAlAk', 'alammala'),
            ('Лёша на полке клопа нашёл', 'ёшанаполкеклопанашё'),
            ('8899889988', '89988998'),
        ]
        for input_string, expected_data in data:
            with self.subTest(input_string=input_string):
                self.assertEqual(find_max_palindrome(input_string), expected_data)

    def test_is_palindrome(self):
        data = [
            ('', False),
            ('a', True),
            ('банан', False),
            ('abcba', True),
            ('lallal', True),
            ('8899889988', True),
        ]
        for input_string, expected_data in data:
            with self.subTest(input_string=input_string):
                self.assertEqual(is_palindrome(input_string), expected_data)

    def test_prepare_string(self):
        data = [
            ('Aaa', 'aaa'),
            ('a,cbvd', 'acbvd'),
            ('банан  SDASD;asdasd!!!', 'бананsdasdasdasd'),
        ]
        for input_string, expected_data in data:
            with self.subTest(input_string=input_string):
                self.assertEqual(prepare_string(input_string), expected_data)


if __name__ == '__main__':
    unittest.main()
