
import pytest 

@pytest.fixture()
def setUp():
    print('Before every test')

def test_method_C(setUp):
    print('Running test C')

def test_method_D(setUp):
    print('Running test D')    