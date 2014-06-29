from scripts.protocol.protocol import LocalProtocol, Protocol
from scripts.bot.scenario import load_scenario_from_json

__author__ = 'Alexiy'


class ScenarioBot():
    """bot for executing scenario"""

    def __init__(self, protocol):
        self._protocol = protocol

    def process(self, scenario):
        """just execute commands from scenario and return result of it"""
        result = []
        for command in scenario:
            command_result = self._protocol.execute(command)
            result.append(command_result)
            if command_result == Protocol.FAIL:
                break
        return result


class LocalScenarioBot(ScenarioBot):
    """bot for client side tests"""

    def __init__(self, command_executor):
        ScenarioBot.__init__(self, LocalProtocol(command_executor))

    def execute_scenario(self, json):
        try:
            scenario = load_scenario_from_json(json)
        except ValueError, e:
            print e
            print Protocol.FAIL
            return

        result = ScenarioBot.process(self, scenario)
        for item in result:
            print item

