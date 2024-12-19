import unittest
from textnode import *
from blockhandler import *

class TestBlockHandler(unittest.TestCase):

    def test_markdown_to_text(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        test = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(markdown_to_block(markdown), test)

if __name__ == "__main__":
    unittest.main()