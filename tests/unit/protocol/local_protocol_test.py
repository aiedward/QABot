import unittest
from tests.utils.mock import mock_method
from scripts.protocol.protocol import LocalProtocol, Protocol
from scripts.protocol.command import CommandExecutor, Command

__author__ = 'Alexiy'


def create_local_protocol(command_executor):
    return LocalProtocol(command_executor)


class FakeExecutor():
    """executor for testing"""

    FAIL_COMMAND_NAME = 'fail'

    def has_executor(self, _):
        return True

    def execute(self, command):
        if command.name == FakeExecutor.FAIL_COMMAND_NAME:
            raise Exception()


class LocalProtocolTest(unittest.TestCase):

    def test_execute_should_call_execute_from_command_executor(self):
        command = Command(None,  None)
        command_executor = CommandExecutor()
        protocol = create_local_protocol(command_executor)
        mock_method(command_executor, 'has_executor', True)
        calls = mock_method(command_executor, 'execute')

        protocol.execute(command)

        self.assertEqual(calls, [[command]])

    def test_execute_should_not_throw_error_if_executor_for_command_not_found(self):
        command_executor = CommandExecutor()
        protocol = create_local_protocol(command_executor)

        result = protocol.execute(Command('some_name', None))

        self.assertEqual(result, Protocol.FAIL)

    def test_execute_should_not_throw_error_if_command_do(self):
        command_executor = FakeExecutor()
        protocol = create_local_protocol(command_executor)

        result = protocol.execute(Command(FakeExecutor.FAIL_COMMAND_NAME, None))

        self.assertEqual(result, Protocol.FAIL)
