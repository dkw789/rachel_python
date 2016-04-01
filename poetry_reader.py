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


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    # file = open('dictionary.txt', 'r')
    #
    # for line in file:
    #     print line

    #################   https://m.reddit.com/r/CompSciPortfolio/comments/303fyo/assignment_3_poetry_reader/

    # pronunciation_dictionary = {}
    # line = pronunciation_file.readline()
    # while line.startswith(';;;'):
    #     line = pronunciation_file.readline()
    # while line != '':
    #     stripped_line = line.strip()
    #     separation = stripped_line.find(' ')
    #     pronunciation_dictionary[stripped_line[:separation]] = stripped_line[(separation + 2):].split()
    #     line = pronunciation_file.readline()
    # return pronunciation_dictionary



    my_list = {}
    for line in pronunciation_file.readlines():
        line = line.strip()
        if line and ";;;" not in line:
            r = line.split()
            word = r[0]
            phonemes = r[1:]
            my_list[word] = phonemes
    return my_list


def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """

    # def read_poetry_form_description(poetry_forms_file):
    #     poetry_pattern = ()
    #     syllables = []
    #     rhyme = []
    #     line = poetry_forms_file.readline()
    #     while line != '\n' and line != '':
    #         stripped_line = line.strip()
    #         separation = stripped_line.find(' ')
    #         syllables.append(int(stripped_line[:separation]))
    #         rhyme.append(stripped_line[(separation + 1):])
    #         line = poetry_forms_file.readline()
    #     poetry_pattern = (syllables, rhyme)
    #     return poetry_pattern
    #
    #
    #
    # dictionary = {}
    # line = poetry_forms_file.readline()
    # while line != '' and line != '\n':
    #     name = line.strip()
    #     pattern = read_poetry_form_description(poetry_forms_file)
    #     dictionary[name] = pattern
    #     line = poetry_forms_file.readline()
    # return dictionary

    my_list = {}
    buffers = []
    for line in poetry_forms_file.readlines():
        line = line.strip()
        if line:
            buffers.append(line)
        else:
            name = buffers[0]
            syllables = []
            rhymes = []
            for s in buffers[1:]:
                r = s.split()
                syllables.append(int(r[0]))
                rhymes.append(r[1])
            pattern = (syllables, rhymes)
            my_list[name] = pattern
            buffers = []
    return my_list


# f = open("dictionary.txt")
# print len(read_pronunciation(f))


# f = open("poetry_form.txt")
# print read_poetry_form_description(f)


# f = open("poetry_forms.txt")
# print read_poetry_form_descriptions(f)