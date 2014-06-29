QABot
=====

Little bot for regression testing


Now it contains only prototype of QABot! 
You can run all unit and doc tests running all_unit_tests.py and run integration tests by running tests/integration/run_test/runner_test.py

How it works
------------

-- find stable version of your application 
-- add application side bot to it and version for executing scenario
  -- write command executors function and register in scripts.protocol.command.CommandExecutor
  -- add script file for running application in scenario mode, enabled by key -scenario
-- write some scenario in JSON format
-- run bot with standart application, testing application and list of scenarios file
-- PROFFIT

In plans:
---------

-- add tcp connection for extending comunicate protocol
-- add generator for tests

Also
----

I think it is good idea when automatisation generate new tests without programmer. I think it's possible write genetic algorithm that can work with small population of working tests and generate new population of working test.

Thanks Google for this idea: https://code.google.com/p/qualitybots/
