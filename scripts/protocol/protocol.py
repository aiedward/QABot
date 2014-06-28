from command import Command, CommandExecutor
from abc import ABCMeta, abstractmethod

__author__ = 'Alexiy'


class Protocol:

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, command):
        """"execute command method"""


class LocalProtocol(Protocol):

    def __init__(self, command_executor):
        self._command_executor = command_executor

    def execute(self, command):
        return self._command_executor.execute(command)

Protocol.register(LocalProtocol)