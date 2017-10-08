"""This is mynamespack.mymodD

"""

# You might want to use these.
COMMA = ','
SPACE = ' '
COLON = ':'


DATAFILE = 'data/names.txt'


def ndatalines():
    # """Returns the number of lines in our DATAFILE.txt. Blank lines are also counted.
    #
    # >>> ndatalines()
    # 12
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    with open(DATAFILE, 'r') as fd:
        lines = fd.readlines()
        result = len(lines)
    return result


def line2tuple(line):
    # """Breaks up data lines into a tuple of length 3. See the DATAFILE.
    #
    # >>> line = 'Chang, Emily            Bloomberg Technology'
    # >>> line2tuple(line)
    # ('Bloomberg Technology', 'Emily', 'Chang')
    #
    # >>> line = 'Maddow, Rachel Anne     MSNBC'
    # >>> line2tuple(line)
    # ('MSNBC', 'Rachel Anne', 'Maddow')
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    line = line.strip()
    names, company = line[:24], line[24:]
    lastnames, firstnames = names.split(',')
    firstnames = firstnames.strip()
    result = (company, firstnames, lastnames)
    return result


def datafile2tuples():
    # """ Reads the DATAFILE and returns a list of tuples for all lines, except blank lines.
    #
    # >>> mytuples = datafile2tuples()
    # >>> len(mytuples)
    # 9
    #
    # >>> for t in mytuples:
    # ...     print(t)
    # ('Bloomberg Technology', 'Emily', 'Chang')
    # ('Apple Inc', 'Tim', 'Cook')
    # ('AMD', 'Lisa', 'Su')
    # ('Google', 'Sundai', 'Pichar')
    # ('Microsoft', 'Satyar', 'Nadella')
    # ('Tesla Motors', 'Elon', 'Musk')
    # ('Yahoo', 'Marissa', 'Mayer')
    # ('Amazon', 'Jeff', 'Bezos')
    # ('MSNBC', 'Rachel Anne', 'Maddow')
    # """

    # REPLACE THE pass BELOW WITH YOUR OWN CODE.
    mytuples = []
    with open(DATAFILE, 'r') as fd:
        lines = fd.read().splitlines()
        for line in lines:
            if not line.strip():
                continue
            else:
                tuple_lines = line2tuple(line)
                mytuples.append(tuple_lines)
    return (mytuples)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
