# test_load_html.py
import unittest
from html import load_html

class TestLoadHtml(unittest.TestCase):

    def test_load_html_success(self):
        result = load_html("https://instagram.com")
        self.assertGreater(len(result), 0)

    def test_load_html_failure(self):
        with self.assertRaises(Exception):
            load_html("http://bad.url.that.does.not.exist")

if __name__ == "__main__":
    unittest.main()
