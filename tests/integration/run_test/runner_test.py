import unittest

from scripts.bot.runner import run_test


__author__ = 'Alexiy'


class RunTest(unittest.TestCase):

    def test_run_test_should_pass_for_the_same_app(self):
        app1 = 'app1.py'
        scenario1 = 'scenario1'

        is_pass = run_test(app1, app1, scenario1)

        self.assertTrue(is_pass)

    def test_run_test_should_fail_for_apps_with_different_results(self):
        app1 = 'app1.py'
        app2 = 'app2.py'
        scenario1 = 'scenario1'

        is_pass = run_test(app1, app2, scenario1)

        self.assertFalse(is_pass)