import unittest
from textnode import TextNode, TextType
from markdownhandler import split_nodes_delimiter


class TestMarkdownHandler(unittest.TestCase):

    def test_split_delimiter_default(self):
        node = TextNode("Sample text with **bold text** in it.", TextType.TEXT)
        test_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(repr(test_nodes), "[TextNode(Sample text with , text, None), TextNode(bold text, bold, None), TextNode( in it., text, None)]")

    def test_split_delimiter_not_text(self):
        node = TextNode("Italicized sentence!", TextType.ITALIC)
        self.assertEqual(repr(split_nodes_delimiter([node], "*", TextType.ITALIC)), "[TextNode(Italicized sentence!, italic, None)]")
    
    def test_split_delimetir_broken_markup(self):
        node = TextNode("Sentence with `broken code markup.", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "`", TextType.CODE))

if __name__ == "__main__":
    unittest.main()