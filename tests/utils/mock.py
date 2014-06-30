__author__ = 'Alexiy'


def mock_method(obj, method_name, return_arg=None):
    """replace object method body, return list of calls"""
    calls = []
    setattr(obj, method_name, lambda *args: __mocker(return_arg, calls, args))
    return calls


def __mocker(return_value, calls, args):
    array = list(args)
    calls.append(array)
    return return_value