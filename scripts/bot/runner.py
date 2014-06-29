import os
from subprocess import Popen, PIPE

__author__ = 'Alexiy'


def _run_scenario(app, scenario):
    """run scenario for application in its own process"""
    args = [app, '-scenario', scenario]
    process = Popen(args, stdout=PIPE, shell=True)
    (output, _) = process.communicate()
    exit_code = process.wait()
    return output, exit_code


def _compare_output(standart_output, testing_output):
    """compare outputs, returns False if it's different, True otherwise"""
    standart_output_array = standart_output.splitlines()
    testing_output_array = testing_output.splitlines()
    standart_output_array_len = len(standart_output_array)
    testing_output_array_len = len(testing_output_array)

    if standart_output_array_len != testing_output_array_len:
        print 'there is different count of steps standart: ', standart_output_array_len, \
            ' testing: ', testing_output_array_len
        return False

    for index in range(0, len(standart_output_array), 1):
        if standart_output_array[index] != testing_output_array[index]:
            print 'there is different results in same step for standsret: ', standart_output_array[index], \
                ' testing: ', testing_output_array[index]
            return False

    return True


def run_test(standart_app, testing_app, *scenario_files):
    """run scenario test for standart app and then on testing"""
    passed = True

    for scenario_file in scenario_files:
        print 'Run scenario: ', scenario_file

        (standart_output, standart_exit_code) = _run_scenario(standart_app, scenario_file)
        if standart_exit_code != 0:
            print 'Standart application finish scenario with code: ', standart_exit_code
            continue

        (testing_output, testing_exit_code) = _run_scenario(testing_app, scenario_files)
        if testing_exit_code != 0:
            print 'Testing application finish scenario with code: ', scenario_file
            continue

        pass_scenario = _compare_output(standart_output, testing_output)

        print 'Pass' if pass_scenario else 'Failed'

        if not pass_scenario:
            passed = False

    return passed

