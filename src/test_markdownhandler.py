import unittest
from textnode import *
from markdownhandler import *


class TestMarkdownHandler(unittest.TestCase):

    def test_split_delimiter_default(self):
        node = TextNode("Sample text with **bold** in it.", TextType.TEXT)
        test_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(test_nodes, [TextNode('Sample text with ', TextType.TEXT, None), TextNode('bold', TextType.BOLD, None), TextNode(' in it.', TextType.TEXT, None)])

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

    def test_split_img(self):
        node = TextNode("This is text with ![a random image](https://www.boot.dev/test.png) and a link [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [TextNode('This is text with ', TextType.TEXT), TextNode('a random image', TextType.IMAGE, 'https://www.boot.dev/test.png'), TextNode(' and a link [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)])

    def test_split_img_no_imgs(self):
        node = TextNode("This text has no images in it!", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [TextNode('This text has no images in it!', TextType.TEXT, None)])

    def test_split_multi_imgs(self):
        node = TextNode("This text has ![multiple](img1.png) kinds of ![images](img2.png) in it.", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [TextNode('This text has ', TextType.TEXT), TextNode('multiple', TextType.IMAGE, 'img1.png'), TextNode(' kinds of ', TextType.TEXT), TextNode('images', TextType.IMAGE, 'img2.png'), TextNode(' in it.', TextType.TEXT)])

    def test_split_link(self):
        node = TextNode("This is text with ![a random image](test.png) and a link [to youtube](https://www.youtube.com/)", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [TextNode('This is text with ![a random image](test.png) and a link ', TextType.TEXT), TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/')])

    def test_split_link_no_links(self):
        node = TextNode("This text has no links in it!", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [TextNode('This text has no links in it!', TextType.TEXT)])

    def test_split_multi_links(self):
        pass

if __name__ == "__main__":
    unittest.main()