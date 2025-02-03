from textnode import *
import re
import enum

class BlockType(enum):
    HEADING = r"^#{1,6}\s.*"
    CODE = r"^`{3}.*\s*`{3}$"
    QUOTE = r"^>"
    ULIST = r"^[\*|-]\s"
    OLIST = r"^(\d+).\s"
    

def markdown_to_block(markdown):
    blocks = []
    split_markdown = re.split('\n\n', markdown)
    for part in split_markdown:
        res = part.strip()
        if res != "":
            blocks.append(res)
    return blocks

def block_to_block_type(block):
    type = "paragraph"
    if re.search(BlockType.HEADING, block):
        type = "heading"
    elif re.search(BlockType.CODE, block):
        type = "code"
    elif re.search(BlockType.QUOTE, block):
        type = "quote"
    elif re.search(BlockType.ULIST, block):
        type = "unordered list"
    elif re.search(BlockType.OLIST, block):
        type = "ordered list"
    return type