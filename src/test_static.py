import unittest, os
from static import *

class TestStatic(unittest.TestCase):

    def test_incomplete_header(self):
        with self.assertRaises(Exception):
            extract_title("# \n")

    def test_proper_header(self):
        print(f"Current working dir: {os.getcwd()}")
        header = extract_title("# A Valid Header")
        self.assertEqual(header, "A Valid Header")

    def test_no_header(self):
        with self.assertRaises(Exception):
            extract_title("Oops, no header!")

if __name__ == "__main__":
    unittest.main()