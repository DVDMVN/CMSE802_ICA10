#Unit test for combine.py
import unittest
from combine import combine_handles

class TestCombineHandles(unittest.TestCase):

    #First test case: All valid emails
    def test_all_valid_emails(self):
        self.assertEqual(combine_handles(["a@msu.edu", "b@msu.edu", "c@msu.edu"]), "a,b,c")