from textnode import *
from htmlnode import *
from blockhandler import *
from inlinehandler import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case BlockType.QUOTE:
                quote_md_to_html(block)
            case BlockType.UO_LIST:
                ul_md_to_html(block)
            case BlockType.O_LIST:
                ol_md_to_html(block)
            case BlockType.CODE:
                code_md_to_html(block)
            case BlockType.HEAD:
                head_md_to_html(block)
            case _:
                para_md_to_html(block)

    #assign proper child htmlnodes to block -- text_to_children(text)
    #parent html node <div> with children derived from above
    pass

def text_to_children(text):
    html_nodes = []
    txt_nodes = text_to_textnodes(text)
    for node in txt_nodes:
        html_nodes.append(node.text_node_to_html_node())
    return html_nodes

def quote_md_to_html(md):
    pass

def ul_md_to_html(md):
    pass

def ol_md_to_html(md):
    pass

def code_md_to_html(self):
    pass

def head_md_to_html(self):
    pass

def para_md_to_html(self):
    pass