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


if __name__ == "__main__":
    unittest.main()