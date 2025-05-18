import unittest

from htmlnode import HTMLNode, LeafNode,ParentNode

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

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div",None)
        with self.assertRaises(Exception) as context:
            parent_node.to_html()

        self.assertTrue("ParentNode must have a children" in str(context.exception))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props_and_children(self):
        child_node = LeafNode("p", "hi there")
        parent_node = ParentNode("a", [child_node],  {"href": "https://www.google.com"})

        self.assertEqual(parent_node.to_html(),'<a href="https://www.google.com"><p>hi there</p></a>')



if __name__ == "__main__":
    unittest.main()