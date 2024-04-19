









                                                        ########## OLD VERSION ##########
#"""
#conftest.py stores fixtures (pytest feature)
#"""
#
#import pytest
#from Selenium.Pages.LoginPage import LoginPage
#from Selenium.Base.SeleniumDriver import SeleniumDriver
#
#def tearDown():
#    """ After all Tests close the driver """
#    SeleniumDriver.driver.close()
#    SeleniumDriver.driver.quit()
#
#@pytest.fixture(scope="session", autouse=True)
#def setUp(request):
#    """ At the beginning of the Tests, log into the system. It's being executed after creating the driver. """
#    request.addfinalizer(tearDown)
