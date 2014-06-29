import unittest
from scripts.bot.scenario import Scenario

__author__ = 'Alexiy'


def create_scenario(count_data=0):
    scenario = Scenario()
    counter = 0
    while counter < count_data:
        counter += 1
        scenario.add_command({})
    return scenario


def has_in_scenario(scenario, command):
    for item in scenario:
        if item == command:
            return True
    return False


class ScenarioTest(unittest.TestCase):

    def test_add_command_should_work(self):
        command = 'data'
        scenario = create_scenario()

        scenario.add_command(command)

        self.assertTrue(has_in_scenario(scenario, command))

    def test_scenario_should_enumerate_inner_values(self):
        count = 10
        counter = 0
        scenario = create_scenario(count)

        for _ in scenario:
            counter += 1

        self.assertEqual(counter, count)

    def test_scenario_string_should_be_like_array_of_commands(self):
        scenario = create_scenario(3)

        scenario_str = str(scenario)

        self.assertEqual(scenario_str, '[{}, {}, {}]')

    def test_equals_same_scenario_should_return_true(self):
        scenario1 = create_scenario(3)
        scenario2 = create_scenario(3)

        self.assertTrue(scenario1 == scenario2)

    def test_equals_different_scenario_should_return_false(self):
        scenario1 = create_scenario(4)
        scenario2 = create_scenario(3)

        self.assertFalse(scenario1 == scenario2)

    def test_equals_scenario_and_object_with_same_data_should_return_false(self):
        scenario1 = create_scenario(3)
        scenario2 = [{}, {}, {}]

        self.assertFalse(scenario1 == scenario2)

