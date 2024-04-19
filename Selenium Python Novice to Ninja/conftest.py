
import pytest 

@pytest.fixture()
def setUp():
    print('Running SetUp')
    yield
    print('Running TearDown')

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print('Running one time SetUp')
    yield
    print('Running one time TearDown')

# def pytest_add_option(parser):
#     parser.addoption("--browser")
#     parser.addoption("--ostype", help ="Windows/Mac")

# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")

# @pytest.fixture(scope="session")
# def ostype(request):
#     return request.config.getoption("--ostype")
