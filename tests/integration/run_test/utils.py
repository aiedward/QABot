__author__ = 'Alexiy'


def parse_scenario(argv):
    index = 0
    argc = len(argv)

    # try find -scenario key in args
    # next arg after -scenario key should be scenario file name
    while index < argc:
        if argv[index] != '-scenario':
            index += 1

        index += 1

        if index >= argc:
            return

        # read scenario
        with open(argv[index]) as f:
            return f.read()
