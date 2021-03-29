import selenium
import requests




import unittest

class TesDemo(unittest.TestCase):



    def tearDown(self) ->None:
        print ("tear down")
    def test_abc(self):
        print ("test abs")
    def setUp(self) -> None:
        print ("set up")
    def test_upper(self):
        print ("test_upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print ("test_isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print ("test_split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
