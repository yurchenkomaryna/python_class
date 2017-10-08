"""This is the module mymodC in the package mynamespack. It defines a namefixer function.

"""

# You might want to use these.
COMMA = ','
SPACE = ' '


def namefixer(name):
    # """Given a comma-separated name, returns the name with the last names in uppercase.
    #
    # >>> name = "Flores Lopez, Juan Carlos"
    # >>> namefixer(name)
    # 'Juan Carlos FLORES LOPEZ'
    #
    # >>> author = 'Vargas Llosa, Mario'
    # >>> namefixer(author)
    # 'Mario VARGAS LLOSA'
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    name = name.split(', ')
    name[1], name[0] = name[0], name[1]
    upper_name = name[0], name[1].upper()
    name_str = ' '.join(upper_name)
    return name_str

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
