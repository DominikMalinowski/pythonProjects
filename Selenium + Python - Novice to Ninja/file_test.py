import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        print('SetUp before every test')

    def tearDown(self):
        print('TearDown after every test')

    def test_method_A(self):
        print('Test method A')
    
    def test_assert(self):
        a = True
        self.assertTrue(a, 'a is not true')

    def test_equal(self):
        a = 'test'
        b = 'test2'
        self.assertEqual(a,b, msg='Values are not equal')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

