import os, shutil

def copy_static(source, destination):
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    
    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)
        if os.path.isfile(src):
            print(f"Copying file: {src} -> {dst}")
            shutil.copy(src, dst)
        if os.path.isdir(src):
            os.mkdir(dst)
            copy_static(src, dst)