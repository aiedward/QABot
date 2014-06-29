import unittest
from tests.utils.mock import mock_method
from scripts.protocol.protocol import LocalProtocol
from scripts.protocol.command import CommandExecutor

__author__ = 'Alexiy'


def create_local_protocol(command_executor):
    return LocalProtocol(command_executor)


class LocalProtocolTest(unittest.TestCase):

    def test_execute_should_call_execute_from_command_executor(self):
        command = {}
        command_executor = CommandExecutor()
        protocol = create_local_protocol(command_executor)
        calls = mock_method(command_executor, 'execute')

        protocol.execute(command)

        self.assertEqual(calls, [[command]])

if __name__ == "__main__":
    unittest.main()