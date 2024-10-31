import unittest
from textnode import *
from markdownhandler import *


class TestMarkdownHandler(unittest.TestCase):

    def test_split_delimiter_default(self):
        node = TextNode("Sample text with **bold text** in it.", TextType.TEXT)
        test_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(test_nodes, [TextNode('Sample text with ', TextType.TEXT, None), TextNode('bold text', TextType.BOLD, None), TextNode(' in it.', TextType.TEXT, None)])

    def test_split_delimiter_not_text(self):
        node = TextNode("Italicized sentence!", TextType.ITALIC)
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), [TextNode('Italicized sentence!', TextType.ITALIC, None)])
    
    def test_split_delimetir_broken_markup(self):
        node = TextNode("Sentence with `broken code markup.", TextType.TEXT)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node], "`", TextType.CODE))

    def test_markdown_img(self):
        text = "Look at this cool ![image!](https://www.google.com/img.png) And ![another](https://www.boot.dev/img.jpg) one."
        self.assertEqual(extract_markdown_images(text), [('image!', 'https://www.google.com/img.png'), ('another', 'https://www.boot.dev/img.jpg')])

    def test_markdown_url(self):
        text = "I think [Boot.dev](https://www.boot.dev/) is pretty cool."
        self.assertEqual(extract_markdown_links(text), [('Boot.dev', 'https://www.boot.dev/')])

if __name__ == "__main__":
    unittest.main()