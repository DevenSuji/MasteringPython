import unittest
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'this is a test of a script that capitalizes each word'
        result = cap.cap_text(text)
        self.assertEqual(
            result, 'This Is A Test Of A Script That Capitalizes Each Word')


if __name__ == '__main__':
    unittest.main()
