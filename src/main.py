import os
import shutil
from copystatic import copy_contents
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    

    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_contents(dir_path_public, dir_path_static)


main()