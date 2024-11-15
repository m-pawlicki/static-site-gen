from textnode import *
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        split = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax.")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split.append(TextNode(sections[i], TextType.TEXT))
            else:
                split.append(TextNode(sections[i], text_type))
        nodes.extend(split)
            
    return nodes

def extract_markdown_images(text):
     return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        split = []
        extract = extract_markdown_images(node.text)
        remaining_text = node.text
        if len(extract) == 0:
            return old_nodes
        for pair in extract:
            alt_txt = pair[0]
            img_url = pair[1]
            sections = list(filter(None, remaining_text.split(f"![{alt_txt}]({img_url})", 1)))
            split.append(TextNode(sections[0], TextType.TEXT))
            split.append(TextNode(alt_txt, TextType.IMAGE, img_url))
            remaining_text = sections[1]
        split.append(TextNode(remaining_text, TextType.TEXT))
        nodes.extend(split)
    
    return nodes
    
               

def extract_markdown_links(text):
     return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            nodes.append(node)
            continue
        split = []
        extract = extract_markdown_links(node.text)
        remaining_text = node.text
        if len(extract) == 0:
            return old_nodes
        for pair in extract:
            link_txt = pair[0]
            link_url = pair[1]
            sections = list(filter(None, remaining_text.split(f"[{link_txt}]({link_url})", 1)))
            split.append(TextNode(sections[0], TextType.TEXT))
            split.append(TextNode(link_txt, TextType.LINK, link_url))
            if 1 <= len(sections):
                continue
            else:
                remaining_text = sections[1]
        split.append(TextNode(remaining_text, TextType.TEXT))
        nodes.extend(split)
    
    return nodes