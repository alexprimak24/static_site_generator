import os
import shutil


def copy_contents(copy_to, copy_from):
    
    if not os.path.exists(copy_to):
        os.mkdir(copy_to)
    
    for item in os.listdir(copy_from):
        currentpath = os.path.join(copy_from, item)
        path_to_move_to = os.path.join(copy_to, item)
        print(f"! Copied from {currentpath} to {path_to_move_to}")
        
        if os.path.isfile(currentpath):
            shutil.copy(currentpath, path_to_move_to)
            print(f"! Copied from {currentpath} to {path_to_move_to}")
            print(f"! Copied from {currentpath} to {path_to_move_to}")
        else:
            os.mkdir(path_to_move_to)
            copy_contents(path_to_move_to, currentpath)
