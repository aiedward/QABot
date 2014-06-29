import json
from scripts.protocol.command import Command

__author__ = 'Alexiy'


class Scenario():
    """represents list of actions"""

    def __init__(self):
        self._commands = []

    def __str__(self):
        return str(self._commands)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __iter__(self):
        for command in self._commands:
            yield command

    def add_command(self, command):
        self._commands.append(command)


def load_scenario_from_json(data):
    """parse json to scenario object"""

    result = Scenario()
    obj = json.loads(data)

    if not isinstance(obj, list):
        raise ValueError('object is ' + str(type(obj)))

    for command in obj:
        if '_name' not in command:
            raise ValueError(str(command) + ' doesnt contains name')
        if '_args' not in command:
            raise ValueError(str(command) + ' doesnt contains args')
        result.add_command(Command(command['_name'], command['_args']))

    return result
