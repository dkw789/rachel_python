import builtins
import poetry_functions
import poetry_reader

# Check for use of functions print and input.

our_print = print
our_input = input


def disable_print(*args):
    raise Exception("You must not call built-in function print!")


def disable_input(*args):
    raise Exception("You must not call built-in function input!")


builtins.print = disable_print
builtins.input = disable_input

# Type checks for poetry_functions module

# Type check poetry_functions.get_poem_lines
result = poetry_functions.get_poem_lines('One,\ntwo,\nthree.\n')
assert isinstance(result, list), \
    '''poetry_functions.get_poem_lines should return a list,''' \
    ''' but returned {0}.'''.format(type(result))
for item in result:
    assert isinstance(item, str), \
        '''poetry_functions.get_poem_lines should return a list of str,''' \
        ''' but returned a list of {0}.'''.format(type(item))

# Type check poetry_functions.count_vowel_phonemes
result = poetry_functions.count_vowel_phonemes([['P', 'OW1', 'AH0', 'M']])
assert isinstance(result, int), \
    '''poetry_functions.count_vowel_phonemes should return an int,''' \
    ''' but returned {0}.'''.format(type(result))

# Type check poetry_functions.last_phonemes
result = poetry_functions.last_phonemes(['G', 'AE1', 'P'])
assert isinstance(result, list), \
    '''poetry_functions.last_phonemes should return a list,''' \
    ''' but returned {0}.'''.format(type(result))
for item in result:
    assert isinstance(item, str), \
        '''poetry_functions.last_phonemes should return a list of str,''' \
        ''' but returned a list of {0}.'''.format(type(item))

# Set-up for the below type checks.
poem_lines = ['The first line leads off,', 'With a gap before the next.',
              'Then the poem ends.']
pattern = ([5, 7, 5], ['A', 'B', 'A'])
word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
                    'GAP': ['G', 'AE1', 'P'],
                    'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
                    'LEADS': ['L', 'IY1', 'D', 'Z'],
                    'WITH': ['W', 'IH1', 'DH'],
                    'LINE': ['L', 'AY1', 'N'],
                    'THEN': ['DH', 'EH1', 'N'],
                    'THE': ['DH', 'AH0'],
                    'A': ['AH0'],
                    'FIRST': ['F', 'ER1', 'S', 'T'],
                    'ENDS': ['EH1', 'N', 'D', 'Z'],
                    'POEM': ['P', 'OW1', 'AH0', 'M'],
                    'OFF': ['AO1', 'F']}

# Type check poetry_functions.check_syllable_counts
result = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                word_to_phonemes)
assert isinstance(result, list), \
    '''poetry_functions.check_syllable_counts should return a list,''' \
    ''' but returned {0}.'''.format(type(result))
for item in result:
    assert isinstance(item, str), \
        '''poetry_functions.check_syllable_counts should return a list''' \
        ''' of str, but returned a list of {0}.'''.format(type(item))

# Type check poetry_functions.check_rhyme_scheme
result = poetry_functions.check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
assert isinstance(result, list), \
    '''poetry_functions.check_rhyme_scheme should return a list of''' \
    ''' list of str, but returned {0}.'''.format(type(result))
for item in result:
    assert isinstance(item, list), \
        '''poetry_functions.check_rhyme_scheme should return a list of''' \
        ''' list of str, but returned a list of {0}.'''.format(type(item))

# Type checks for poetry_reader module

# Type check poetry_reader.read_pronunciation
try:
    file = open('dictionary.txt')
except:
    assert False, '''place the pronunciation dictionary dictionary.txt ''' \
                  '''in the same folder as the typechecker'''
result = poetry_reader.read_pronunciation(file)
assert isinstance(result, dict), \
    '''poetry_reader.read_pronunciation should return a dict ''' \
    '''but returned {0}'''.format(type(result))
key = list(result.keys())[0]
assert isinstance(key, str), \
    '''poetry_reader.read_pronunciation should return a dict of ''' \
    '''str: list of str, but has keys of type {0}.'''.format(type(key))
assert isinstance(result[key], list), \
    '''poetry_reader.read_pronunciation should return a dict of ''' \
    '''str: list of str, but has values of type {0}.''' \
        .format(type(result[key]))
for item in result[key]:
    assert isinstance(item, str), \
        '''poetry_reader.read_pronunciation should return a dict of ''' \
        '''str: list of str, but instead returned a dict of ''' \
        '''str: list of {0}.''' \
            .format(type(item))

# Type check poetry_reader.read_poetry_form_descriptions
try:
    file = open('poetry_forms.txt')
except:
    assert False, '''place the poetry forms file poetry_forms.txt ''' \
                  '''in the same folder as the typechecker'''
result = poetry_reader.read_poetry_form_descriptions(file)
assert isinstance(result, dict), \
    '''poetry_reader.read_poetry_form should return a dict but ''' \
    '''returned {0}'''.format(type(result))
key = list(result.keys())[0]
assert isinstance(key, str), \
    '''poetry_reader.read_poetry_form should return a dict of ''' \
    ''' str: poetry pattern, but returned keys of type {0}''' \
        .format(type(key))
result = result[key]
assert isinstance(result, tuple), \
    '''poetry_reader.read_poetry_form should return a dict with values ''' \
    ''' that are poetry patterns but has values of type {0}''' \
        .format(type(result))
assert isinstance(result[0], list), \
    '''poetry_reader.read_poetry_form should return a dict with values ''' \
    ''' that are poetry patterns, but the first element has type {0}''' \
        .format(type(result[0]))
assert isinstance(result[1], list), \
    '''poetry_reader.read_poetry_form should return a dict with values ''' \
    ''' that are poetry patterns, but the second element has type {0}''' \
        .format(type(result[1]))
for item in result[0]:
    assert isinstance(item, int), \
        '''poetry_reader.read_poetry_form should return a dict with values ''' \
        ''' that are poetry patterns, but the first element is a ''' \
        '''list of {0}'''.format(type(item))
for item in result[1]:
    assert isinstance(item, str), \
        '''poetry_reader.read_poetry_form should return a dict with values ''' \
        ''' that are poetry patterns, but the second element is a ''' \
        '''list of {0}'''.format(type(item))

builtins.print = our_print
builtins.input = our_input

print("""

The type checker passed.

This means that the functions in poetry_functions.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.

This does NOT mean that the functions are correct!

Run the doctests to execute one test case per required
poetry_functions.py function.

Be sure to thoroughly test your functions yourself before submitting.
""")
