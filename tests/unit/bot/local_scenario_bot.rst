=======================
Local Scenario Bot Test
=======================

Anyway we should use import module

    >>> from scripts.bot.scenario_bot import LocalScenarioBot
    >>> from scripts.protocol.command import CommandExecutor

create command executor

    >>> command_executor = CommandExecutor()

init executor

    >>> command_executor.register_executor('some_executor', lambda args: 'from some executor: ' + str(args))
    >>> command_executor.register_executor('other_executor', lambda args: 'from other executor: ' + str(args))

create LocalScenarioBot

    >>> bot = LocalScenarioBot(command_executor)

execute scenario with valid json should work
--------------------------------------------
::

    >>> bot.execute_scenario('[{"_args": 5, "_name": "some_executor"}]')
    from some executor: 5

    >>> bot.execute_scenario('[{"_args": [5, "data"], "_name": "other_executor"}]')
    from other executor: [5, u'data']

    >>> bot.execute_scenario('[{"_args": 5, "_name": "some_executor"}, {"_args": 8, "_name": "other_executor"}]')
    from some executor: 5
    from other executor: 8


execute scenario with invalid json should return Failed
-------------------------------------------------------
::

    >>> bot.execute_scenario('{"_args": 5, "_name": "some_executor"}')
    Failed

execute scenario with invalid command name should return Failed
---------------------------------------------------------------
::

    >>> bot.execute_scenario('[{"_args": 5, "_name": "another_executor"}]')
    Failed
