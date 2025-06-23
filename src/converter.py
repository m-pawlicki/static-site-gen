from textnode import *
from htmlnode import *
from blockhandler import *
from inlinehandler import *
import re

def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_block(markdown)

    for block in blocks:
        match block_to_block_type(block):
            case BlockType.QUOTE:
                node = quote_md_to_html(block)
            case BlockType.UO_LIST:
                node = ul_md_to_html(block)
            case BlockType.O_LIST:
                node = ol_md_to_html(block)
            case BlockType.CODE:
                node = code_md_to_html(block)
            case BlockType.HEAD:
                node = head_md_to_html(block)
            case _:
                node = para_md_to_html(block)
        block_nodes.append(node)

    parent_node = ParentNode("div", block_nodes)
    return parent_node

def text_to_children(text):
    child_nodes = []
    txt_nodes = text_to_textnodes(text)

    for node in txt_nodes:
        html_node = node.text_node_to_html_node()
        child_nodes.append(html_node)

    return child_nodes

def quote_md_to_html(md):
    lines = md.split("\n")
    processed_lines = [line.lstrip(">").strip() for line in lines]
    children = text_to_children("\n".join(processed_lines))
    return HTMLNode("blockquote", None, children, None)

def ul_md_to_html(md):
    lines = md.split("\n")
    cleaned_lines = [line.lstrip("*-").strip() for line in lines]
    processed_nodes = []
    for line in cleaned_lines:
        processed_nodes.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ul", processed_nodes)

def ol_md_to_html(md):
    lines = md.split("\n")
    cleaned_lines = [line.split(".", 1)[1].strip() for line in lines]
    processed_nodes = []
    for line in cleaned_lines:
        processed_nodes.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ol", processed_nodes)
    
def code_md_to_html(md):
    lines = md.split('\n')
    content_lines = lines[1:-1]
    stripped_lines = [line.lstrip() for line in content_lines]
    content = '\n'.join(stripped_lines) + '\n'
    inner_node = [LeafNode("code", content)]
    return ParentNode("pre", inner_node)

def head_md_to_html(md):
    parts = md.split(" ", 1)
    tag = "h" + str(parts[0])
    children = text_to_children(parts[1])
    return ParentNode(tag, children)

def para_md_to_html(md):
    strip = re.sub(r'\s+', ' ', md.strip())
    children = text_to_children(strip)
    return ParentNode("p", children)