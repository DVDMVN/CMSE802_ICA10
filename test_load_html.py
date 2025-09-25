import unittest
from unittest.mock import patch, Mock
import requests
from html import load_html

class Test_LoadHtml(unittest.TestCase):

    @patch("html.requests.get")
    def test_load_html_success(self, mock_get):
        fake_response = Mock()
        fake_response.text = "<html>OK</html>"
        fake_response.raise_for_status = Mock()
        mock_get.return_value = fake_response

        result = load_html("http://walmart.com")
        self.assertEqual(result, "<html>OK</html>")

    @patch("html.requests.get")
    def test_load_html_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("boom")

        with self.assertRaises(requests.exceptions.RequestException):
            load_html("http://fnsdjkfd.com")

if __name__ == "__main__":
    unittest.main()
