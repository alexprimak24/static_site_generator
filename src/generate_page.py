import os
from urllib.parse import urljoin
from pathlib import Path
from markdown_blocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    markdown_items = markdown_to_blocks(markdown)

    for markdown_item in markdown_items:
        if markdown_item.startswith("# "):
            return markdown_item[2:].strip()
        
    raise ValueError("no title found")
        

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path, "r")
    markdown_content = markdown.read()
    markdown.close()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()


    html_from_markdown = markdown_to_html_node(markdown_content).to_html()

    page_title = extract_title(markdown_content)

    updated_template = template.replace("{{ Title }}", page_title)
    updated_template = updated_template.replace("{{ Content }}", html_from_markdown)
    updated_template = updated_template.replace('href="/', f'href="{urljoin(basepath, "")}')
    updated_template = updated_template.replace('src="/', f'src="{urljoin(basepath, "")}')




    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    f = open(dest_path, "w")
    f.write(updated_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    for item in os.listdir(dir_path_content):
        currentpath = os.path.join(dir_path_content, item)
        path_to_move_to = os.path.join(dest_dir_path, item)
        print(f"! Copied from {currentpath} to {path_to_move_to}")

        if os.path.isfile(currentpath) and currentpath[-3:] == ".md":
            generate_page(currentpath,template_path, path_to_move_to[:-3] + ".html", basepath)
            continue
        if os.path.isfile(currentpath) and not currentpath[-3:] == ".md":
            raise Exception("Only markdown files supported")

        else:
            generate_pages_recursive(currentpath, template_path, path_to_move_to, basepath) 
