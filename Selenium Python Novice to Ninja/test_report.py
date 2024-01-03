import pytest
from class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class TestReporting():

    @pytest.fixture(autouse = True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_method_E(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 20
        print('Running method  E')

    def test_method_F(self):
        result = self.abc.sumNumbers(2,8)
        assert result > 20
        print('Running method F')

# invoke py.test -v --html=<nazwapliku>.html 