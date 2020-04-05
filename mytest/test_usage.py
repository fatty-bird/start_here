class TestUsage():
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def setup_method(self):
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")

    @classmethod
    def setup_class(cls):
        print("setup_class")

    def test_usage1(self):
        assert 2 == 3

    def test_usage(self):
        assert 1 == 1
