import unittest

from generate_page import extract_title



class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        md = """
        # Tolkien Fan Club

        # Tolkien Fan Club

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        self.assertEqual(extract_title(md), "Tolkien Fan Club")


if __name__ == "__main__":
    unittest.main()

