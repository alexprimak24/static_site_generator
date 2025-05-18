import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('h1', '24px', "body", {"href": "https://www.google.com"})
        node1 = HTMLNode('h1', '24px', "body", {"href": "https://www.google.com"})


        self.assertEqual(node,node1)

    def test_eq_false(self):
        node = HTMLNode("h1")
        node1 = HTMLNode("h1", "24px")
        self.assertNotEqual(node,node1)

    def test_value(self):
        node = HTMLNode("div", "I wish I could read")

        self.assertEqual(
            node.tag,
            "div"
        )

        self.assertEqual(
            node.value,
            "I wish I could read"
        )

        self.assertEqual(
            node.children,
            None
        )
        
        self.assertEqual(
            node.props,
            None
        )

    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        node = HTMLNode(props=test_props)
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello World")
        self.assertEqual(node.to_html(), "Hello World")

if __name__ == "__main__":
    unittest.main()