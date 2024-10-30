import unittest
from textnode import TextNode, TextType
from splitdelimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a test node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev/")
        node2 = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev/")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev/")
        self.assertEqual("TextNode(This is a text node, bold, https://www.boot.dev/)", repr(node))

    def test_text_to_html_node(self):
        node = TextNode("Try out Boot.dev today!", TextType.LINK, "https://www.boot.dev/")
        self.assertEqual(node.text_node_to_html_node().to_html(), '<a href="https://www.boot.dev/">Try out Boot.dev today!</a>')

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