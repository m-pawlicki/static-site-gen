from textnode import *
import re
from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UO_LIST = "unordered_list"
    O_LIST = "ordered_list"

def markdown_to_block(markdown):
    blocks = []
    split_markdown = re.split('\n\n', markdown)
    for part in split_markdown:
        res = part.strip()
        if res != "":
            blocks.append(res)
    return blocks

def block_to_block_type(block):
    heading = r"^#{1,6} .*$"
    code = r"^```[\s\S]*```$"
    quote = r"^>.*$"
    unordered = r"^- .*$"
    ordered = r"^\d+\. .*$"
    order_nums = r"^(\d+)\. .*$"

    block_lines = block.split('\n')

    if re.match(heading, block):
        return BlockType.HEAD
    if re.match(code, block):
        return BlockType.CODE
    if all(re.match(quote, line) for line in block_lines):
        return BlockType.QUOTE
    if all(re.match(unordered, line) for line in block_lines):
        return BlockType.UO_LIST
    if all(re.match(ordered, line) for line in block_lines):
        numbers = [int(re.match(order_nums, line).group(1)) for line in block_lines]
        if numbers[0] == 1 and all(numbers[i] == numbers[i-1] + 1 for i in range(1, len(numbers))):
            return BlockType.O_LIST
    return BlockType.PARA