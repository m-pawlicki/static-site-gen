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
            nodes.append(node)
            continue
        for pair in extract:
            alt_txt = pair[0]
            img_url = pair[1]
            sections = remaining_text.split(f"![{alt_txt}]({img_url})", 1)
            if sections[0] != "":
                split.append(TextNode(sections[0], TextType.TEXT))
            split.append(TextNode(alt_txt, TextType.IMAGE, img_url))
            if len(sections) > 1:
                remaining_text = sections[1]
        if len(sections) > 1:
            if remaining_text != "":
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
            nodes.append(node)
            continue
        for pair in extract:
            link_txt = pair[0]
            link_url = pair[1]
            sections = remaining_text.split(f"[{link_txt}]({link_url})", 1)
            if sections[0] != "":
                split.append(TextNode(sections[0], TextType.TEXT))
            split.append(TextNode(link_txt, TextType.LINK, link_url))
            if len(sections) > 1:
                remaining_text = sections[1]
        if len(sections) > 1:
            if remaining_text != "":
                split.append(TextNode(remaining_text, TextType.TEXT))
        nodes.extend(split)
    
    return nodes

def text_to_textnodes(text):
    aggregate_nodes = []
    old_nodes = [TextNode(text, TextType.TEXT)]
    bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    link = split_nodes_link(code)
    img = split_nodes_image(link)
    aggregate_nodes.extend(img)
    return aggregate_nodes