import os
import shutil
from copystatic import copy_contents
from generate_page import generate_page, generate_pages_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"
template_path = "./template.html" 

def main():
    
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public dir")
    copy_contents(dir_path_public, dir_path_static)
    print("Generating the page")
    # generate_page("./content/index.md",template_path, "./public/index.html" )

    generate_pages_recursive("./content",template_path,dir_path_public)

main()