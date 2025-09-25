# test_load_html.py
import unittest
from html import load_html

class Test_LoadHtml(unittest.TestCase):
    def test_load_html(self):
        self.assertEqual(load_html("url"), "<html>OK</html>")

if __name__ == "__main__":
    unittest.main()
