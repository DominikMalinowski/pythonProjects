"""
Assertions.py handles all assertions.
Import it to the test_ class.
"""

import Selenium.Utilities.Logger as ml
import inspect

logs = ml.MESlogger()
result_list = []

def setResult(actual, expected):
    """ It's a base method. If result is True, add 'PASS' to the results list, if not, add 'FAIL' """
    result = actual == expected
    try:
        if result is not None:
            if result:
                result_list.append("PASS")
                logs.info("Verification PASS. Actual results: " + actual + ", Expected results: " + expected)
            else:
                result_list.append("FAIL")
                logs.warning("Verification FAIL. Actual results: " + actual + ", Expected results: " + expected)
        else:
            result_list.append("FAIL")
            logs.warning("Verification Fail. Actual results: " + actual + ", Expected results: " + expected)
    except Exception as ex:
        result_list.append("FAIL")
        logs.exception("Verification FAIL. Exception Occured: " + str(ex))

def addAssertion(actual, expected):
    """ Add assertion to the list. Use this method if it is not the last assertion for a test case """
    setResult(actual, expected)

def lastAssertion(actual, expected, message):
    """
    Add assertion to the list. Check all results, return True if all assertions have been passed, False if not.
    Use this method if it is the last assertion for a test case.
    """
    setResult(actual, expected)
    if "FAIL" in result_list:
        logs.error("Assertion error. Failed test: " + inspect.stack()[1][3] + ", Message: " + str(message))
        result_list.clear()
        raise Exception("Assertion error. Failed test: " + inspect.stack()[1][3] + ", Message: " + str(message) + "; Actual: " + str(actual) + ", Expected: " + str(expected))
    else:
        logs.info("All verifications have been done successfully. TEST PASS: " + inspect.stack()[1][3] + ", Message: " + message)
        result_list.clear()
        assert True == True
