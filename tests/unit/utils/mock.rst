==========
Mock Tests
==========

Anyway we should use import module

    >>> from tests.utils import mock

And define class for mocking

    >>> class SomeClass():
    ...     def method(self, arg):
    ...         return arg

mocked method should not be called
----------------------------------
::

    >>> obj = SomeClass()
    >>> calls = mock.mock_method(obj, 'method', 'mock')
    >>> obj.method(None)
    'mock'

mock method without return value should return None
---------------------------------------------------
::

    >>> obj = SomeClass()
    >>> calls = mock.mock_method(obj, 'method')
    >>> obj.method(None)


mock method do not affect on other objects
------------------------------------------
::

    >>> obj = SomeClass()
    >>> calls = mock.mock_method(obj, 'method', 'mock')
    >>> other_obj = SomeClass()
    >>> other_obj.method('data')
    'data'

mock method should return calls
-------------------------------
::

    >>> obj = SomeClass()
    >>> mock.mock_method(obj, 'method')
    []

mock method should append call array after every call
-----------------------------------------------------
::

    >>> obj = SomeClass()
    >>> calls = mock.mock_method(obj, 'method')
    >>> var = obj.method('data')
    >>> calls
    [['data']]

    >>> var = obj.method('other_data')
    >>> calls
    [['data'], ['other_data']]

    >>> var = obj.method('another_data')
    >>> calls
    [['data'], ['other_data'], ['another_data']]

