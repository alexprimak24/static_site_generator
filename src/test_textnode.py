import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2) 

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC,"https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC,"https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_wrong_format(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        html_mode = text_node_to_html_node(node)
        
        self.assertEqual(html_mode.tag, "img")

    def test_split_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        expected_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        
        self.assertEqual(new_nodes, expected_out)

    def test_split_multiple_delimiter(self):
        node = TextNode("This is text with a **code block** word of **tanks**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        expected_out = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.BOLD),
            TextNode(" word of ", TextType.TEXT),
            TextNode("tanks", TextType.BOLD)
        ]
        
        self.assertEqual(new_nodes, expected_out)


        

if __name__ == "__main__":
    unittest.main()