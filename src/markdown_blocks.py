from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    splitted_block = block.split("\n")
    
    if block.startswith(("# ","## ","### ","#### ","##### ","###### ")):
        return BlockType.HEADING
    if block.startswith("```") or block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for block in splitted_block:
            if not block.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    if block.startswith("- "):
        for block in splitted_block:
            if not block.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith("1."):
        i = 1
        for block in splitted_block:
            if not block.startswith(f"{i}."):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    md_entries = markdown.split("\n\n")
    trimmed_md_entries = []
    for md_entry in md_entries:
        if md_entry == "":
            continue

        trimmed_md_entries.append(md_entry.strip())

    return trimmed_md_entries

