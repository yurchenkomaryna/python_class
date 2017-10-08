"""This is my mymodA module in my mynamespack package. It defines some functions that create acronyms.

"""

__course__ = 'CS131A:Wostner:Fall2017'

# EDIT THE __author__ and __date__ lines below.
__author__ = 'myurchen'
__date__ = '2017-09-22'


# First, we define two slightly different functions, acronym1 and acronym2.

BLANK = ' '

def acronym1(s):
    # """Given a string s, returns an acronym based on the first letter of each  word in the string.
    #
    # >>> acronym1('Environmental Protection Agency')
    # 'EPA'
    # >>> acronym1('Supreme Court of the United States')
    # 'SCOTUS'
    # """
    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    for word in s:
        words = s.split(BLANK)
        for_loop = [letter[0] for letter in words]
        join_letters = ''.join(for_loop)
        result = join_letters.upper()
        return result


def acronym2(s):
    # """Given a string s, returns an acronym based on all uppercase letters in the string.
    #
    # >>> acronym2('FaceBook')
    # 'FB'
    # >>> acronym2('City College of San Franciso')
    # 'CCSF'
    # >>> acronym2('HyperText Markup Language')
    # 'HTML'
    #
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE
    for word in s:
        join_upper = ''.join([o for o in s if o.isupper()])
        return join_upper

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
