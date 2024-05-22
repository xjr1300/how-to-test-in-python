# ruff: noqa
import unittest


class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        print("setUpClass was called!")

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        print("tearDownClass was called!")

    def setUp(self) -> None:
        super().setUp()
        print("setUp was called!")

    def tearDown(self) -> None:
        super().tearDown()
        print("tearDown was called!")

    def test_foo(self) -> None:
        print("[test case] test_foo was called!")

    def test_bar(self) -> None:
        print("[test case] test_bar was called!")


if __name__ == "__main__":
    unittest.main()
