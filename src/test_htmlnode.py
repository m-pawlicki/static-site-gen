import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        props1 = { "href": "https://www.google.com", "target": "_blank",}
        props2 = { "href": "https://www.boot.dev"}
        node1 = HTMLNode(props=props1)
        node2 = HTMLNode(props=props2)
        print(node2)
        html_test = node1.props_to_html()
        print(html_test)



if __name__ == "__main__":
    unittest.main()