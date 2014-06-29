import doctest
__author__ = 'Alexiy'


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite('local_scenario_bot.rst'))
    return tests

if __name__ == '__main__':
    doctest.testfile('local_scenario_bot.rst')