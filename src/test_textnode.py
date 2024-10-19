import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a test node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        self.assertEqual(node, node2)
        #self.assertEqual(node2, node3)
        #self.assertEqual(node3, node4)
        #self.assertEqual(node, node5)


if __name__ == "__main__":
    unittest.main()