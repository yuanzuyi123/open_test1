import  unittest


class Search:

    def search_fun(self):
        print ("search")
        return True

class   TestSearch(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            print("set up class")
            cls.search =  Search()

        @classmethod
        def tearDownClass(cls):
            print ("tear down class")

        def setUp(self) -> None:
            print("set up")

        def tearDown(self) -> None:
            print("tear down")
        def test_search(self):
            print('test_seacher')

            assert True == self.search.search_fun()

        def test_search1(self):
            print('test_seacher1')

            assert True == self.search.search_fun()
        def test_search2(self):
            print('test_seacher2')

            assert True == self.search.search_fun()


class TestSearch1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("set up class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("tear down class")
    def setUp(self) -> None:
        print ("set up2")
    def tearDown(self) ->None:
        print ("tear down2")
    def test_search(self):
        print('test_seacher')

        assert True == self.search.search_fun()

    def test_search1(self):
        print('test_seacher1')

        assert True == self.search.search_fun()

    def test_search2(self):
        print('test_seacher2')

        assert True == self.search.search_fun()
class TestSearch2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def setUp(self) -> None:
        print("set up2")

    def tearDown(self) -> None:
        print("tear down2")

    def test_search(self):
        print('test_seacher2')

        assert True == self.search.search_fun()

    def test_search1(self):
        print('test_seacher12')

        assert True == self.search.search_fun()

    def test_search2(self):
        print('test_seacher22')

        assert True == self.search.search_fun()

if __name__ == '__main__':
    #unittest.main()
    # suite  = unittest.TestSuite()
    # suite.addTest(TestSearch1("test_search1"))
    # suite.addTest(TestSearch1("test_search2"))
    # unittest.TextTestRunner().run(suite)

    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)

    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearch2)
    suite = unittest.TestSuite([suite1,suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)