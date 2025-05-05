import unittest
from textnode import *
from blockhandler import *

class TestBlockHandler(unittest.TestCase):

    def test_markdown_to_block(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        test = ["# This is a heading", "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", "- This is the first list item in a list block\n- This is a list item\n- This is another list item"]
        self.assertEqual(markdown_to_block(markdown), test)

    def test_block_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_block_heading_too_many(self):
        block = "####### Uh oh, too many!"
        self.assertIsNot(block_to_block_type(block), BlockType.HEAD)

    def test_block_code(self):
        block = "``` A simple block\nof code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_code_no_end(self):
        block = "```I forgor to end my code block..."
        self.assertIsNot(block_to_block_type(block), BlockType.CODE)

    def test_block_unordered(self):
        block = "- Wowee\n- Look at this\n- List!"
        self.assertEqual(block_to_block_type(block), BlockType.UO_LIST)

    def test_block_unordered_wrong(self):
        block = "-There is\nNo middle\n-List option"
        self.assertIsNot(block_to_block_type(block), BlockType.UO_LIST)

    def test_block_ordered(self):
        block = "1. Tomatoes\n2. Corn\n3. Laser Gun"
        self.assertEqual(block_to_block_type(block), BlockType.O_LIST)
    
    def test_block_ordered_wrong(self):
        block = "1. Three\n3. Two\n4. One\n5. Miku Miku Beam"
        self.assertIsNot(block_to_block_type(block), BlockType.O_LIST)

    def test_paragraph(self):
        block = "A simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

if __name__ == "__main__":
    unittest.main()