import unittest
import json
from scripts.bot.scenario import load_scenario_from_json, Scenario
from scripts.protocol.command import Command

__author__ = 'Alexiy'


def create_scenario(*commands):
    scenario = Scenario()
    for command in commands:
        scenario.add_command(command)
    return scenario


def create_scenario_json(*commands):
    array = []
    for command in commands:
        array.append(command.__dict__)
    return json.dumps(array)


class LoadScenarioFromJsonTest(unittest.TestCase):

    def test_parsing_valid_json_should_work(self):
        command = Command('some_name', ['data', 1, {}])
        expected_scenario = create_scenario(command)
        json_data = create_scenario_json(command)

        result_scenario = load_scenario_from_json(json_data)

        self.assertEqual(expected_scenario, result_scenario)

    def test_parsing_invalid_json_should_raise_exception(self):
        json_data = '{'

        self.assertRaises(ValueError, load_scenario_from_json, json_data)

    def test_parsing_json_without_array_as_root_should_raise_exception(self):
        json_data = '{}'

        self.assertRaises(ValueError, load_scenario_from_json, json_data)

    def test_parsing_json_with_command_without_args_should_raise_exception(self):
        json_data = "[{'_args':12}]"

        self.assertRaises(ValueError, load_scenario_from_json, json_data)

    def test_parsing_json_with_command_without_name_should_raise_exception(self):
        json_data = "[{'_name':'some_name'}]"

        self.assertRaises(ValueError, load_scenario_from_json, json_data)

