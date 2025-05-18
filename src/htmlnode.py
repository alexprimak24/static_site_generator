class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        str = ""
        for node in self.props:
            str += f' {node}="{self.props[node]}"'
        
        return str
    
    def __eq__(self, other):
        return (self.tag == other.tag 
                and self.value == other.value 
                and self.children == other.children
                and self.props == other.props
                )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value")
        if self.tag == None:
            return self.value

        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have a children")
        def children_to_html(children):
            if not children:
                return ""
            return children[0].to_html() + children_to_html(children[1:])
        
        prettyfied_children = children_to_html(self.children)
            
        return f"<{self.tag}{super().props_to_html() if self.props else ''}>{prettyfied_children}</{self.tag}>"
