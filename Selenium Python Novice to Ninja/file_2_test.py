import unittest

class TestCase2(unittest.TestCase):

    def setUp(self):
        print('SetUp before every test for second file')

    def tearDown(self):
        print('TearDown after every test for second file')

    def test_method_B(self):
        print('Test method A')
    
    def test_assert2(self):
        a = True
        self.assertTrue(a, 'a is not true')

    def test_equal2(self):
        a = 'second'
        b = 'second'
        self.assertEqual(a,b, msg='Values are not equal')
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

