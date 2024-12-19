from textnode import *
import re

def markdown_to_block(markdown):
    blocks = []
    split_markdown = re.split('\n\n', markdown)
    for part in split_markdown:
        res = part.strip()
        if res != "":
            blocks.append(res)
    return blocks