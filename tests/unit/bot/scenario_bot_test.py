import unittest
from tests.utils.mock import mock_method
from scenario_test import create_scenario
from scripts.bot.scenario_bot import ScenarioBot
from scripts.protocol.protocol import LocalProtocol, Protocol

__author__ = 'Alexiy'


class ScenarioBotTest(unittest.TestCase):

    def test_bot_should_process_scenario(self):
        protocol = LocalProtocol(None)
        bot = ScenarioBot(protocol)
        scenario = create_scenario(4)
        mock_method(protocol, 'execute', True)

        result = bot.process(scenario)

        self.assertEqual(result, [True, True, True, True])

    def test_process_should_stop_after_first_fail(self):
        protocol = LocalProtocol(None)
        bot = ScenarioBot(protocol)
        scenario = create_scenario(4)
        mock_method(protocol, 'execute', Protocol.FAIL)

        result = bot.process(scenario)

        self.assertEqual(result, [Protocol.FAIL])