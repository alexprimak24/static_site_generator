import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Hi"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Hi"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Hi"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Hi"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("##### Hi"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Hi"), BlockType.HEADING)
    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> hi\n> hi"), BlockType.QUOTE)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\nhi\n```"), BlockType.CODE)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- hi\n- hi"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("1. hi\n2.hi"), BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("hi"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()