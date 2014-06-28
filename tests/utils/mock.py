__author__ = 'Alexiy'


def mock_method(obj, method_name, return_arg=None):
    calls = []
    setattr(obj, method_name, lambda *args: __mocker(return_arg, calls, args))
    return calls


def __mocker(return_value, calls, args):
    calls.append(args)
    return return_value