from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
        nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                nodes.append(node)
            elif len(node.text.split(delimiter,3)) != 3:
                 raise Exception("Invalid markdown syntax.")
            else:
                 split = node.text.split(delimiter, 3)
                 new_node_one = TextNode(split[0], TextType.TEXT)
                 new_node_two = TextNode(split[1], text_type)
                 new_node_three = TextNode(split[2], TextType.TEXT)
                 nodes.extend([new_node_one,new_node_two,new_node_three])

            
        return nodes