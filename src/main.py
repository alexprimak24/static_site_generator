from textnode import TextNode, TextType

def main():
    new_text_node = TextNode("This is some anchor text",TextType.LINK, "https://www.boot.dev")    

    print(repr(new_text_node))
main()