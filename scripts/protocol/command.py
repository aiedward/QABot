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


