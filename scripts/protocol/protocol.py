from abc import ABCMeta, abstractmethod

__author__ = 'Alexiy'


class Protocol:
    """base protocol class"""
    __metaclass__ = ABCMeta

    FAIL = 'Failed'

    @abstractmethod
    def execute(self, command):
        """"execute command method"""


class LocalProtocol(Protocol):
    """simple protocol for using bots within app"""

    def __init__(self, command_executor):
        self._command_executor = command_executor

    def execute(self, command):
        if not self._command_executor.has_executor(command.name):
            return Protocol.FAIL
        try:
            result = self._command_executor.execute(command)
        except:
            result = Protocol.FAIL
        return result

Protocol.register(LocalProtocol)