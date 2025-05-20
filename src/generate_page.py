from markdown_blocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    markdown_items = markdown_to_blocks(markdown)

    for markdown_item in markdown_items:
        if markdown_item.startswith("# "):
            return markdown_item[2:].strip()
        
    raise ValueError("no title found")
        

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path, "r")
    markdown_content = markdown.read()
    markdown.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()


    html_from_markdown = markdown_to_html_node(markdown_content).to_html()

    page_title = extract_title(markdown_content)

    updated_template = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_from_markdown)
    
    f = open(dest_path, "w")
    f.write(updated_template)



