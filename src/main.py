from textnode import TextNode, TextType


def main():
    # Example usage
    node1 = TextNode("Hello, World!", TextType.TEXT)
    node2 = TextNode("Click here", TextType.BOLD, url="https://example.com")
    print(node1)
    print(node2)


if __name__ == "__main__":
    main()
