import unittest

__author__ = 'Alexiy'


if __name__ == '__main__':
    test_suite = unittest.TestLoader().discover('./tests/unit/', '*test.py')
    unittest.TextTestRunner(verbosity=1).run(test_suite)