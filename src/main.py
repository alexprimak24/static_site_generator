import os
import sys
import shutil
from copystatic import copy_contents
from generate_page import generate_pages_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html" 
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public dir")
    copy_contents(dir_path_docs, dir_path_static)
    print("Generating the page")

    generate_pages_recursive(dir_path_content,template_path,dir_path_docs, basepath)

main()