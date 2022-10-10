from helpers.screenshot_listener import ScreenshotListener

def screenshot_decorator(test_fun):
   def wrapper(self):
       try:
           return test_fun(self)
       except AssertionError as ex:
           ScreenshotListener().on_exception(ex, self.ef_driver)
           raise ex

   return wrapper