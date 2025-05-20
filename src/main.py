import os
import shutil
from copystatic import copy_contents
from generate_page import generate_page
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_contents(dir_path_public, dir_path_static)
    
    generate_page("./content/index.md","./template.html", "./public/index.html" )


main()