"""
A poetry pattern:  tuple of (list of int, list of str)
  o first item is a list of the number of syllables required in each line
  o second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  o each key is a word (a str)
  o each value is a list of phonemes for that word (a list of str)
"""


# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.


# ===================== Required Functions =====================

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
    result = poem.split("\n")
    return result


########### https://www.reddit.com/r/CompSciPortfolio/comments/303fpv/assignment_3_poetry_functions/


def count_vowel_phonemes(phonemes):
    """ (list of list of str) -> int

    Return the number of vowel phonemes in phonemes.

    >>> phonemes = [['N', 'OW1'], ['Y', 'EH1', 'S']]
    >>> count_vowel_phonemes(phonemes)
    2

    """

    ####################################################https: // stackoverflow.com / questions / 29322310 / count - items - using - nested - loops


    number_of_vowel_phonemes = 0
    for phoneme in phonemes:
        for item in phoneme:
            # if 0 or 1 or 2 in item:
            if "0" in item or "1" in item or "2" in item:
                number_of_vowel_phonemes = number_of_vowel_phonemes + 1
    return number_of_vowel_phonemes


def last_phonemes(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and any subsequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.

    >>> last_phonemes(['AE1', 'B', 'S', 'IH0', 'N', 'TH'])
    ['IH0', 'N', 'TH']
    >>> last_phonemes(['IH0', 'N'])
    ['IH0', 'N']
    """

    ################## https://stackoverflow.com/questions/29402908/return-a-list-that-contains-the-last-vowel-phoneme-and-subsequent-consonant-phon

    for i, phoneme in reversed(list(enumerate(phoneme_list))):
        if phoneme[-1] in '012':
            return phoneme_list[i:]
    return []


def check_syllable_counts(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'],
    ...                     'A': ['AH0'],
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'],
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllable_counts(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllable_counts(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """
    wrong_number_syllables = []
    full_words = []
    for line in range(len(poem_lines)):
        syllables = 0
        words = poem_lines[line].split()
        full_words = []
        for i in range(len(words)):
            # Only want to append strings that are not empty.
            if clean_up(words[i].strip()) != '':
                full_words.append(clean_up(words[i].strip()))
        # Search through every phoneme and add 1 each time a stress is found.
        for word in range(len(full_words)):
            phonemes_of_word = word_to_phonemes[full_words[word]]
            for phoneme in phonemes_of_word:
                if phoneme[-1].isdigit():
                    syllables += 1
        # Also comparing to 0 because we don't care when it is 0.
        if syllables != pattern[0][line] and pattern[0][line] != 0:
            wrong_number_syllables.append(poem_lines[line])
    return wrong_number_syllables


def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary)
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with
    each other but don't. If all lines rhyme as they should, return the empty
    list.

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'],
    ...                     'A': ['AH0'],
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'],
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> bad_lines = check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    >>> bad_lines.sort()
    >>> bad_lines
    [['The first line leads off,', 'Then the poem ends.']]
    """
    no_rhyme_full = []
    # # tester is used to ensure that no line is checked twice.
    # tester = make_tester(poem_lines)
    for line in range(len(poem_lines)):
        no_rhyme = []
        check = True
        # phonemes_of_word = last_word_phonemes(line, poem_lines, word_to_phonemes)

        # last_stress = last_stress_finder(phonemes_of_word)
        line_to_check = 0
        while check and line_to_check < len(poem_lines):
            # Compares to '*' because we don't care when it is '*'.
            if pattern[1][line] == pattern[1][line_to_check] and pattern[1][line_to_check] != '*':
                phonemes_of_word = last_phonemes(line_to_check, poem_lines, word_to_phonemes)
                # Will check if the last stress of the last word of poem_lines[line] is equal to the phonemes of the last word of poem_lines[line_to_check]
                # check = match(last_stress, phonemes_of_word)
            line_to_check += 1
            # if not check and tester[line] == 0:
            no_rhyme = []
            for i in range(len(pattern[1])):
                if pattern[1][i] == pattern[1][line]:
                    # Value of tester[i] is changed because it indicates that
                    # the specific line in poem_lines has already been checked.
                    # tester[i] = 1
                    no_rhyme.append(poem_lines[i])
        # Only want to append to no_rhyme_full if the list is not empty.
        if no_rhyme != []:
            no_rhyme_full.append(no_rhyme)
        no_rhyme = []
    return no_rhyme_full


if __name__ == '__main__':
    import doctest

    doctest.testmod()
