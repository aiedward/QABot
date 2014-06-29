import sys

from tests.integration.run_test.utils import parse_scenario
from tests.integration.run_test.commands_executors import get_command_executor
from scripts.bot.scenario_bot import LocalScenarioBot


__author__ = 'Alexiy'


def main(argv):
    scenario = parse_scenario(argv)
    if scenario is None:
        return -1
    command_executor = get_command_executor()
    bot = LocalScenarioBot(command_executor)
    bot.execute_scenario(scenario)


if __name__ == '__main__':
    main(sys.argv)