__author__ = 'Alexiy'


class Command:
    """class represents command for protocol"""

    def __init__(self, name, args):
        self._name = name
        self._args = args

    @property
    def name(self):
        """unique command name"""
        return self._name

    @property
    def args(self):
        """args for command"""
        return self._args


class CommandExecutor():
    """class processes command by executor"""
    def __init__(self):
        self._executors = {}

    def register_executor(self, name, executor):
        """registers executor with unique name"""
        self._executors[name] = executor

    def has_executor(self, name):
        """check if executor with name was registered"""
        return name in self._executors

    def clear_executors(self):
        """clear all executors"""
        self._executors.clear()

    def execute(self, command):
        """try find executor for command by its name and execute command"""
        if not self.has_executor(command.name):
            raise KeyError('Cant find executor for: ', command.name)
        executor = self._executors[command.name]
        return executor(command.args)
