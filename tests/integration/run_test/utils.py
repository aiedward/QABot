__author__ = 'Alexiy'


def parse_scenario(argv):
    index = 0
    argc = len(argv)

    while index < argc:
        if argv[index] != '-scenario':
            index += 1

        index += 1

        if index >= argc:
            return

        with open(argv[index]) as f:
            return f.read()
