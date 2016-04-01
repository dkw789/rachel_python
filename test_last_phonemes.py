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

    def test_single_line(self):

        phoneme_list = [ 'EH1', 'N', 'D', 'Z']


        actual = poetry_functions.last_phonemes(phoneme_list)
        expected = ['EH1', 'N', 'D', 'Z']
        self.assertEqual(actual, expected)




    def test_multiple_words(self):

        phoneme_list = ['DH', 'AH0',
                        'F', 'ER1', 'S', 'T',
                        'L', 'AY1', 'N',
                        'L', 'IY1', 'D', 'Z',
                        'AO1', 'F',
                        'W', 'IH1', 'DH',
                        'AH0',
                        'G', 'AE1', 'P',
                        'B', 'IH0', 'F', 'AO1', 'R',
                        'N', 'EH1', 'K', 'S', 'T']

        actual = poetry_functions.last_phonemes(phoneme_list)
        expected = ['EH1', 'K', 'S', 'T']
        self.assertEqual(actual, expected)





    def test_consecutive_phonemes(self):

        phoneme_list = ['DH', 'AH0',
                        'F', 'ER1', 'S', 'T',
                        'L', 'AY1', 'N',
                        'L', 'IY1', 'D', 'Z',
                        'AO1', 'F',
                        'W', 'IH1', 'DH',
                        'AH0',
                        'G', 'AE1', 'P',
                        'B', 'IH0', 'F', 'AO1', 'R',
                        'N', 'EH1', 'K', 'S', 'T',
                        'DH', 'EH1', 'N',
                        'P', 'OW1', 'AH0', 'M']

        actual = poetry_functions.last_phonemes(phoneme_list)
        expected = ['AH0', 'M']
        self.assertEqual(actual, expected)



# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
