# require running as administrator and via "py.test" command in terminal 
import pytest 

def test_method_C(oneTimeSetUp, setUp):
    print('Running test C')

def test_method_D(oneTimeSetUp, setUp):
    print('Running test D')    