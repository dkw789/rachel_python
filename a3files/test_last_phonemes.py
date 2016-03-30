import unittest
import poetry_functions


class TestLastPhonemes(unittest.TestCase):
    def test_last_phonemes_empty(self):
        """ Test last_phonemes on an empty list. """

        actual = poetry_functions.last_phonemes([])
        expected = []
        self.assertEqual(actual, expected, 'empty list')

        # Place your unit test definitions after this line.

    #####################################################################################################################################################

    def test_single_newline(self):
        """Test get_poem_lines with a string that only has a newline character."""
        lst = ['\n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = []
        self.assertEqual(actual, expected)

    def test_all_puncuation_special_character_string(self):
        """Test get_poem_lines with two strings that only contains punctuation and special characters and another that is full of spaces. Both lines end in a newline, as the precondition specifies."""
        lst = ['.........#(*&_$@(*&$)@$\n', '!!!!!???><?><??><#!\n', '     \n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = ['.........#(*&_$@(*&$)@$\n', ], ['!!!!!???><?><??><#!\n', ]
        self.assertEqual(actual, expected)

    def test_single_word_no_newline(self):
        """Test get_poem_lines with a string that only contains a single word and single newline character."""
        lst = ['Hello\n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = 1
        self.assertEqual(actual, expected)

    def test_single_word_single_starting_newline_and_space(self):
        """Test get_poem_lines with a string that only contains a single word with
        a single newline character and space at the beginning and the end."""
        lst = ['\n Hello \n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = 1
        self.assertEqual(actual, expected)

    def test_multiple_words_with_middle_newlines_and_spaces(self):
        """Test get_poem_lines with a single string made of multiple words that contain newline characters and spaces throughout."""
        lst = ['\n\n\n\nHello   \n\n\n my name\n\n\n is bob\n\n\n.\n\n\n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = 1
        self.assertEqual(actual, expected)

    def test_multiple_strings_with_newlines_and_spaces(self):
        """Test get_poem_lines with 5 strings that consist of multiple words and newline characters and spaces throughout. Some strings are composed
        soley of newlines and spaces and punctuation."""
        lst = ['\n\n\n\nHello   \n\n\n my name\n\n\n is bob\n\n\n.\n\n\n', '\n\n\n\n\n\n\n         \n\n\n     \n',
               ' \n', ' I like to build stuff. \n\n\n\n       But I am starting to program now.\n', '!@#$%^&*()\n']
        actual = poetry_functions.get_poem_lines(lst)
        expected = 3
        self.assertEqual(actual, expected)


# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
