import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()