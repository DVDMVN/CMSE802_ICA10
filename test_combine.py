#Unit test for combine.py
import unittest
from combine import combine_handles

class TestCombineHandles(unittest.TestCase):

    #First test case: All valid emails
    def test_all_valid_emails(self):
        self.assertEqual(combine_handles(["a@msu.edu", "b@msu.edu", "c@msu.edu"]), "a,b,c")

    #Second test case: Non-email strings
    def test_non_email_strings(self):
        self.assertEqual(combine_handles(["test@msu.edu", "invalid_email", "test2@msu.edu"]), "test,test2")
