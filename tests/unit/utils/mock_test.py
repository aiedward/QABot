import doctest

__author__ = 'Alexiy'


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite('mock.rst'))
    return tests

if __name__ == '__main__':
    doctest.testfile('mock.rst')