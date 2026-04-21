import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Hello", TextType.TEXT, "http://example.com")
        node2 = TextNode("Hello", TextType.TEXT, "http://example.com")
        node3 = TextNode("Hello", TextType.TEXT)
        node4 = TextNode("Hello", TextType.ITALIC, "http://example.com")
        node5 = TextNode("Click here", TextType.BOLD)

        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)
        self.assertNotEqual(node1, node5)


if __name__ == "__main__":
    unittest.main()
