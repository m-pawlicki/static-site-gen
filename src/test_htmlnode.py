import unittest
from htmlnode import *


class TestTextNode(unittest.TestCase):

    def test_to_html_nyi(self):
        self.assertRaises(NotImplementedError, lambda: HTMLNode("p").to_html())

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode(props=props)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode("a", "Boot.dev is cool", None, {"href": "https://www.boot.dev/"})
        self.assertEqual("HTMLNode(a, Boot.dev is cool, children: None, {'href': 'https://www.boot.dev/'})", repr(node))

    def test_vals(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_leafnode_to_html_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com/"})
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com/\">Click me!</a>")

    def test_leafnode_to_html_eq2(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leafnode_to_html_raise(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, lambda: node.to_html())

    def test_parentnode_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    def test_nest_parentnode(self):
        node = ParentNode(
            "p",
            [ParentNode("b", 
                        [
                            LeafNode("i", "Italic text"),
                            LeafNode(None, "Normal text")
                        ],
                    )
                ],
            )
        self.assertEqual(node.to_html(), "<p><b><i>Italic text</i>Normal text</b></p>")

"""     def test_parentnode_no_child(self):
        self.assertRaises(ValueError, lambda: ParentNode(tag="div").to_html())

    def test_parentnode_no_tag(self):
        self.assertRaises(ValueError, lambda: ParentNode(children=[LeafNode("p", "Paragaph text.")]).to_html()) """

if __name__ == "__main__":
    unittest.main()