"""This is the module mymodB in mynamespack. Defines functions for person names.

"""

# You might want to use these.
COMMA = ','
SPACE = ' '
PERIOD = '.'


def initials(name):
    # """Given a name returns the initials.
    #
    # >>> initials('Elon Reeve Musk')
    # 'E.R.M.'
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    name = PERIOD.join([letter for letter in name if letter.isupper()])
    return name + PERIOD

def name2tuple(name):
    # """Given a comma-separated name, returns a tuple of the form (firstnames, lastnames).
    #
    # >>> tvhost = "Maddow, Rachel Anne"
    # >>> name2tuple(tvhost)
    # ('Rachel Anne', 'Maddow')
    #
    # >>> author = "Borges Acevedo, Jorge Francisco Isidoro Luis"
    # >>> name2tuple(author)
    # ('Jorge Francisco Isidoro Luis', 'Borges Acevedo')
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    name = name.split(', ')
    name[1], name[0] = name[0], name[1]
    tupple_name = tuple(name)
    return tupple_name



# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

