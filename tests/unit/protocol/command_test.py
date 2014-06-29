import unittest
from scripts.protocol.command import Command

__author__ = 'Alexiy'


def create_command(name, args):
    return Command(name, args)


def create_executor(name, args):
    return Command(name, args)


class CommandTest(unittest.TestCase):

    def test_name_property_should_work(self):
        expected_name = 'some_name'
        command = create_command(expected_name, None)

        result_name = command.name

        self.assertEqual(result_name, expected_name)

    def test_args_property_should_work(self):
        expected_args = (10, [], {}, 'data')
        command = create_command(None, expected_args)

        result_args = command.args

        self.assertEqual(result_args, expected_args)

    def test_str_method_should_work(self):
        command = create_command('some_name', 'data')

        str_command = str(command)

        self.assertTrue("'_name': 'some_name'" in str_command)
        self.assertTrue("'_args': 'data'" in str_command)

    def test_equals_should_return_true_for_commands_with_same_data(self):
        command_name = 'some_name'
        command_args = 'args'

        command1 = create_command(command_name, command_args)
        command2 = create_command(command_name, command_args)

        self.assertTrue(command1 == command2)

    def test_equals_command_and_object_with_same_data_should_return_false(self):
        command_name = 'some_name'
        command_args = 'args'

        command1 = create_command(command_name, command_args)
        command2 = {'_name': command_name, '_args': command_args}

        self.assertFalse(command1 == command2)

    def test_equals_commands_with_different_data_should_return_false(self):
        command1 = create_command('some_name', 'some_data')
        command2 = create_command('other_name', 'other_data')

        self.assertFalse(command1 == command2)
