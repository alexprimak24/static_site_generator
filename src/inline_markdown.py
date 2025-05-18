from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    try:
        if text_type == TextType.TEXT:
            return old_nodes
        
        splitted_nodes = old_nodes[0].text.split(delimiter)

        new_nodes = []

        for i in range(0, len(splitted_nodes)):
            if not splitted_nodes[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(splitted_nodes[i], TextType.TEXT))
            
            else:
                new_nodes.append(TextNode(splitted_nodes[i],text_type))

        return new_nodes
    
    except:
        raise ValueError("Invalid Markdown syntax")