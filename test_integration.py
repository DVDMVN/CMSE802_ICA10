from pipeline import msu_handle_finder
import unittest

class TestIntegration(unittest.TestCase):
    def test_integration_get_nothing(self):
        test_url_1 = "http://example.com"

        print(msu_handle_finder(test_url_1))
        self.assertEqual(msu_handle_finder(test_url_1), "")

    def test_integration_get_something(self):
        test_url_2 = "https://grad.msu.edu/departments/computational-mathematics-science-and-engineering"

        self.assertEqual(msu_handle_finder(test_url_2), "cmsegrad,cmsegrad,cmsegrad,cmsegrad,cmsegrad,cmsegrad,cmsegrad,cmsegrad")