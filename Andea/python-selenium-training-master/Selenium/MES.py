"""
Main file.
It is being used to execute chosen test scenarios.
"""


import pytest
import os
import py.io

def runTest(test_name):
    tests_path = os.path.dirname((__file__)) + "\\Tests\\"
    capture = py.io.StdCapture()
    pytest.main(["--capture=sys", "-v", "-rf", "--tb=line", "--color=no", "--no-print-logs", tests_path + test_name])
    std, err = capture.reset()
    # print("std:" +std)
    # print("err:" +err)

    parsedStd=[]
    for line in str(std).splitlines():
        # print("line "+line)
        parsedStd.append(str(line))

    return parsedStd

# runTest("test_MachineStates.py::test_MachineStates::test_MachineStates_TC1")
# runTest("test_MachineStates.py::test_MachineStates::test_MachineStates_TC2")



runTest("test_PHPTadmin_KK.py::test_PHPTadmin_KK")





"""                         ########## OLD VERSION ##########
# import unittest2
# from Tests.test_MachineStates import test_MachineStates
#
# # Get scenarios from test_ classes
# scenario_MachineStates = unittest2.TestLoader().loadTestsFromTestCase(test_MachineStates)
#
# # Create a test suite with needed test scenarios
# LESSuite = unittest2.TestSuite([scenario_MachineStates])
#
# # Run chosen test suite
# unittest2.TextTestRunner(verbosity=2).run(LESSuite)

import pytest
import os

def runTest(test_name):
    tests_path = os.path.dirname((__file__)) + "\\Tests\\"
    pytest.main(["-s", "-v", "--tb=line", tests_path + test_name])

    return "message"

# runTest("test_MachineStates.py::test_MachineStates::test_MachineStates_TC1")
"""