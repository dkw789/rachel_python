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

    """ (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line.

    # >>> get_poem_lines('The first line leads off,\n\n\n'
    # ... + 'With a gap before the next.\nThen the poem ends.\n')
    # ['The first line leads off,',
     ' With a gap before the next.',
      'Then the poem ends.']
    """


    # result = poem.split("\n")
    # return result


    final_poem=[]
    poem_list = poem.split('\n')
    for i in range(len(poem_list)):
        #  to append only if the string is not empty.

        if poem_list[i].strip() != '':
            final_poem.append(poem_list[i].strip())
    return final_poem



def count_vowel_phonemes(phonemes):
    """ (list of list of str) -> int

    Return the number of vowel phonemes in phonemes.

    >>> phonemes = [['N', 'OW1'], ['Y', 'EH1', 'S']]
    >>> count_vowel_phonemes(phonemes)
    2

    """



    number_of_vowel_phonemes = 0
    for phoneme in phonemes:
        for item in phoneme:
            # if  phoneme ends in 0, 1, or 2 the it's a vowel phoneme
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


    if phoneme_list:
        for phoneme in range(len(phoneme_list)):
            if phoneme_list[phoneme][-1].isdigit():
                last_vowel = phoneme_list[phoneme:]

        return last_vowel

    else:
        #else if all constanant return blank
        return []

def check_syllable_counts(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    # >>> pattern = ([5, 7, 5], ['*', '*', '*'])           ############## The actual pattern !!! ################


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
    # Splitting poem into lines
    for line in range(len(poem_lines)):
        syllables = 0
        words = poem_lines[line].split()
        cleaned_words = []
        for i in range(len(words)):
            # Only want to append strings that are not empty.
            if clean_up(words[i].strip()) != '':
                cleaned_words.append(clean_up(words[i].strip()))
        # Search through every phoneme and increment by one each time a vowel is found.
        for word in range(len(cleaned_words)):
            phonemes_of_word = word_to_phonemes[cleaned_words[word]]
            for phoneme in phonemes_of_word:
                if phoneme[-1].isdigit():
                    syllables += 1
        # Also comparing to 0 because we want to find those which are not matching
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

    for line in range(len(poem_lines)):
        no_rhyme = []
        for i in range(len(pattern[1])):
            if pattern[1][i] == pattern[1][line]:
                    no_rhyme.append(poem_lines[i])
        # Only want to append to no_rhyme_full if the list is not empty.
    if no_rhyme != []:
        no_rhyme_full.append(no_rhyme)
        #  no_rhyme = []
    return no_rhyme_full


if __name__ == '__main__':
    import doctest

    doctest.testmod()
