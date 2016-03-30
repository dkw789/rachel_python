import unittest
import poetry_functions

SMALL_PRONOUNCING_LIST = [
    'HOW  HH AW1',
    'NOW N AW1',
    'BROWN  B R AW1 N',
    'COW C AW1',
    'CHOWDER  CH AW1 D ER0',
    'SHOW  SH OW1',
    'TOWN T AW1 N',
    'TOUT T AW1 T',
    'THEMISTOCLES DH EH1 M AH0 S T OW1 K L IY0 Z',
    'THERMOPYLAE TH ER2 M AA1 P IH1 L AY1',
    'THE  DH AH0',
    'PELOPONESSIAN  P EH1 L OW1 P OW1  N IY2 ZH EH1 N',
    'WAR W AO1 R',
    'X IH0 K S',
    'SQUARED S K W EH1 R D',
    'Y W AY1',
    'WHY W AY1',
    'H2SO4 EY1 CH T UW1 EH2 S OW1 F AO1 R',
    'SOFTWOOD S AO1 F T W UH2 D',
    'ORBER AO1 R B ER0',
    'COOPERATIVE  K OW0 AA1 P ER0 EY2 T IH0 V',
    'ACCELERATING AE0 K S EH1 L ER0 EY2 T IH0 NG',
    'THINKING TH IH1 NG K IH0 NG',
    'SARONG S ER0 AO1 NG',
]

pronunciation_dict = {}
for w in SMALL_PRONOUNCING_LIST:
    w_list = w.split()
    pronunciation_dict[w_list[0]] = w_list[1:]


class TestCheckSyllableCounts(unittest.TestCase):
    def test_check_syllable_counts_one_line_poem(self):
        """ Test check_syllable_counts on a one line poem. """

        poem_lines = ['How now brown cow.']
        pattern = ([4], ['A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'one-line poem')

    # Place your unit test definitions after this line.
    #####################################################################################################################################################


    def test_multi_no_syllable_requirement(self):
        """Test check_syllables with no syllable requirements and multiple lines each with multiple words. Multiple lines are being tested in this
        case."""
        pattern = ([0, 0, 0], ['A', 'B', 'A'])
        word_to_phonemes = {'THEN': ['DH', 'EH1', 'N'], 'ENDS':
            ['EH1', 'N', 'D', 'Z'], 'WITH': ['W', 'IH1', 'DH'], 'THE':
                                ['DH', 'AH0'], 'A': ['AH0'], 'POEM': ['P', 'OW1', 'AH0', 'M'],
                            'FIRST': ['F', 'ER1', 'S', 'T'], 'LEADS': ['L', 'IY1', 'D', 'Z'],
                            'LINE': ['L', 'AY1', 'N'], 'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                            'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'], 'OFF': ['AO1', 'F']}
        poem_lines = ['The first line leads off the ,', 'With a the next.', 'the poem ends before the.']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_no_syllable_requirement(self):
        """Test check_syllables with no syllable requirements and multiple lines each with multiple words."""
        pattern = ([0], ['A'])
        word_to_phonemes = {'THEN': ['DH', 'EH1', 'N'], 'ENDS':
            ['EH1', 'N', 'D', 'Z'], 'WITH': ['W', 'IH1', 'DH'], 'THE':
                                ['DH', 'AH0'], 'A': ['AH0'], 'POEM': ['P', 'OW1', 'AH0', 'M'], 'FIRST':
                                ['F', 'ER1', 'S', 'T'], 'LEADS': ['L', 'IY1', 'D', 'Z'], 'LINE': ['L', 'AY1', 'N'],
                            'GAP': ['G', 'AE1', 'P'], 'NEXT': ['N', 'EH1', 'K', 'S',
                                                               'T'], 'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'OFF': ['AO1', 'F']}
        poem_lines = ['The first line leads off the gap,']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_syllable_requirment_no_match(self):
        """Test check_syllables with a single syllable requirement. Since pattern[0] only has 1 value, there must only be 1 line in poem_lines. In this test there is only 1 word. The word does not have the correct
        number of syllables."""
        pattern = ([1], ['A'])
        word_to_phonemes = {'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R']}
        poem_lines = ['Before']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['Before']
        self.assertEqual(actual, expected)

    def test_single_syllable_requirment_match(self):
        """Test check_syllables with a single syllable requirement. Since pattern[0] only has 1 value, there must only be 1 line in poem_lines. In this test there is only 1 word. The word has the correct number of syllables."""
        pattern = ([2], ['A'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['Poem']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_multi_syllable_requirement_no_match(self):
        """Test check_syllables with multiple syllable requirements. Since pattern[0] has 3 values, there must only be 3 lines in poem_lines. The number of words in each line is not being tested. The syllables in the lines of poem_lines do not match up with those in pattern[0]."""
        pattern = ([2, 1, 2], ['A', 'B', 'C'])
        word_to_phonemes = {'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'], 'NEXT':
            ['N', 'EH1', 'K', 'S', 'T'], 'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['Before poem,', 'next,', 'poem!!!']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['Before poem,']
        self.assertEqual(actual, expected)

    def test_multi_syllable_requirement_match(self):
        """Test check_syllables with multiple syllable requirements. Since pattern[0] has 3 values, there must only be 3 lines in poem_lines. The number of words in each line is not being tested. The syllables in the lines of poem_lines match up with those in pattern[0]."""
        pattern = ([2, 1, 2], ['A', 'B', 'C'])
        word_to_phonemes = {'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                            'NEXT': ['N', 'EH1', 'K', 'S', 'T'], 'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['Before,', 'next,', 'poem!!!']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_word_with_single_surrounding_punctuation(self):
        """Test check_syllables with a single word that has a single exclamation mark punctuation at the beginning and end."""
        pattern = ([2], ['A'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['!Poem!']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_single_word_with_multiple_surrounding_punctuation(self):
        """Test check_syllables with a single word that is surrounded by
        multiple punctuation characters."""
        pattern = ([2], ['A'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['....!!!!Poem!!!!....']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_line_with_internal_punctuation(self):
        """Test check_syllables with a single line that contains various punctuation inside of the line, but not inside of words."""
        pattern = ([8], ['A'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M']}
        poem_lines = ['....!!!!Poem$$ poem -- + poem poem!!.. ! $ @']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = []
        self.assertEqual(actual, expected)

    def test_multiple_lines_multiple_words(self):
        """Test with multiple lines. The syllable requirements and number of words are not being tests."""
        pattern = ([2, 2, 1], ['A', 'B', 'C'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M'], 'THE': ['DH',
                                                                      'AH0'], 'ENDS': ['EH1', 'N', 'D', 'Z']}
        poem_lines = ['The the,', 'poem ends', 'the ends!']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['poem ends', 'the ends!']
        self.assertEqual(actual, expected)

    def test_multiple_lines_single_word(self):
        """Test with multiple lines made of single words. The syllable requirements are not being tested."""
        pattern = ([2, 2, 1], ['A', 'B', 'C'])
        word_to_phonemes = {'POEM': ['P', 'OW1', 'AH0', 'M'], 'THE': ['DH',
                                                                      'AH0'], 'ENDS': ['EH1', 'N', 'D', 'Z']}
        poem_lines = ['The', 'poem', 'ends!']
        actual = poetry_functions.check_syllables(poem_lines, pattern, word_to_phonemes)
        expected = ['The']
        self.assertEqual(actual, expected)


# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
