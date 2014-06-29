import unittest
from scripts.protocol.command import CommandExecutor, Command

__author__ = 'Alexiy'


def create_command_executor():
    return CommandExecutor()


class CommandExecutorTest(unittest.TestCase):

    def test_has_executor_should_return_true_for_added_executor(self):
        name = 'some_id'
        command_executor = create_command_executor()

        command_executor.register_executor(name, {})

        self.assertTrue(command_executor.has_executor(name))

    def test_has_executor_should_return_false_for_not_added_executor(self):
        name = 'some_id'
        command_executor = create_command_executor()

        self.assertTrue(not command_executor.has_executor(name))

    def test_has_executor_should_return_false_after_call_clear_executors(self):
        name = 'some_id'
        command_executor = create_command_executor()

        command_executor.register_executor(name, {})
        command_executor.clear_executors()

        self.assertTrue(not command_executor.has_executor(name))

    def test_execute_should_call_executor_by_name(self):
        expected_result = 'first_called'
        execute_command_name = 'first'
        command_executor = create_command_executor()
        command_executor.register_executor(execute_command_name, lambda args: expected_result)
        command_executor.register_executor('second', lambda args: 'second_called')
        command = Command(execute_command_name, None)

        result = command_executor.execute(command)

        self.assertEqual(result, expected_result)

    def test_execute_should_throw_exception_if_executor_not_found(self):
        command_executor = create_command_executor()
        command_executor.register_executor('some_id', None)
        command = Command('other_id', None)

        self.assertRaises(KeyError, command_executor.execute, command)
