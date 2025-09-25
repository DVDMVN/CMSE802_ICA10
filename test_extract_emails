import unittest
from extract import extract_emails

class TestExtractEmails(unittest.TestCase):

    def test_extracts_valid_emails(self):
        html = """
        <p>Contact: alice@msu.edu</p>
        <p>External: bob@gmail.com</p>
        """
        emails = extract_emails(html)
        self.assertIn("alice@msu.edu", emails)
        self.assertIn("bob@gmail.com", emails)

    def test_ignores_invalid_emails(self):
        html = "<p>Not an email: test@</p>"
        emails = extract_emails(html)
        self.assertEqual(emails, [])

    def test_empty_input(self):
        self.assertEqual(extract_emails(""), [])

    def test_wrong_type_raises(self):
        with self.assertRaises((TypeError, ValueError)):
            extract_emails(None)

if __name__ == "__main__":
    unittest.main()
