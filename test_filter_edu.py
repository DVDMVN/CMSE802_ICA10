import unittest
import filter_edu
from math import pi

class TestFilterEdu(unittest.TestCase):
    def test_filter(self):
        test_string = """
        randomemail@random.com
        michiganstate@msu.edu
        justanotheremail@email.org
        """

        self.assertListEqual(filter_edu(test_string), ["michiganstate@msu.edu"])
