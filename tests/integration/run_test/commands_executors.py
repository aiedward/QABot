from scripts.protocol.command import CommandExecutor

__author__ = 'Alexiy'


def raise_exception():
    raise Exception()


def get_command_executor(has_differ=False):
    """return inited CommandExecutor"""
    data = []
    command_executor = CommandExecutor()
    command_executor.register_executor('get_num', lambda args: 10)
    command_executor.register_executor('get_str', lambda args: 'bad_str' if has_differ else 'some_str')
    command_executor.register_executor('push_data', lambda args: data.append(args))
    command_executor.register_executor('pop_data', lambda args: data.pop())
    command_executor.register_executor('raise_exception', lambda args: raise_exception())
    return command_executor